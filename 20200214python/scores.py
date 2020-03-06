class Student:
  def __init__(self, name, math, eng, chi, bio):
    self.name = name
    self.math = math
    self.eng = eng
    self.chi = chi
    self.bio = bio
  def info(self):
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
    return fmt.format(self.name, self.math, self.eng, self.chi, self.bio)
  def total(self):
    return self.math + self.eng + self.chi + self.bio

def select_math_larger_equal(sts, score):
  chosen = []
  for st in sts:
    if st.math >= score:
      chosen.append(st)
  return chosen

def select_chinese_less(sts, score):
  chosen = []
  for st in sts:
    if st.chi < score:
      chosen.append(st)
  return chosen

def select_biology_higher_avg(sts):
  avg = sum([st.bio for st in sts]) / len(sts)
  chosen  = []
  for st in sts:
    if st.bio > avg:
      chosen.append(st)
  return chosen

def select_english_lowest(sts):
  lowest = sts[0]
  for st in sts:
    if st.eng < lowest.eng:
      lowest = st
  return lowest

def select_avg_highest(sts):
  highest = sts[0]
  for st in sts:
    if st.total() > highest.total():
      highest = st
  return highest

def pr_sts(sts):
  for st in sts:
    print(st.info())

def read_scores():
  sts = []
  with open('scores.txt') as f1:
    first = f1.readline()
    #print(first)
    for line in f1:
      ts = line.strip().split()
      st = Student(ts[0], int(ts[1]), int(ts[2]), int(ts[3]), int(ts[4]))
      #print(st.info())
      sts.append(st)
  print(len(sts))

  lst1 = select_math_larger_equal(sts, 80)
  pr_sts(lst1)
  print('-' * 50)
  lst2 = select_chinese_less(sts, 80)
  pr_sts(lst2)
  print('-' * 50)
  lst3 = select_biology_higher_avg(sts)
  pr_sts(lst3)
  print('-' * 50)
  lowest = select_english_lowest(sts)
  print(lowest.info())
  print('-' * 50)
  highest = select_avg_highest(sts)
  print(highest.info())

read_scores()