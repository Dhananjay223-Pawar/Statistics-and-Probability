import numpy

delivery_times = [32, 28, 29, 45, 30, 31, 60, 30, 29,
                  35, 40, 27, 33, 38, 42, 31, 36, 34, 29, 50]

p25 = numpy.percentile(delivery_times, 25)
p50 = numpy.percentile(delivery_times, 50)
p75 = numpy.percentile(delivery_times, 75)

print("25th Percentile:", p25)
print("50th Percentile:", p50)
print("75th Percentile:", p75)