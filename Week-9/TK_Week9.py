import matplotlib.pyplot as plt
from random import uniform

#Q1 Part A and Part B
def func_gradient_descent(theeta_0, dfx, learning_rate, no_iterations) :
	list_theetas = [None]*no_iterations
	list_theetas[0] = theeta_0
	
	for index in range(1,no_iterations):
		# FORMULA : Theeta(i) = Theeta(i-1) - (alpha * dfx(theeta(i-1)))
		list_theetas[index] = list_theetas[index - 1] - (learning_rate * dfx(list_theetas[index-1]))	

	return list_theetas

	
fx = lambda x : (x*x) - 1		# x^2 - 1
dfx = lambda x : 2*x			# 2x
theeta_0 = uniform(-1,1)		# theetha_0 selected randomly b/w -1,1
no_iterations = 100				# Number of iterations = 100



for learning_rate in [1.0, 0.1, 0.01]:
	value = func_gradient_descent(theeta_0, dfx, learning_rate, no_iterations)
	
	#Plot Graph
	plt.plot(list(map(fx,value)))
	plt.title("For Learning Rate = "+str(learning_rate))
	plt.ylabel('f(x)')
	plt.xlabel('value')
	plt.show()



	

	 

