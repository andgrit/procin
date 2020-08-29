"""Top-level package for procin."""
__author__ = """Powell Quiring"""
__email__ = 'powellquiring@gmail.com'
__version__ = '0.1.0'

import subprocess
import typing
import json

class Command:
    def __init__(self, print_output=False, print_error=True, cache=False, cache_dir="~/procin"):
        self.print_output = print_output
        self.print_error = print_error
        self.cache = cache
        self.cache_dir = cache_dir
    def run(self, command):
        try:
            out = subprocess.check_output(command)
            stdout = out.decode()
        except subprocess.CalledProcessError:
            print('*** Command execution failed')
        return stdout
    def run_json(self, command):
        return json.loads(self.run(command))

def log_command(command, **kwargs):
    print(' '.join(command) + '    ' + kwargs.get('delimiter', ''))
    if kwargs.get('dryrun', False):
        return
    stdout = ''
    try:
        out = subprocess.check_output(command)
        stdout = out.decode()
    except subprocess.CalledProcessError:
        print('*** Command execution failed')
    if kwargs.get('print_output', True):
        print(stdout)
    return stdout
