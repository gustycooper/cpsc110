infile = open("ch5grades.txt", "r")
grades = []
while True:
    line = infile.readline()
    if line == '':
        break
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
