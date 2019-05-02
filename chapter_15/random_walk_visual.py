import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=5)

    plt.plot(rw.x_values[-1], rw.y_values[-1], linewidth=5)

    plt.show()

    keep_running = input('Make another walk? y/n: ')
    if keep_running == 'n':
        break
