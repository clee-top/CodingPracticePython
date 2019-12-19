# Read this https://docs.python.org/3/howto/sorting.html
# Sort examples, from above link. For my own silly testing.
from operator import itemgetter, attrgetter

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# sorted_list = sorted(student_tuples, key=lambda student: student[2])
sorted_list = sorted(student_tuples, key=itemgetter(2))

print("Sorted with tuples: " + str(sorted_list))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [Student('john', 'A', 15), Student('jane', 'B', 12), Student('dave', 'B', 10)]
# object_sorted_list = sorted(student_objects, key=lambda student: student.age)
object_sorted_list = sorted(student_objects, key=attrgetter('age'))

print("Sorting objects: " + str(object_sorted_list))

# multi_sorted = sorted(student_tuples, key=itemgetter(1,2))
multi_sorted = sorted(student_objects, key=attrgetter('age', 'grade'))

print("Multiple sorts looks like this: " + str(multi_sorted))