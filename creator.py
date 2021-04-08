from faker import Faker
import json

class Student:
    """ creates a student """
    def __init__(self, name, email, address, phone, social):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.social = social

    def __repr__(self):
        return f'Name: {self.name}\n\nEmail: {self.email} \n\nAddress: {self.address} \n\nPhone: {self.phone} \n\nSocial: {self.social} \n\n'

class School:
    """ creates a school """
    def __init__(self, name):
        """ makes a school with a dictionary for fast access """
        self.name = name
        self.students = dict()

    def new_student(self, name, email, address, phone, social):
        """ creates new student and adds it to school dictionary """
        student = Student(name, email, address, phone, social)
        self.students[student.name] = student

    def list_students(self):
        """ list out students in school dictionary """
        for kid in self.students:
            print(kid)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def make_fake_school(self, amount):
        """ generates multiple student objects with fake credentials and stores them as jason in a txtfile"""
        fake = Faker()
        for i in range(1, amount+1):
            name = fake.name()
            address = fake.address()
            phone = fake.numerify(text="(###)-###-####")
            social = fake.ssn()
            email = fake.email()
            self.new_student(name, email, address, phone, social)
        with open("school.json", "w") as f:
            f.write(self.toJSON())
