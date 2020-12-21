# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 2

#netacad email cth: 'abcd@gmail.com'
email='abcd@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded

def isPointInCircle(x,y,r,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  points = (x - center[0])**2 + (y - center[1])**2
  z = r**2
  if points <= z:    
        isPointInCircle = True
  else:
    isPointInCircle = False
  return isPointInCircle
  
 
#Graded
import random

def generateRandomSquarePoints(n,length,center=(0,0)):
  # MULAI KODEMU DI SINI
  minx = center[0]-length/2
  miny = center[1]-length/2
  maxx = center[0]+length/2
  maxy = center[1]+length/2  
  
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  points = [[random.uniform(minx, maxx), random.uniform(miny, maxy)]for i in range(n)] 
  
  return points
  
 
#Graded

def MCCircleArea(r,n=100,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass
  length = r*2  
  points = generateRandomSquarePoints(n,length,center=(center[0],center[1]))
  InCircle = [isPointInCircle(x,y,r,center=(center[0],center[1])) for x, y in points]
  SumInCircle = InCircle.count(True) 
  LuasPersegi = length*length
  LuasLingkaran = (SumInCircle/n)*LuasPersegi  
  return LuasLingkaran
  
#Graded

def LLNPiMC(nsim,nsample):
  # MULAI KODEMU DI SINI
  pass
  Pi = [MCCircleArea(1,nsample) for i in range (nsim)]
  estpi = sum(Pi)/len(Pi)
  return estpi  

  
# Graded

def relativeError(act,est):
  
  # MULAI KODEMU DI SINI
  pass
  E = abs((est - act)/act) * 100
  return E 