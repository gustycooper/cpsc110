from operator import itemgetter

def get_scale(fn): # fn is filename
    f = open(fn,'r')
    scale = f.readline()
    f.close()
    scale = scale.split(',')
    scale_dict = {}
    A = scale[0]
    a_min = int(scale[1])
    scale_dict[A] = a_min
    B = scale[2]
    b_min = int(scale[3])
    scale_dict[B] = b_min
    C = scale[4]
    c_min = int(scale[5])
    scale_dict[C] = c_min
    D = scale[6]
    d_min = int(scale[7])
    scale_dict[D] = d_min
    return scale_dict

def get_students(fn): # fn is filename
    f = open(fn,'r')
    scale = f.readline() # consume scale line
    students = []
    for line in f:
       student = line.split(',')
       print(type(student), student)
       for i in range(1,len(student)):
          student[i] = int(student[i])
       students.append(student)
    f.close()
    return students

def process_students(students, scale):
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
       if ave >= scale['A']:
          let_grade = 'A'
       elif ave >= scale['B']:
          let_grade = 'B'
       elif ave >= scale['C']:
          let_grade = 'C'
       elif ave >= scale['D']:
          let_grade = 'D'
       s_out.append(let_grade) # add letter grade to s_out
       students_out.append(s_out) # add s_out to students_out
    students_out = sorted(students_out, key=itemgetter(1), reverse=True)
    return students_out

def main():
    fn = input("Enter student filename: ")
    scale = get_scale(fn) # scale['A'] returns a_min
    students_in = get_students(fn)
    students_out = process_students(students_in, scale)
    for o in students_out:
       print(o)

main()
