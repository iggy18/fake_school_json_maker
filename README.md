# this was a study in several things

- I wanted to learn how to use faker for an upcomming project where I will be making a school system. 

- I was able to create a demo school and fill it with students that have unique information.

- secondly I wanted to work with python IO a bit more and actually save the work to a file that another program would then open and use.

- I stored the result of the make_fake_school method in a dictionary and then serialized the dictionary. this creates a json file named "school.json". 

- to use this program you must run the creator.py file.
`python creator.py`

- create a school object
`schoolnamevariable = School("School Name")`

- then add student objects to the school object's dictionary
`schoolnamevariable.make_fake_school(int_number_of_desired_students)`

- this will output a "school.json" file.

- the organizer.py file will open the "school.json" file and allow a user to search for a student. if the student is enrolled in that school the students personal and contact information is printed to the console. else the user is informed that the student is not at the school

- to search you must run the organizer.py file.
`python organizer.py`

- you will by asked "who would you like to find?". type in the name of the student and the input will be used as the key.

- you can escape the program by typing "Q" into the console and pressing enter.
`Q`
