import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from integration import integration_fun1
import imageio, os
from natsort import natsorted


class Particle:
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
        self.z = np.concatenate((pos, v))  # array of positions and velj
        self.z_list = []
        self.e_list = []

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

    def make_energy_list(self):
        for zs in range(len(self.z_list.t)):
            kin = (
                0.5
                * self.mass
                * (self.z_list.y[2][zs] ** 2 + self.z_list.y[3][zs] ** 2)
            )
            pot = 0
            tot = kin + pot
            self.e_list.append(tot)


# ------------------------------------------System-------------------------------------------#


class System:
    def __init__(
        self, part_num, dimension, field_strength, max_mass, frames, step_size
    ):
        """
        Initialize system with particels, beam, and box
        inputs:
                part_num: number of particles in box (int)
                dimension: x-y length of box (float)
                field_strength: beam strength
                max_mass: largest particle mass
                frames: number of evolution, or iterations
                step_size: integration step size
        outputs:
                system of particles, beam, box
        """
        self.particles = []
        for part in range(part_num):
            part_i = Particle(
                np.random.uniform(0, max_mass),
                np.random.uniform(0, dimension, 2),
                np.random.uniform(-dimension / 5, dimension / 5, 2),
            )  # velocity can't be too fast
            self.particles.append(part_i)
        self.field_strength = field_strength
        self.beam_width = (
            dimension / 10
        )  # if (particle.pos[1] < dimension / 2 + beam_width) and (particle.pos[1] > dimension / 2 + beam_width)
        self.max_x = dimension
        self.max_y = dimension
        self.max_mass = max_mass
        self.timeline = np.arange(0, frames + 1, step_size)
        self.step_size = step_size
        self.total_energy_list = []

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

    def make_total_energy_list(self):
        """
        Compute total energy at each timestep
        """
        self.total_energy_list = np.zeros_like(self.timeline)
        for particle in self.particles:
            particle.e_list = []
            particle.make_energy_list()
            l = particle.e_list
            self.total_energy_list = self.total_energy_list + l

    def iterate_over(self):
        """
        Update each particle velocity and position
        """
        for particle in self.particles:
            particle_coords = sp.integrate.solve_ivp(
                integration_fun1,
                t_span=[self.timeline[0], self.timeline[-1]],
                y0=particle.z,
                t_eval=self.timeline,
                args=(self.max_x, self.max_y, self.field_strength, self.beam_width),
            )
            particle.z_list = particle_coords

    def plot_initial_system(self):
        """
        Plot the system under ./figures
        """
        for particle in self.particles:
            plt.plot(
                particle.pos[0],
                particle.pos[1],
                color="#50c878",  # emerald
                marker=".",
                linestyle="None",
                markersize=particle.mass,
                label=f"Particles",
            )
        plt.title(f"Particles in a Square 2D Box")
        plt.xlabel(f"X Dimension")
        plt.ylabel(f"Y Dimension")
        plt.grid()
        plt.xlim(0, self.max_x)
        plt.ylim(0, self.max_y)
        plot_destination = "./figures/system_plot.png"
        plt.savefig(plot_destination, dpi=500)

    def plot_particle_traj(self):
        for particle in self.particles:
            for frame in particle.z_list.t:
                plt.plot(
                    particle.z_list.y[0],
                    particle.z_list.y[1],
                    # 	color = '#50c878', # emerald
                    marker=".",
                    linestyle="None",
                    markersize=particle.mass,
                    label=f"Particles",
                )
        plt.hlines(self.max_y / 2 + self.beam_width, 0, self.max_x)
        plt.hlines(self.max_y / 2 - self.beam_width, 0, self.max_x)
        plt.xlim(0, self.max_x)
        plt.ylim(0, self.max_y)
        plt.xlabel(f"X Dimension")
        plt.ylabel(f"Y Dimension")
        plt.title(f"Particle Evolution in Force Field")
        plt.savefig("./figures/particle10.png", dpi=500)
        plt.clf()

    def plot_particle_byframe(self):
        for frame in self.timeline:
            for particle in self.particles:
                plt.plot(
                    particle.z_list.y[0][(int)(frame / self.step_size)],
                    particle.z_list.y[1][(int)(frame / self.step_size)],
                    # 	color = '#50c878', # emerald
                    marker=".",
                    linestyle="None",
                    markersize=particle.mass,
                    label=f"Particles",
                )

            plt.hlines(self.max_y / 2 + self.beam_width, 0, self.max_x)
            plt.hlines(self.max_y / 2 - self.beam_width, 0, self.max_x)
            plt.xlim(0, self.max_x)
            plt.ylim(0, self.max_y)
            plt.xlabel(f"X Dimension")
            plt.ylabel(f"Y Dimension")
            plt.title(
                f"Particle Evolution in Force Field, frame: ({(int)(frame / self.step_size + 1)}/{len(self.timeline)})"
            )
            plot_frame_path = f"./animation_plots/particle_frame({(int)(frame / self.step_size + 1)}).png"
            plt.savefig(plot_frame_path, dpi=500)
            plt.clf()
        images = natsorted(
            [img for img in os.listdir("./animation_plots") if img.endswith(".png")]
        )
        image_list = [
            imageio.imread(os.path.join("./animation_plots", img)) for img in images
        ]
        imageio.mimsave("./gifs/animated_particles.gif", image_list, duration=0.5)


x = System(
    10, 2, 1, 10, 10, 0.1
)  # particles, boundary, beam field, max mass, frames, step size
print(f"")
# print(f"[X, Y, Vx, Vy of First Particle]: {x.particles[0].z}")
# print(f"Field Strength: {x.field_strength}")
# print(f"Dimension Boundary: {x.max_x}")
# print(f"Total Energy: {x.total_energy()}")
# x.plot_initial_system()
x.iterate_over()
# x.particles[0].make_energy_list()
# print(f"p0 E: {x.particles[0].e_list}")

x.plot_particle_traj()
x.plot_particle_byframe()
print(len(x.particles[1].z_list.y[1]))
print(x.timeline)
# print(f"list particle 0: {x.particles[0].z_list}")

# x.make_total_energy_list()
print(x.total_energy_list)
