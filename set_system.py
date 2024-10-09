import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class Particle():
	def __init__(self, m, pos, v):
		self.mass = m
		self.pos = pos
		self.vel = v
		#self.z = np.array([m, pos, v])

	def energy(self):
		self.kinetic = 0.5 * self.mass * np.dot(self.vel, self.vel)
		self.potential = 0
		self.total = self.kinetic + self.potential
		return self.total


class System():
	def __init__(self, part_num, dimension, field):
		self.particles = []
		for part in range(part_num):
			part_i = Particle(np.random.uniform(), np.random.uniform(0,dimension, 2), np.random.uniform(-5,5,2))
			self.particles.append(part_i)
		self.field = field
		self.max_x = dimension
		self.max_y = dimension
	
	def total_energy(self):
		self.total_energy = 0
		for ind_part in self.particles:
			ind_energy = ind_part.energy()
			self.total_energy += ind_energy
		return self.total_energy
			
x = System(2, 2, 1)
print(x.particles[0].pos,x.field, x.max_x)
print(x.total_energy())
		
			
		 
