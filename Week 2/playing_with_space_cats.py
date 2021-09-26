# Write your import_bss function here.
import numpy as np

def hms2dec(h, m, s):
  return 15 * (h+ m/60 + s/3600)

def dms2dec(d, m, s):
  if d > 0:
    return d + m/60 + s/3600
  return -1 * (-d + m/60 + s/3600)

def import_bss(file='bss.dat'):
  data = np.loadtxt(file, usecols=range(1,7))
  res = []
  for i in range(len(data)):
    row = data[i]
    ra = hms2dec(row[0], row[1], row[2])
    dc = dms2dec(row[3], row[4], row[5])
    res.append((i+1, ra, dc))
  return res

def import_super(file='super.csv'):
  data = np.loadtxt(file, delimiter=',', skiprows=1, usecols=[0,1])
  res = []
  for i in range(len(data)):
    row = data[i]
    res.append((i+1, row[0], row[1]))
  return res


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)