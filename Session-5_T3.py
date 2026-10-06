import numpy

steps = [ 6500, 7200, 8000, 6000, 9000, 7500, 8200, 6800, 7100, 8500, 9200, 7800, 6900, 7400, 8100, 6300, 8800, 7600, 7000, 9500]

q1 = numpy.percentile(steps, 25)
q3 = numpy.percentile(steps, 75)

iqr = q3 - q1

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)