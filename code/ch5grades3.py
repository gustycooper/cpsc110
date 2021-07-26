grades = [88, 79, 62, 95, 82]
highest = lowest = grades[0]
gradessum = 0
for grade in grades:
    gradessum = gradessum + grade
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade
print('Ave: ', gradessum / len(grades),
      'High:', highest,
      'Low: ', lowest)
