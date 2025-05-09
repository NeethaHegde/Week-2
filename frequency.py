numbers = [1, 2, 2, 3, 3, 3, 4]

most_common = None
max_count = 0

for num in numbers:
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        most_common = num

print("Most frequent number is:", most_common)
