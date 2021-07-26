from operator import itemgetter

fn = input("Enter student filename: ")
f = open(fn,'r')
scale = f.readline()
scale = scale.split(',')
a_min = int(scale[1])
b_min = int(scale[3])
c_min = int(scale[5])
d_min = int(scale[7])
students = []
for line in f:
   student = line.split(',')
   print(type(student), student)
   for i in range(1,len(student)):
      student[i] = int(student[i])
   students.append(student)

print(a_min, b_min, c_min, d_min)

students_out = []     # [[name,ave,let_grade],[name,ave,let_grade]]
for s in students:
   s_out = []         # [name,ave,let_grade]
   s_out.append(s[0]) # add name to s_out
   sum_grades = 0
   for i in range(1, len(s)):
      sum_grades = sum_grades + s[i]
   ave = sum_grades / (len(s) - 1)
   ave = round(ave, 2) # Convert ave to have 2 decimal places
   s_out.append(ave)   # add ave to s_out
   let_grade = 'F'
   if ave >= a_min:
      let_grade = 'A'
   elif ave >= b_min:
      let_grade = 'B'
   elif ave >= c_min:
      let_grade = 'C'
   elif ave >= d_min:
      let_grade = 'D'
   s_out.append(let_grade) # add letter grade to s_out
   students_out.append(s_out) # add s_out to students_out
   #students_out.sort(key=lambda x: x[1], reverse=True)
   students_out = sorted(students_out, key=itemgetter(1), reverse=True)

for o in students_out:
   print(o)


