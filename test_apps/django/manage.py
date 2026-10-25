"""Django's command-line utility for administrative tasks."""

import os
import sys


def main() -> None:  # pragma: no cover
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

    from django.core.management import execute_from_command_line  # noqa: PLC0415

    execute_from_command_line(sys.argv)


if __name__ == '__main__':  # pragma: no cover
    main()
