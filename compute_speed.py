# Program to calculate laptimes for running races.

import datetime

def compute_speed(distance_in_meters, h, m, s):
    distance_in_km = distance_in_meters/1000.0
    total_time_in_hours = h + m/60.0 + s/3600.0
    return distance_in_km / total_time_in_hours
    
if __name__ == "__main__":

    speed_in_km_h = compute_speed(21097.5, 1, 57, 27.485)
    print "%.2f km/h" % speed_in_km_h
