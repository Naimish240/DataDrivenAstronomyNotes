# Write your find_closest function here
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

def angular_dist(r1, d1, r2, d2):
  r1, r2, d1, d2 = np.radians([r1, r2, d1, d2])
  a = np.sin(np.abs(d1-d2)/2) ** 2
  b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1-r2)/2) ** 2
  d = 2 * np.arcsin(np.sqrt(a+b))
  return np.degrees(d)

def find_closest(data, ra, dc):
  res = 500
  idx = -1
  for i in range(len(data)):
    row = data[i]
    dist = angular_dist(ra, dc, row[1], row[2])
    if dist < res:
      res = dist
      idx = i
  return idx+1, res



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))
