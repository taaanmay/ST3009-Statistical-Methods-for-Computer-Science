import matplotlib.pyplot as plt
from random import uniform

#Q1 Part C and Part D
def func_random_point(start_point, fx, no_iterations, max_step_distance, max_num_tries) :
	vals = [None]*no_iterations
	vals[0] = start_point
	lowest_x = None

	for index in range(1,no_iterations):
		lowest_x = vals[index - 1]
		current_x = lowest_x
		num_tries = 0

		while num_tries < max_num_tries and fx(current_x) >= fx(lowest_x) :
			num_tries = num_tries + 1
			# FORMULA : Current_x = Current X + Random(Max Step, (- Max Step) )
			current_x = uniform(max_step_distance ,(-max_step_distance)) + current_x

		# Check if fx(New) is less than fx(lowest)
		if fx(current_x) < fx(lowest_x):
			lowest_x = current_x
		
		vals[index] = lowest_x

	return vals

	
fx = lambda x : (x*x) - 1		# x^2 - 1
dfx = lambda x : 2*x			# 2x
start_point = uniform(-1,1)		# start_point selected randomly b/w -1,1
no_iterations = 100				# Number of iterations = 100

max_step_distance = 0.1			# Maximum change in value of x
max_num_tries = 50				# Maximum number of tries to change value of x


value = func_random_point(start_point, fx, no_iterations, max_step_distance, max_num_tries)
	
#Plot Graph
plt.plot(list(map(fx,value)))
plt.title("Random Point")
plt.ylabel('f(x)')
plt.xlabel('value')
plt.show()
