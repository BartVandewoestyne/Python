# Program to calculate laptimes for running races.

import datetime

def to_seconds(h, m, s):
    return h*3600.0 + m*60.0 + s;

def to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return h, m, s

def calculate_laptimes(h, m, s):

    total_seconds = to_seconds(h, m, s)
    print("total time = {0:f} seconds").format(total_seconds)

    full_distance = 21097.5
    frac1 = 1076.0/full_distance
    frac2 = (1076.0+1*5005)/full_distance
    frac3 = (1076.0+2*5005)/full_distance
    frac4 = (1076.0+3*5005)/full_distance
    frac5 = (1076.0+4*5005)/full_distance

    lap1 = frac1*total_seconds
    lap2 = frac2*total_seconds
    lap3 = frac3*total_seconds
    lap4 = frac4*total_seconds
    lap5 = frac5*total_seconds

    h, m, s = to_hms(lap1)
    print "%d:%02d:%02d" % (h, m, s)
    h, m, s = to_hms(lap2)
    print "%d:%02d:%02d" % (h, m, s)
    h, m, s = to_hms(lap3)
    print "%d:%02d:%02d" % (h, m, s)
    h, m, s = to_hms(lap4)
    print "%d:%02d:%02d" % (h, m, s)
    h, m, s = to_hms(lap5)
    print "%d:%02d:%02d" % (h, m, s)

    print "%.2f km/h" % (21.0975/(h+m/60.0+s/3600))

if __name__ == "__main__":

    calculate_laptimes(1, 38, 37)
