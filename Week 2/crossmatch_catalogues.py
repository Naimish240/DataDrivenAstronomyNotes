# Write your crossmatch function here.
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

def angular_dist(r1, d1, r2, d2):
  r1, r2, d1, d2 = np.radians([r1, r2, d1, d2])
  a = np.sin(np.abs(d1-d2)/2) ** 2
  b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1-r2)/2) ** 2
  d = 2 * np.arcsin(np.sqrt(a+b))
  return np.degrees(d)

def crossmatch(cat1, cat2, max_radius):
    matches = []
    no_matches = []
    for id1, ra1, dec1 in cat1:
        closest_dist = np.inf
        closest_id2 = None
        for id2, ra2, dec2 in cat2:
            dist = angular_dist(ra1, dec1, ra2, dec2)
            if dist < closest_dist:
                closest_id2 = id2
                closest_dist = dist
        if closest_dist > max_radius:
            no_matches.append(id1)
        else:
            matches.append((id1, closest_id2, closest_dist))

    return matches, no_matches

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  #matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  #print(matches[:3])
  #print(no_matches[:3])
  #print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  #print(matches[:])
  #print(no_matches[:3])
  print(len(no_matches))
