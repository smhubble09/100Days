with open("Day26/file1.txt") as numbers:
    file1 = numbers.readlines()

with open("Day26/file2.txt") as numbers:
    file2 = numbers.readlines()

result = [int(num) for num in file1 if num in file2]

# Write your code above 👆

print(result)