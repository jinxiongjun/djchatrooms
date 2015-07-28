#!/usr/bin/env python
#how to load module
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djchatrooms.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
