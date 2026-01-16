# X bottles of beer on the
# X bottles of beer.
# Take one down, pass it all around, Y  bottles of beer on the wall

# MY VERSION

num = 101

while num > 0:
    num_wall = num - 1
    print(f'{num} bottles of beer on the wall, ')
    print(f'{num} bottles of beer.')
    print(f'Take one down, pass it all around, {num_wall}  bottles of beer on the wall')
    print("*" * 8)
    num -= 1

# COLT'S VERSION

for bottles in range(100, 0, -1):
     num_wall = bottles - 1
     print(f'{bottles} bottles of beer on the wall, ')
     print(f'{bottles} bottles of beer.')
     print(f'Take one down, pass it all around, {num_wall}  bottles of beer on the wall')
     print("*" * 8)
