#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

class student:
    import random

    class Student:
        def __init__(self, name, student_id, year, major, gpa):
            self.name = name
            self.student_id = student_id
            self.year = year
            self.major = major
            self.gpa = gpa
        def is_eligible_for_honors(self):
            if self.gpa > 3.5:
                print(f"{self.name} eligible for the honors program")
                return True
            else:
                print(f"{self.name} not eligible for the honors program.")
                return False
        def check_free_lunch(self, random_id):
            if random_id == self.student_id:
                print(f"Winner! {self.name} gets free lunch today")
            else:
                print("Loser")


    Bryce = Student("Bryce Lazarto", 12345, "Freshman", "Computer Science", 3.4)
    Bryce.is_eligible_for_honors()
    random_id = random.randint(1000, 9999)
    Bryce.check_free_lunch(random_id)

    
    
    
    
main():
