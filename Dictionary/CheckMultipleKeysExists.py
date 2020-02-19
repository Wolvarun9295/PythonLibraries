student = {
    'Name': 'Varun',
    'Class': 'D',
    'RollNo': '2'
}
print(student.keys() >= {'Class', 'Name'})
print(student.keys() >= {'Name', 'Varun'})
print(student.keys() >= {'RollNo', 'Name'})
