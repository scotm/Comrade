#!/usr/bin/env python
# coding=utf-8
import sys

import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Comrade.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
