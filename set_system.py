import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import integration as igt

class Particle():
	def __init__(self, m, pos, v):
		"""
		Initialize particle mass, position, and velocity
		imputs:
			m: mass float/int
			pos: position 2D array x-y pos
			v: velocity 2D array x-y vel
		outputs:
			initialized particle object
		"""
			
		self.mass = m
		self.pos = pos
		self.vel = v
		self.z = np.concatenate((pos, v))  #array of positions and vel


	def energy(self):
		"""
		Compute kinetic potential and total energies for single particle
		inputs:
			particle object
		outputs: 
			energies
		"""
		self.kinetic = 0.5 * self.mass * np.dot(self.vel, self.vel)
		self.potential = 0
		self.total = self.kinetic + self.potential
		return self.total

	def integrate(self, f, t, h):
		"""Integrate step
		inputs:
			self: particle object
			f: integration function
			t: timepoint
			h: timestep
		outputs:
			updated pos, vel, concat array
		"""
		self.z = igt.rk4(f, t, h, self.z)
		self.pos = self.z[0:2]
		self.vel = self.z[2:4]

#------------------------------------------System-------------------------------------------#

class System():
	def __init__(self, part_num, dimension, field, max_mass, frames, step_size):	
		"""
		Initialize system with particels, beam, and box
		inputs:
			part_num: number of particles in box (int)
			dimension: x-y length of box (float)
			field: beam
			max_mass: largest particle mass
			frames: number of evolution, or iterations
			step_size: integration step size
		outputs:
			system of particles, beam, box
		"""
		self.particles = []
		for part in range(part_num):
			part_i = Particle(np.random.uniform(0, max_mass), np.random.uniform(0,dimension, 2), np.random.uniform(-dimension / 5, dimension / 5, 2)) # velocity can't be too fast
			self.particles.append(part_i)
		self.field = field
		self.max_x = dimension
		self.max_y = dimension
		self.max_mass = max_mass
		self.timeline = np.arange(0, frames + 1, 1)
		self.step_size = step_size
	
	def total_energy(self):
		"""
		Compute total energy of N-particles
		input:
			system obecjt
		outputs:
			total energy of N particles
		"""
		self.total_energy = 0
		for ind_part in self.particles:
			ind_energy = ind_part.energy()
			self.total_energy += ind_energy
		return self.total_energy

	def step(self):
		"""
		Update each particle velocity and position
		"""
		for particle in self.particles:
			for frame in self.timeline:
				particle.integrate(self.field, frame, self.step_size)
				# should also check boundary, if particle goes out, it should rebound by the same magnituce, and invert velocity

	def plot_system(self):
		"""
		Plot the system under ./figures
		"""
		for particle in self.particles:
			plt.plot(particle.pos[0], particle.pos[1],
				color = '#50c878', # emerald
				marker = ".",
				linestyle = "None",
				markersize = particle.mass,
				label = f"Particles")
		plt.title(f"Particles in a Square 2D Box")
		plt.xlabel(f"X Dimension")
		plt.ylabel(f"Y Dimension")
		plt.grid()
		plt.xlim(0, self.max_x)
		plt.ylim(0, self.max_y)
		plot_destination = "figures/system_plot.png"
		plt.savefig(plot_destination, dpi=500)
			
x = System(10, 2, 0, 10, 5, 1) # particles, boundary, field, max mass, frames, step size
print(f"")
print(f"[Vx Vy, X, Y of First Particle]: {x.particles[0].z}")
print(f"Field Strength: {x.field}")
print(f"Dimension Boundary: {x.max_x}")
print(f"Total Energy: {x.total_energy()}")
x.plot_system()
		
			
		 
