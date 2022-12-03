#!/usr/bin/python3
def print_reveresd_list_integer(my_list=[]):
	if not my_list:
		pass
	else:
		for y in reversed(my_list):
			print("(:d\n".format(y), end='')
