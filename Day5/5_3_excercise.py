total = 0
for x in range(1, 101):
    if x % 2 == 0:
        total += x

print(f"The total of even numbers is {total}")

total2 = 0
for x in range(2, 101,2):
    total2 += x

print(f"The total of even numbers is {total2}")