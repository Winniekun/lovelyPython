"""
@time : 2019/8/28下午7:29
@Author: kongwiki
@File: testThread.py
@Email: kongwiki@163.com
"""
import threading

"""
验证GIL的影响，评估多线程应用的性能
"""


class threads_object(threading.Thread):
	def run(self):
		function_to_run()


class nothreads_object(object):
	def run(self):
		function_to_run()


def non_threaded(num_iter):
	funcs = []
	for i in range(int(num_iter)):
		funcs.append(nothreads_object())
	for i in funcs:
		i.run()


def threaded(num_threads):
	funcs = []
	for i in range(int(num_threads)):
		funcs.append(threads_object())
	for i in funcs:
		i.start()
	for i in funcs:
		i.join()


def function_to_run():
	pass


def show_results(funcname, results):
	print("%-23s %4.6f seconds" % (funcname, results))


if __name__ == '__main__':
	import sys
	from timeit import Timer

	repeat = 100
	number = 1
	num_threads = [1, 2, 4, 8]
	print('Starting tests')
	for i in num_threads:
		t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
		best_result = min(t.repeat(repeat=repeat, number=number))
		show_results("non_threaded (%s iters)" % i, best_result)
		t = Timer("threaded(%s)" % i, "from __main__ import threaded")
		best_result = min(t.repeat(repeat=repeat, number=number))
		show_results("threaded (%s threads)" % i, best_result)
		print('Iterations complete')
