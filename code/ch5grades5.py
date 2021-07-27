infile = open("ch5grades.txt", "r")
grades = []
for line in infile:
    grades.append(int(line))
infile.close()
gradessum = 0
highest = lowest = int(grades[0])
for grade in grades:
    gradessum = gradessum + grade
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade
print('Ave: ', gradessum / len(grades),
      'High:', highest,
      'Low: ', lowest)
    
