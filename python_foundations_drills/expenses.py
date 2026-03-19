
expenses = [10.50, 8, 5, 15, 20, 5, 3]

#the easier way to go through a list
total = sum(expenses)

print('You spent $', total, sep = '')

'''the harder way to go through a list
sum = 0

for x in expenses:
    sum = sum + x

print('You spent $', sum, ' this week.', sep = "")
'''