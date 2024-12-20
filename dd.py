"""
Name:Abe Weber
Date:12/20/24
Description:
"""
import math
def slope(point1:tuple,point2:tuple)->float:
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    slope = (y2-y1)/(x2-x1)
    return slope



def distance(point1:tuple, point2:tuple)->float:

    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

def main():
    point1 = (3,4)
    point2 = (-8, 12)
    print(slope(point1,point2))
    print(distance(point1,point2))

if __name__ == "__main__":
    main()