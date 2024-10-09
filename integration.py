import numpy as np
import scipy as sp

def rk4(f, t, h, z, args = ()):
	"""
	fourth order Runga Kutta method
	inputs:
		function of dz/dt = f()
		t: time
		z: position and vecolity vecs concat
		h: timestep
	returns:
		z_new = z(t+h)
	"""
	
	if not isinstance(args, tuple):
		args = (args,)
	k1 = f(t,z, args,)
	k2 = f(t + 0.5 * h, z + 0.5 * h * k1, *args)
	k3 = f(t + 0.5 * h, z + 0.5 * h * k2, *args)
	k4 = f(t + h, z + h * k3, *args)
	return z + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
	
