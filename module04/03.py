# We have a list of students' indicators in the group – this is a list with the test scores received.
# It is necessary to divide the list into two parts. Write a split_list function that takes a list (integers),
# finds the average of the score in the list, and divides it into two lists. The first one includes values less than the average,
# including the average, while the second one is strictly higher than the average. 
# The function returns a tuple of these two lists. For an empty list, return two empty lists.


def split_list(grade):
    if len(grade) == 0:
        return [], []
    less_than_average = []
    greater_than_average = []
    average = sum(grade) / len(grade)
    
    for student_grade in grade:
        if student_grade <= average:
            less_than_average.append(student_grade)
        else:
            greater_than_average.append(student_grade)
    return less_than_average, greater_than_average

student_grade = [70, 80, 90, 60, 75]


            
            
            
    