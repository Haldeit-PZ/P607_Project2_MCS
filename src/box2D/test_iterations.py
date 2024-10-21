import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import integration
import set_system

particle_num_list = np.arange(5, 106, 5)


monte_iterations = 1000


def test_it(particle_num_list, monte_iterations):
    list3 = []
    for part in particle_num_list:
        list1 = []
        for i in range(monte_iterations):  # repeat simulation N times
            x = set_system.System(
                part, 2, 1, 10, 10, 0.1
            )  # initialize single system randomly
            x.iterate_over()  # integrate single system
            x.make_total_energy_list()  # find energy at each integration step
            list1.append(x.total_energy_list)  # store single system energy list
            list2 = list1[0]
        for i in range(len(list1)):
            if i != 0:
                list2 = np.add(
                    list2, list1[i]
                )  # finding total energy over N sinulations at each step

        list3.append(list2)
    return list1, list2, list3


def plot_test_it(particle_num_list, monte_iterations):
    list1, list2, list3 = test_it(particle_num_list, monte_iterations)
    plt.imshow(list3)
    plt.gca().invert_yaxis()
    plt.colorbar(location="bottom")
    plt.savefig("figures/energy_change.png", dpi=500)
    plt.clf()
    for i in range(len(list3)):
        initial_energy = list3[i][0]
        list3[i] = list3[i] / initial_energy

    plt.imshow(list3)
    plt.gca().invert_yaxis()
    plt.colorbar(location="bottom")
    plt.savefig("figures/energy_change_per.png", dpi=500)
    plt.clf()

    list4 = []
    for i in range(monte_iterations):
        single = list1[i][8]
        list4.append(single)
    plt.hist(list4, 30)
    plt.savefig("figures/energy_hist.png", dpi=500)
    plt.clf()


plot_test_it(particle_num_list, monte_iterations)
