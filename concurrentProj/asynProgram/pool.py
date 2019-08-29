"""
@time : 2019/8/29上午11:34
@Author: kongwiki
@File: pool.py
@Email: kongwiki@163.com
"""
import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
	result_item = count(x)
	return result_item


def count(number):
	for i in range(0, 10000000):
		i += 1
	return i*number


if __name__ == '__main__':
	# 顺序执行
	start_time = time.time()
	for item in number_list:
		print(evaluate_item(item))
	print("Sequential execution in " + str(time.time() - start_time), "seconds")
	# 线程池执行
	start_time = time.time()
	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		futures = [executor.submit(evaluate_item, item) for item in number_list]
		for future in concurrent.futures.as_completed(futures):
			print(future.result())
	print("Thread pool execution in " + str(time.time() - start_time), "seconds")

	# 进程池执行
	start_time = time.time()
	with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
		futures = [executor.submit(evaluate_item, item) for item in number_list]
		for future in concurrent.futures.as_completed(futures):
			print(future.result())
	print("Process pool execution in " + str(time.time() - start_time), "seconds")