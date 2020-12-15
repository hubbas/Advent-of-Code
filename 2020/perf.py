import time
import tracemalloc

def time_to_run(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f'Time to run: {end - start:.3f}s')
		return result
	return wrapper

def memory_allocated(func):
	def print_snapshot(snapshot, key_type='lineno'):
		snapshot = snapshot.filter_traces((
			tracemalloc.Filter(False, '<frozen importlib._bootstrap>'),
			tracemalloc.Filter(False, '<unknown>'),
		))
		top_stats = snapshot.statistics('lineno')
		total = sum(stat.size for stat in top_stats)
		print(f'Total allocated size: {total / 1024:.1f} KiB')

	def wrapper(*args, **kwargs):    
		tracemalloc.start()
		result = func(*args, **kwargs)
		snapshot = tracemalloc.take_snapshot()
		print_snapshot(snapshot)
		return result
	return wrapper

def performance(func):
	def wrapper(*args, **kwargs):
		f = memory_allocated(time_to_run(func))
		return f(*args, **kwargs)
	return wrapper
