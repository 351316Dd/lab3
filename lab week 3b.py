#NAMES

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
class MyClass():
    def __init__(self, a, b):
        self.a = 10
        self.b = 20
        self.x = a + b
my_instance = MyClass(10,20)
my_instance.x

#2
class MyClass():
    def __init__():
        a = 10
        b = 20
        x = a + b
my_instance = MyClass()

my_instance.a
my_instance.b
my_instance.x

#without entering the first postional argument (a pointer to instance),
# the class is static

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x
#missing the pointer to instance


#4 Create a class to hold all of the courses a student at Harris is enrolled in.
#  - The instance should take two arguments when created; student name, 
#    and student year
#  - At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  - Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  - When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  - Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.

#define argument 
#ppha1234

class HarrisCohort ():
    def __init__ (self, name, year):
        self.name = name
        self.year = year
    def enroll (self):
        enrolled_courses = []
        name_mod = enrolled_courses.append(name)
        year_mod = enrolled_courses.append(year)
        
#attempt 2
    def __init__ (self, name, year): 
        self.name = name
        self.year = year 
        self.enrolled_courses = [] 
    def enroll (self, code, time):
        bundle = (name, year, code, time)
        self.enrolled_courses.append(bundle)

cohort1 = HarrisCohort('David', 2000)
cohort1.enroll ('ppha1234', '9:00')
print(cohort1.enrolled_courses)

#attempt 3
class HarrisCohort:
    def __init__ (self, name, year): 
        self.name = name
        self.year = year 
        self.enrolled_courses = [] 
    def enroll (self, code, time):
        bundle = (code, time)
        self.enrolled_courses.append(bundle)

cohort1 = HarrisCohort('David', 2000)
cohort1.enroll ('ppha1234', '9:00')
print(cohort1.enrolled_courses)