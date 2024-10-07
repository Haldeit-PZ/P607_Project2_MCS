# P607_Project2_MCS (Ben Maves, Haoyang Zhou)

A simulation of particles (potentially interact with each others on some random scale) in a 2D box, with or without an external driven force field (could be a function by itself, or constant) from an external beam.

## Pseudo-Code:
### Initialize the x-y positions of particles numbers, initial velocities of particles, and beam parameters using Monte Carlo Simulation.
### Set up the ODE itself, the ODE for particles in a force field is similar to a trajectory problem in effect of gravity.
### Begin iteration loop, each iteration updates the next set of particle positions, store average energy, velocity, position in separate arrays.
### Plot the list, and compare with our expectations of positions, with or without the external force.
