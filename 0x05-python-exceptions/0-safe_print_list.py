#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
	total = 0
	for i in len(my_list):
		try:
			print(f"{my_list[i]}", end= "")
			total += 1
		except IndexError:
			break
	print()
	return(total)
