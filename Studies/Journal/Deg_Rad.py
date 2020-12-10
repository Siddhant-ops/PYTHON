from math import pi


def con_to_rad(deg):
    temp = (deg * pi) / 180
    temp = format(temp, ".3f")
    print(temp)


def con_to_deg(rad):
    temp = (rad * 180) / pi
    temp = format(temp, ".3f")
    print(temp)
