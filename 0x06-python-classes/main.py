#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

my_square_5 = Square(3, (3, 0, 1))
my_square_5.my_print()

my_square_6 = Square(3, ['H', 0])
my_square_6.my_print()
print("--")
