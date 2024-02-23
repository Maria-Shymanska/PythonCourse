"""
Write a formatted_grades function that takes as input a dictionary of student grading for a subject of the following form:
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
And returns a list of formatted strings so that when the following code is output:

for el in formatted_grades(students):
    print(el)
The following table was obtained:

1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  | 

First column - 4 characters wide, right-aligned
second column is 10 characters wide, left-aligned
third and fourth columns are 5 characters wide, centered
Vertical Symbol | is not included in the width of the column
"""

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    result = []
    count = 1
    for name, grade in students.items():
        number_grade = grades.get(grade)
        result.append(
            "{:>4}|{:<10}|{:^5}|{:^5}".format(count, name, grade, number_grade)
        )
        count += 1
        return result

    for row in formatted_grades({"Nick": "A", "Olga": "B", "Boris": "FX", "Anna": "C"}):

        print(row)
