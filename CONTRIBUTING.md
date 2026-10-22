# How to contribute

Please read our [AI Policy](.github/AI_POLICY.md) before contributing.

## Dependencies

The project requires Python 3.12 or newer (within Python 3).
We use [Poetry](https://github.com/python-poetry/poetry) to manage dependencies.

To install them:

```bash
poetry install
```

The commands below use `poetry run`, so you do not need to activate
the virtual environment.

## One magic command

Run `make check` to run linting, type checks, package checks, and all tests!
Docker is required for integration tests. Documentation is built separately.

## Tests

To run all tests, including integration tests (requires Docker):

```bash
make test
```

To run unit tests only:

```bash
make unit
```

`make unit` also runs pytest doctests in Python docstrings, `*.rst` files,
and `README.md`. Write executable examples with `>>>` prompts and expected
output; ordinary Python code fences are not executed. Leave a blank line after
the expected output before closing a Markdown code fence.

To run linting:

```bash
make lint
```

To check types:

```bash
make type-check
```

`make lint` also checks slots and import architecture. `make package` checks
that `poetry.lock` matches `pyproject.toml` and installed dependencies agree.

These checks also run in CI.

## Documentation

To install the documentation dependencies and build the HTML documentation:

```bash
poetry install --with docs
make docs
```

The output is in `docs/_build/html`. The build treats warnings as errors.

## Submitting your code

We use [trunk based](https://trunkbaseddevelopment.com/)
development (we also sometimes call it `wemake-git-flow`).

What is the point of this method?

1. We use protected `master` branch,
   so the only way to push your code is via pull request
2. We use issue branches: to implement a new feature or to fix a bug
   create a new branch named `issue-$TASKNUMBER`
3. Then create a pull request to `master` branch
4. We use `git tag`s to make releases, so we can track what has changed
   since the latest release

So, this way we achieve an easy and scalable development process
which frees us from merging hell and long-living branches.

The latest development version of the library is always in the `master` branch.

### Before submitting

Before submitting your code please do the following steps:

1. Run `make check` to make sure everything was working before
2. Add any changes you want
3. Add tests for the new changes
4. Edit documentation if you have changed something significant
5. Update `CHANGELOG.md` with a quick summary of your changes
6. Run `make check` again to make sure it is still working

If you changed the documentation, run `make docs` as well.

## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
