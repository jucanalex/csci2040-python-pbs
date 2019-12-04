

def area (polygon):
    x = 0
    y = 1

    ar = (polygon[0][x]*polygon[1][y] + polygon[1][x]*polygon[2][y] + polygon[2][x]*polygon[0][y] -
             polygon[1][x]*polygon[0][y] - polygon[2][x]*polygon[1][y] - polygon[0][x]*polygon[2][y]) / 2

    if len(polygon) == 3:
        return ar
    else:
        del polygon[1]
        return ar + area(polygon)

poly = [(0,20), (3,0), (10,10), (5,15), (3, 18)]


print (area(poly))