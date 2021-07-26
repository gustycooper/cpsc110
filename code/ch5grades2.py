grades = [88, 79, 62, 95, 82]
highest = lowest = grades[0]
gradessum = 0
for index in range(len(grades)):
    gradessum = gradessum + grades[index]
    if grades[index] > highest:
        highest = grades[index]
    if grades[index] < lowest:
        lowest = grades[index]
    index = index + 1
print('Ave: ', gradessum / len(grades),
      'High:', highest,
      'Low: ', lowest)
