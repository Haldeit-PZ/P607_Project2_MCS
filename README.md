# P607_Project2_MCS (Ben Maves, Haoyang Zhou)

A simulation of particles (potentially interact with each others on some random scale) in a 2D box, with or without an external driven force field (could be a function by itself, or constant) from an external beam.

To run the code, please first clone the repo, then install the package with:
```
pip install -e .
```

The command to run the script is:
```
simulateBox
```

This will create an animation under folder ./gif, some plots showing overall trajectories, energy under ./figures. ./animation plots are the frames of the gif created.

![](https://github.com/Haldeit-PZ/P607_Project2_MCS/blob/main/gifs/animated_particles.gif)
