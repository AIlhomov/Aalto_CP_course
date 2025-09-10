n = int(input())
a = list(map(int, input().split()))

from math import sqrt
import itertools

def average_distance(Point2D):
  Point2D = list(Point2D)
  distances=[]
  if len(Point2D) < 2:
        raise ValueError
  for i in range(len(Point2D)) :
    for y in range(len(Point2D)):
  #   print (Point2D[i][0], Point2D[y][0])
      print (Point2D[i][1], Point2D[y][1])

      x1, x2 = Point2D[i][0], Point2D[y][0]
      y1, y2 = Point2D[i][1], Point2D[y][1]

      #print (x1, x2, y1,y2)
      
      mydistance = (sqrt((x2-x1)**2 + (y2-y1)**2))
      round(mydistance)
      if mydistance !=0:
        distances.append(mydistance)

  return round(sum(distances)/len(distances),4)

all_combinations = list(itertools.combinations(a, 2))
#print(all_combinations)
print(average_distance(all_combinations))