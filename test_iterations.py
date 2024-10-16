import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import integration
import set_system

particle_num_list = np.arange(5,26,5)
frames_num_list = np.arange(5,26,5)

monte_iterations = 100

for part in particle_num_list:
	for fra in frames_num_list:
		energy_diff_list = []
		
