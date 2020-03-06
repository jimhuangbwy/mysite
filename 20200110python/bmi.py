def computeBMI(h, w):
  h = h / 100
  return w / (h ** 2)

def getMemo(bmi):
  #體重過輕   BMI < 18.5
  #正常範圍   18.5 <= BMI < 22.9
  #過   重   22.9 <= BMI < 27
  #輕度肥胖   27 <= BMI < 30
  #中度肥胖   30 <= BMI < 35
  #重度肥胖   BMI >= 35
  if bmi < 18.5:
    return 'underweight'
  elif bmi < 22.9:
    return 'normal'
  elif bmi < 27:
    return 'overweight'
  elif bmi < 30:
    return 'obese 1'
  elif bmi < 35:
    return 'obese 2'
  else:
    return 'obese 3'

def table():
  with open('bmi.txt') as f:
    first = f.readline()
    hs = first.split()
    fmt = '{:>10}{:>10}{:>10}{:>10}{:>10}{:>14}'
    print(fmt.format(hs[0], hs[1], hs[2], hs[3], 'BMI', 'MEMO'))
    print('-' * 64)
    for line in f:
      tks = line.strip().split()
      name, gender, h, w = tks[0], tks[1], float(tks[2]), float(tks[3])
      bmi = round(computeBMI(h, w), 2)
      memo = getMemo(bmi)
      print(fmt.format(name, gender, h, w, bmi, memo))
      #print(type(name), type(gender), type(h), type(w))
table()