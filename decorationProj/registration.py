"""
@time : 2019/9/2下午4:33
@Author: kongwiki
@File: registration.py
@Email: kongwiki@163.com
"""
registry = []


def register(func):
	print("runnnig register(%s)" % func)
	registry.append(func)
	return func


@register
def f1():
	print("running f1()")


@register
def f2():
	print("running f2()")


def f3():
	print("running f3()")


def main():
	print("running main()")
	print("registry ->", registry)
	f1()
	f2()
	f3()


if __name__ == '__main__':
	main()
