import numpy

scores = [25, 45, 12, 78, 56, 34, 90, 67, 23, 41,
          55, 72, 38, 61, 29, 84, 49, 15, 70, 52]

q1 = numpy.quantile(scores, 0.25)
q2 = numpy.quantile(scores, 0.50)
q3 = numpy.quantile(scores, 0.75)

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)