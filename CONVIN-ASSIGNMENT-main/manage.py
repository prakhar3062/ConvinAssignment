#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE', 'tutorial.settings'))

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
