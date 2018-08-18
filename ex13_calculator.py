# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

from ex12_convert_seconds import convert_seconds

KILO_TO_U = 2**10
MEGA_TO_U = 2**20
GIGA_TO_U = 2**30
TERA_TO_U = 2**40
BYTE_TO_BIT = 8

def convert_to_bits_using_dict(s):
    FACTOR_SIZE = {
        'k': KILO_TO_U, 'm': MEGA_TO_U, 'g': GIGA_TO_U, 't': TERA_TO_U
    }
    factor = FACTOR_SIZE[s[0].lower()]
    quantity_bit = s[1]
    if quantity_bit == 'B':
        factor *= BYTE_TO_BIT 
    return factor

def convert_to_bits(s):
    factor = 0

    quantity = s[0].lower()
    quantity_bit = s[1]

    if quantity == 'k':
        factor = KILO_TO_U 
    if quantity == 'm':
        factor = MEGA_TO_U
    if quantity == 'g':
        factor = GIGA_TO_U
    if quantity == 't':
        factor = TERA_TO_U
    if quantity_bit == 'B':
        factor *= BYTE_TO_BIT 
    return factor  

def download_time(file_size, f_unit, bandwidth, bw_unit):
    size_bits = file_size * convert_to_bits(f_unit)
    bandwidth_bits = bandwidth * convert_to_bits(bw_unit)
    seconds = size_bits / bandwidth_bits
    return convert_seconds(seconds)


print(download_time(1024,'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print(download_time(1024,'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13,'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13,'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10,'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10,'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print(download_time(11,'GB', 5, 'MB'))
# >>> 0 hours, 37 minutes, 32.8 seconds

print(download_time(1,'kB',3,'MB'))
#>>>  0 hours, 0 minutes, 0.000325520833333 seconds

print(download_time(1,'TB', 100, 'Mb'))
#>>> 23 hours, 18 minutes, 6.08 seconds
