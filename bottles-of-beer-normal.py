# Origin Question:
# http://www.jianshu.com/p/6d33b4c31d5b
#Just the first algorthm implementation
#How many beer can we get finally given input a beer?
#4 caps can get one more beer
#2 bottles can get one more bear
#n for new beer
#b for existing bottle
#c for existing cap
#lb for left old bottle
#lc for left old cap
#nb for new beer from bottle
#nc for new beer from cap
#s for total beer we can get

def bottle_to_beer(b):
  return int(b/2),b%2
    
def cap_to_beer(c):
  return int(c/4),c%4
  
def total_beer(a):
  s = a
  b = a
  c = a
  lb = 0
  lc = 0
  nb = 1
  nc = 1
  
  while(nb!=0 or nc!=0):
    nb,lb = bottle_to_beer(b)
    s = s + nb
    b = lb + nb
    c = c + nb
    nc,lc = cap_to_beer(c)
    s = s + nc 
    b = b + nc
    c = lc + nc
  
  return s
  
print(total_beer(100))
print(total_beer(5)) 