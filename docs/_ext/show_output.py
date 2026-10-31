"""
Execute selected Python examples and display their standard output.

Add ``:show-output:`` to ``literalinclude`` to append a collapsed
``Show Output`` block. Source selection options affect only the displayed
code: the complete file runs in a fresh interpreter during the Sphinx build.
Examples must print their results and finish within the execution timeout.
Use ``:output-language: python`` to highlight Python representations;
output is plain text by default.
"""

import os
import subprocess  # noqa: S404
import sys
from pathlib import Path
from typing import ClassVar, Final, override

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.directives.code import LiteralInclude
from sphinx.errors import SphinxError
from sphinx_immaterial.code_annotations import annotations_list

_PROJECT_ROOT: Final = Path(__file__).resolve().parents[2]
_EXECUTION_TIMEOUT: Final = 30


def _example_environment(root: Path) -> dict[str, str]:
    """Preserve build settings while preferring local imports and UTF-8."""
    environment = os.environ.copy()
    python_path = environment.get('PYTHONPATH')
    environment['PYTHONPATH'] = (
        os.pathsep.join((str(root), python_path)) if python_path else str(root)
    )
    environment['PYTHONIOENCODING'] = 'utf-8'
    return environment


def _execute_example(example: Path) -> str:
    """
    Execute a Python file from the project root and return its stdout.

    Use the build's interpreter so examples see the same dependencies as
    autodoc. A separate process keeps their imports and global state out of
    Sphinx. Nothing is fetched from the generated image URLs.

    Raises:
        SphinxError: If the file is not Python, fails to execute, exceeds
            the timeout, or prints no non-whitespace output.
    """
    if example.suffix != '.py':
        raise SphinxError(f':show-output: requires a Python file: {example}')

    stdout = _run_example(example)
    if not stdout.strip():
        raise SphinxError(f'Example {example} produced no stdout')
    return stdout


def _run_example(example: Path) -> str:
    """Capture stdout and report execution failures with the example path."""
    try:
        process = subprocess.run(  # noqa: S603
            [sys.executable, str(example)],
            cwd=_PROJECT_ROOT,
            env=_example_environment(_PROJECT_ROOT),
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=_EXECUTION_TIMEOUT,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise SphinxError(
            f'Example {example} failed (exit {exc.returncode}):\n'
            f'{exc.stdout}{exc.stderr}',
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise SphinxError(
            f'Example {example} exceeded {_EXECUTION_TIMEOUT} seconds',
        ) from exc
    except OSError as exc:
        raise SphinxError(
            f'Could not execute example {example}: {exc}'
        ) from exc
    return process.stdout


def _create_output_node(stdout: str, language: str) -> nodes.admonition:
    """
    Build a themed, collapsed result containing literal text.

    Construct Docutils nodes directly, as in DMR's example extension.
    Printed reStructuredText or HTML stays literal instead of being parsed
    as documentation markup. Sphinx handles escaping and code highlighting.
    """
    literal = stdout.rstrip('\r\n')
    output = nodes.literal_block(literal, literal)
    output['language'] = language
    return nodes.admonition(
        '',
        nodes.title('', 'Show Output'),
        output,
        collapsible='',
        classes=['show_output'],
    )


class ExecutedLiteralInclude(LiteralInclude):
    """
    Include source and optionally append the complete file's actual output.

    Regular includes keep Sphinx's behavior. Execution is opt-in through
    ``:show-output:`` and only runs when source inclusion succeeds. The
    parent directive tracks the example as a dependency for rebuilds.
    """

    option_spec: ClassVar = {
        **LiteralInclude.option_spec,
        'show-output': directives.flag,
        'output-language': directives.unchanged_required,
    }

    @override
    def run(self) -> list[nodes.Node]:
        """Render source, execute the selected example, and append stdout."""
        rendered = super().run()
        if 'show-output' not in self.options or any(
            isinstance(node, nodes.system_message) for node in rendered
        ):
            return rendered

        example = Path(self.env.relfn2path(self.arguments[0])[1])
        output = _create_output_node(
            _execute_example(example),
            self.options.get('output-language', 'text'),
        )
        self.set_source_info(output)
        return [*rendered, output]


def _arrange_annotations(_app: Sphinx, document: nodes.document) -> None:
    """
    Keep code annotations beside their source, before the generated result.

    The theme requires the annotation list immediately after the code block.
    Move it ahead of our inserted result so both features work together.
    """
    for annotation in document.findall(annotations_list):
        parent = annotation.parent
        if parent is None:
            continue

        index = parent.index(annotation)
        previous = parent[index - 1] if index else None

        if (
            isinstance(previous, nodes.admonition)
            and ('show_output' in previous.get('classes', ()))  # pyright: ignore[reportUnnecessaryContains]
        ):
            parent.remove(annotation)
            parent.insert(index - 1, annotation)


def setup(app: Sphinx) -> dict[str, bool]:
    """Replace literalinclude while allowing parallel reads and writes."""
    app.add_directive('literalinclude', ExecutedLiteralInclude, override=True)
    app.add_css_file('show_output.css')
    app.connect('doctree-read', _arrange_annotations)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
