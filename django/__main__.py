"""
Invokes django-admin when the django module is run as a script.

Example: python -m django check
"""
from django.core import management

if __name__ == "__main__":
    # handles the scenario when we run django module as script
    # we setup __main__.py and this is called when a module in called as script
    # e.g. python -m django 
    management.execute_from_command_line()
