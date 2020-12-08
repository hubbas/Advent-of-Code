import os
import subprocess

dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
for d in dirs:
	print(f'Running {d}')
	abs_dir = os.path.abspath(d)
	for part in ('part1', 'part2'):
		print(f'{part}:', end=' ')
		script = os.path.join(abs_dir, f'{part}.py')
		subprocess.call(['python', script], cwd=abs_dir)
	print()
