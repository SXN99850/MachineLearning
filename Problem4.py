from ast import Delete
from ntpath import join
from random import Random, random

# Given input Sets and List
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("it_companies", it_companies)

# 1.Length of the set it_companies
print("Length of the set it_companies", len(it_companies))

# 2.Add twitter to it_companies
it_companies.add('twitter')
print("Added twitter to it_companies", it_companies)

# 3.Add multiple values at once to set it_companies
it_companies.update(('Infosys', 'Cognizant', 'Accenture', 'Travelers', 'DXC'))
print("updated companies\n", it_companies)

# 4,5.Remove one of the companies from it_companies and difference between remove and discard
# To remove a particular member, use remove() method - Will raise an error if member does not exist
it_companies.remove('Cognizant')
print("it_companies after removing\n", it_companies)
# To remove a specific member, use discard() method - Will not raise an error if member does not exist
it_companies.discard('Wipro')  # Does not throw an error
it_companies.discard('Infosys')
print("it_companies after discarding\n", it_companies)
# To remove a random member from set, use pop() method
it_companies.pop()
print("it_companies after popping\n", it_companies)

# 6.Join A and B
# method 1
# A |= B  # Adds all elements of SetB to SetA
# print("After joining A and B", A)
# method 2 - using union()
print("After joining A and B using union method", A.union(B))
# method 3 - using update()
# A.update(B)  # returns new updated set combining A and B
# print("After joining A and B using update method", A)

# 7. Find A intersection B
print("Intersection of A and B - ", A.intersection(B))

# 8.Is A subset of B
print("Is A subset of B", A.issubset(B))

# 9.Are A and B disjoint sets (Disjoint sets are those who don't have anything in common)
print("Are A and B disjoint sets?", A.isdisjoint(B))

# 10.Join A with B and B with A
print("Joining A with B", A.union(B))
print("Joining B with A", B.union(A))

# 11.What is the symmetric difference between A and B
# (Symmetric diff is the elements in both sets excluding intersection)
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B", symmetric_diff)

# 12.Delete the sets completely
A.clear()
B.clear()
print("A and B sets are  deleted completely")

# 13.Convert the ages to a set and compare the length of the list and the set.
length_age_list = len(age)
print("length of the list-age is", length_age_list)
print("Converting list age", age, "to a set", set(age))
length_age_set = len(set(age))
print("length of set-age", length_age_set)
# comparing the age list and age set
if length_age_list == length_age_set:
    print("Length of age as list-", length_age_list, "is equal to length of age as set-", length_age_set)
elif length_age_set < length_age_list:
    print("Length of age as set-", length_age_set, "is less than length of age as list-", length_age_list)
else:
    print("Length of age as list-", length_age_list, "is greater than length of age as set-",length_age_set)
