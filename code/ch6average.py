def avg(numbers):
   s = 0
   for n in numbers:
      s = s + n
   a = s / len(numbers)
   return a

def main():
   lst = [90, 95, 78,82]
   ave = avg(lst)
   print(avg([90, 95, 78, 82]), ave)

if __name__ == '__main__':
   main()
