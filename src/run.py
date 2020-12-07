import os
import subprocess

dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
for d in dirs:
	print(f'Running {d}')
	abs_dir = os.path.abspath(d)
	script = os.path.join(abs_dir, 'main.py')
	subprocess.call(['python', script], cwd=abs_dir)
	print()
