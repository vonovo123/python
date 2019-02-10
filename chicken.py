in_file = open('chicken.txt', 'r')
day_count = 0
total_sale = 0
for line in in_file:
    day_count += 1
    total_sale += int(line.strip().split(': ')[1])
print(total_sale / day_count)
