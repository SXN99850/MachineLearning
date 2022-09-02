# Create a tuple with names of sisters and brothers

# Brother tuple
brother_tuple = ("Aditya", "Nandu", "Vedu", "Aditya")
print("Brother tuple",brother_tuple)
# Sister tuple
sister_tuple = ("shruthi", "sneha", "medha")
print("Sister tuple",sister_tuple)

# Join brother and sister tuples and assign it to siblings
siblings = brother_tuple + sister_tuple
print("siblings tuple", siblings)

# Siblings count
print("No. of siblings", len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

# Tuples are immutable so modify the tuple by changing it to list
Family_members = list(siblings)
Family_members.extend(["Ram", "Lalitha"])
# Convert back list to tuple
family_members = tuple(Family_members)
print("Extended family with Father, Mother and Siblings", family_members)
