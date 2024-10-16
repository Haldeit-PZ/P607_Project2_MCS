import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import integration
import set_system

particle_num_list = np.arange(5,26,5)


monte_iterations = 100

list3 = []
for part in particle_num_list:
	list1 = []
	for i in range(monte_iterations):
		x = set_system.System(part,2,1,10,10,.1)
		x.iterate_over()
		x.make_total_energy_list()
		list1.append(x.total_energy_list)
		list2 = list1[0]
	for i in range(len(list1)):
		if i != 0:
			list2 = np.add(list2, list1[i])
	
	list3.append(list2)	
print(list3)
	
		
