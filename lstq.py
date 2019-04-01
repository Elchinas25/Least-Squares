import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt

#x = [1.47, 1.5, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.7, 1.73, 1.75, 1.78, 1.80, 1.83]
#y = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]


def find_lstq(x, y):
	x = np.array(x)
	y = np.array(y)
	n = np.size(x)
	n2 = np.size(y)

	if n != n2:
		raise "Error, lengths not equal"

	s1 = np.sum( np.multiply(x, y) )
	s2 = np.sum( np.power(x, 2) )
	s3 = np.sum( x )
	s4 = np.sum( y )
	s5 = np.sum( np.power(y, 2) )

	L1 = np.polyfit(x, y, 1, full = True)

	m = L1[0][0]
	b = L1[0][1]
	least_squares = L1[1][0] #Sum of y errors squared

	n_inv = 1/n 
	s4sqrd = np.power(s4, 2)
	msqrd = np.power(m, 2)
	s3sqrd = np.power(s3, 2)

	sr2 = ( 1 / (n - 2) )*( s5 -n_inv*s4sqrd -msqrd*(s2 - n_inv*s3sqrd) )

	pre_m_error = ( n*sr2 )/( n*s2 - s3sqrd )
	m_error = np.sqrt(pre_m_error)

	pre_b_error = ( s2*sr2 )/( n*s2 - s3sqrd )
	b_error = np.sqrt(pre_b_error)

	#print("sr2 = {}".format(sr2))
	# print("Slope = {}".format(m))
	# print("b = {}".format(b))
	# print("Error in slope = {}".format(m_error))
	# print("Error in b = {}".format(b_error))
	# print("Least squares = {}".format(least_squares))



	return (m, b, m_error, b_error, least_squares)

tupl = find_lstq(x, y)
print(tupl)
