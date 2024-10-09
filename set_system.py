import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class Particle():
	def __init__(self, m, pos, v):
		self.mass = m
		self.pos = pos
		self.vel = v
		#self.z = np.array([m, pos, v])

	def interaction(self, other):
		pass


class System():
	def __init__(self, part_num, dimension, field):
		self.particles = []
		for part in range(part_num):
			part_i = Particle(np.random.uniform(), np.random.uniform(0,dimension, 2), np.random.uniform(-5,5,2))
			self.particles.append(part_i)
		self.field = field
		self.max_x = dimension
		self.max_y = dimension
x = System(2, 2, 1)
print(x.particles[0].pos,x.field, x.max_x)
		
			
		 
