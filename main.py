import numpy as numpy
import scipy as stats

marks_of_students=[90, 72, 82, 90, 69, 19, 23, 30, 45, 5]
my_mean = numpy.mean(marks_of_students)
print("the mean is: ", numpy.mean(marks_of_students))
my_median=numpy.median(marks_of_students)
print("the median is:", numpy.median(marks_of_students))
my_mode=stats.mode(marks_of_students)
print("the mode is:", stats.mode(marks_of_students))
my_range=numpy.ptp(marks_of_students)
print("the range is: ", numpy.ptp(marks_of_students))

