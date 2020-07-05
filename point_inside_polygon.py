import math
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def isInside(poly,p):
    n = len(poly)
    if n < 3 : return False
    if p in poly: return True
    total_angle = 0
    
    for i in range(n):
        j = (i+1)%n
        ang = getAngle(poly[i],p,poly[j])
        if  ang == 180:
            return True
        total_angle += ang
    if total_angle == 360:
        return True
    else: 
        return False
if __name__ == '__main__':
    if(isInside( [[1,0], [8,3], [8,8], [1,5]],[8,4])):
        print("Inside")
    else:
        print("Outside")