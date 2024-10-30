from math import pi

def radians(degree) :
    return pi/2*(degree/90.0)

if   __name__ == "__main__" :
    degree=90.0
    print(radians(degree))
    degree=180.0
    print(radians(degree))
