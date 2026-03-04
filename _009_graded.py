student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
}

for x in student_scores:
    if student_scores[x] <= 70:
        student_grades[x] = "Fail" 
    elif student_scores[x] <= 80:
        student_grades[x] = "Acceptable" 
    elif student_scores[x] <= 90:
        student_grades[x] = "Exceeds Expectations"
    else:
        student_grades[x] = "Outstanding"  

print(student_grades)