from creator import School, Student
import json

with open("school.json",) as data:
    f = json.load(data)
    print(f['name'])
    while True:
        search = input('''
        **************************************
        **** who would you like to find? *****
        **************************************
        ''')
        if search == "Q":
            Print("***** thank you for using student finder *****")
            break
        if search in f['students']:
            student = f['students'][search]
            print(student['name'])  
            print(student['address'])
            print(student['email'])
            print(student['phone'])
            print(student['social'])
        else:
            print("that student is not here...")

