contacts = {
    'number':4,
    'students':
    [
        {'name':'Sarah Holderness','email':'satah@example.com'},
        {'name':'Błażej Wliniski','email':"blazej@example.com"},
        {'name':'Michal Antoszczyszyn','email':'michal@example.com'},
        {'name':'Yasangi Rathnamali','email':'Yasangi@example.com'}
    ]
}

print("student emails:")
for student in contacts['students']:
    print(student['email'])