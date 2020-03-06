class Student:
  sid = 'unknown'
  name = 'unknown'
  gender = 'unknown'
  height = 0
  weight = 0
  def __init__(self, sid, name, gender):
    self.sid = sid
    self.name = name
    self.gender = gender
  def set_height(self, h):
    self.height = h
  def set_weight(self, w):
    self.weight = w
  def bmi(self):
    return self.weight / ((self.height / 100) ** 2)
  def info(self):
    return '{:10}{:10}{:10}{:10}{:10}{:10}'.format(self.sid, self.name, 
      self.gender, self.height, self.weight, round(self.bmi(), 2))

class BmiReport:
  name = 'unknown'
  sts = []
  def __init__(self, name):
    self.name = name
  def add_student(self, st):
    self.sts.append(st)
  def remove_student(self, sid):
    remove = None
    for st in self.sts:
      if st.sid == sid:
        remove = st
        break
    self.sts.remove(remove) 
  def save_file(self, filename):
    with open(filename, 'w') as f:
      f.write(self.name)
      f.write('\n')
      for st in self.sts:
        f.write(st.info())
        f.write('\n')
  def read_file(self, filename):
    with open(filename) as f:
      first = f.readline()
      self.name = first.strip()
      for line in f:
        ts = line.split(',')
        st = Student(ts[0], ts[1], ts[2])
        st.set_height(float(ts[3]))
        st.set_weight(float(ts[4]))
        #print(st.info())
        self.add_student(st)
  def print_report(self):
    print(self.name)
    for st in self.sts:
      print(st.info())

def test1():
  report = BmiReport("Class A")
  report.read_file("students.txt")
  report.save_file("result.txt")

def test2():
  report = BmiReport('')
  report.read_file('students.txt')
  report.print_report()

def test3():
  report = BmiReport("")
  report.read_file("students.txt")
  report.remove_student("A01")
  st = Student("A10", "Easter", "M")
  st.set_height(160)
  st.set_weight(65)
  report.add_student(st)
  report.save_file("result2.txt")

#test1()
#test2()
#test3()

def run_app():
  report = None
  print("BMI 管理系統 by Jimmy")
  while True:
    line = input('>')
    if line == 'exit': 
      break
    if line == 'help':
      print('可用命令： <...>必要參數  [...]可省略參數')
      print('blank <name>               -- 開始一個名為 <name> 班級')
      print('open <file>                -- 打開班級檔案')
      print('save [file]                -- 儲存檔案')
      print('import [file]              -- 匯入學生資料檔案')
      print('list [from [to]]           -- 列印學生')
      print('add <id> [name]            -- 加入學生')
      print('update <id> <field> <val>  -- 更改學生資料欄位')
      print('exit                       -- 離開')
    if line.startswith('blank'):
      tokens = line.split()
      report = BmiReport(tokens[1])
    if line.startswith('list'):
      report.print_report()
    if line.startswith('import'):
      tokens = line.split()
      if not report:
        report = BmiReport('dummy')
      report.read_file(tokens[1])
    if line.startswith('add'):
      tokens = line.split()
      st = Student(tokens[1], tokens[2], tokens[3])
      st.set_height(float(tokens[4]))
      st.set_weight(float(tokens[5]))
      report.add_student(st)
    if line.startswith('save'):
      tokens = line.split()
      report.save_file(tokens[1])

  print('Bye bye')

run_app()