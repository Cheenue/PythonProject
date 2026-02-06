# print("meow")
# print("meow")
# print("meow")

count = 0
while True:
    print(f"{count}. meow")
    count += 1
    if count > 49:
        break

print("*" * 50)

# this is cleaner
for count in range(50):
    print(f"{count}. meow")