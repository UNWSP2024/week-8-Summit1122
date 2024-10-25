# Program #5: Course Info
# Luis Amador
# 10/22/24
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.


def new_course_adder():
    loops = 'true'
    course_info = ''
    while loops == 'true':
        course_id = input("What is the course ID? (ex: COS 2005): ")
        course_name = input("What is the name of the course?: ")
        entry = course_id + course_name
        course_info = course_info + entry
        ques = input("Would you like to add another course? y or n: ")
        if ques == 'y':
            loops = 'true'
        else:
            loops = 'false'


def main():
    new_course_adder()
    list = ''
    subject = input("What subject list would you like to see? (ex: COS): ")
    for string in course_info:
        if subject in string:
            list = list + string

main()