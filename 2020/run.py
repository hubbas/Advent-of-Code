import os
import sys
import hashlib
import tempfile
import argparse
import itertools
import subprocess

replace_str = r"""
{perf}

@performance
def func():
{code}

func()
"""

def run(py_scripts):
	with tempfile.TemporaryDirectory() as tempdir:
		for py_script in py_scripts:
			print(f'Running {py_script}')
			
			temp_script_name = hashlib.md5(py_script.encode('utf-8')).hexdigest()
			temp_script_path = os.path.join(tempdir, f'{temp_script_name}.py')
			
			with open('perf.py') as f:
				perf_file_contents = f.read()
			with open(py_script) as f:
				code_file_contents = ''.join(['\t' + line for line in f.readlines()])
			with open(temp_script_path, 'w+') as f:
				contents = replace_str.format(perf=perf_file_contents, code=code_file_contents)
				f.write(contents)
			
			if subprocess.call(['python', temp_script_path], cwd=os.path.dirname(py_script)) != 0:
				return 1
			
			print()
	return 0

def parse_days(args):
	return [os.path.abspath(os.path.join(day, f'{part}.py'))\
			for day, part in itertools.product(
				[f'day{i}' for i in set(args.days)],
				[f'part{i}' for i in set(args.parts)])]

def main():
	parser = argparse.ArgumentParser(description='Advent of Code 2020')
	parser.add_argument('-days', '-d', nargs='+', type=int, choices=range(1, 9), default=list(range(1, 9)), help='Specify which day(s) to run')
	parser.add_argument('-parts', '-p', nargs='+', type=int, choices=range(1, 3), default=[1, 2], help='Specify which part(s) to run')
	return run(parse_days(parser.parse_args()))

if __name__ == '__main__':
	sys.exit(main())
