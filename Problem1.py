# Given ages as List of 10 integers
import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("ages before sorting ", ages)

# 1) Sorting the list using list.sort() method
ages.sort()
# print the sorted list
print("ages after sorting", ages)
# min and max after sorting
minimum, maximum = ages[0], ages[len(ages) - 1]
# another way of doing this
minimum = min(ages)
maximum = max(ages)
print("Minimum age is", minimum, "and Maximum age is", maximum)

# 2) Add min and max elements again to the list
ages.append(minimum)  # min
ages.append(maximum)  # max
print("New list after appending min and max elements", ages)  # print new list

# 3) Find the median from the list -
# Based on even and odd number of elements in list, the median is calculated using if else block
length = len(ages)
if length % 2 == 0:
    median = (ages[length // 2] + ages[(length // 2) - 1]) / 2
else:
    median = (ages[length // 2])
# another way of doing this
median = statistics.median(ages)
print("median of the list is ", median)

# 4)Average age
average_age = sum(ages) / length
print("Average age is", average_age)

# 5)Range of ages
Range = maximum - minimum
print("Range of ages is", Range)
