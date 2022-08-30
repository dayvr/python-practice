# Function that takes as its inputs the result ofa traceroute (in ms) and 
# distance (in km) between two points. It should return the speed the data 
# travels as a decimal fraction of the speed of light.

speed_of_light = 300000. # km per second

def speed_fraction(traceroute_result, distance):
    km_sec = (distance * 2) / (traceroute_result / 1000)
    fraction = km_sec / speed_of_light
    return fraction

print(speed_fraction(50,5000))
#>>> 0.666666666667

print(speed_fraction(50,10000))
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?
