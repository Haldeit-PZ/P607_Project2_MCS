import numpy as np
import scipy as sp


def rk4(f, t, h, z, args=()):
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
    k1 = f(
        t,
        z,
        args,
    )
    k2 = f(t + 0.5 * h, z + 0.5 * h * k1, *args)
    k3 = f(t + 0.5 * h, z + 0.5 * h * k2, *args)
    k4 = f(t + h, z + h * k3, *args)
    return z + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def integration_fun1(t, particle, max_x, max_y, field_strength, beam_width):
    """ """
    r = particle[0:2]
    v = particle[2:4]
    if r[0] > max_x:  # particle x exeeds +x limit
        v[0] = -v[0]
        r[0] = 2 * max_x - r[0]
    elif r[0] < 0:  # particle x less than zero
        v[0] = -v[0]
        r[0] = -r[0]
    if r[1] > max_y:  # particle y exceeds +y boundary
        v[1] = -v[1]
        r[1] = 2 * max_y - r[1]  # particle y less than zero
    elif r[1] < 0:
        v[1] = -v[1]
        r[1] = -r[1]

    if (r[1] < max_y / 2 + beam_width) and (r[1] > max_y / 2 - beam_width):
        dvdt = np.array([field_strength, 0])
    else:
        dvdt = np.array([0, 0])

    drdt = v
    dzdt = np.concatenate((drdt, dvdt))
    return dzdt
