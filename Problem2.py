# 1.create an empty dictionary dog
dog = {}
# 2.Add name,color,breed,legs and age to dog dictionary
dog.update({
    'name': 'Hachi',
    'color': 'brown',
    'breed': 'Akita',
    'legs': '4',
    'age': '11'
})
print("dog dictionary \n", dog)
print("dog is of", type(dog), "type")

# 3.create student dictionary with given keys
student = {
    'first_name': 'Shraddhasree',
    'last_name': 'Nangunoori',
    'gender': 'Female',
    'age': '25',
    'marital status': 'Unmarried',
    'skills': ["C#", "Java", "Python"],
    'country': 'India',
    'city': 'Hyderabad',
    'address': 'Happy Homes, Apt 503, Hyd - 500076'
}
print("Student dictionary \n", student)
# 4.length of student dictionary
print("Length of student dictionary is", len(student))

# 5.Get the value of skills and check the data type
print("skills value of", student['first_name'], "are ", student['skills'])
print("datatype of 'skills' in student dictionary is", type(student['skills']))

# 6.Modifying the skills key in student dictionary
student['skills'].extend(["Microsoft Azure", "Javascript"])
print("Modified skills of", student['first_name'], "are ", student['skills'])

# 7.Get the dictionary keys as a list;
print("Keys in student dictionary are :  \n", list(student.keys()))

# 8.Get the dictionary values as a list
print("values of student dictionary are : \n", list(student.values()))
