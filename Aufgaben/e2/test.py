import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin

import matplotlib.animation as animation

t_stop = 4.0  # how many seconds to simulate
history_len = 500  # how many trajectory points to display



# create a time array from 0..t_stop sampled at 0.02 second steps
dt = 0.01
t = np.arange(0, t_stop, dt)


# integrate the ODE using Euler's method
y = np.empty((len(t), 4))
for i in range(1, len(t)):
    y[i] = y[i - 1] + dt

# A more accurate estimate could be obtained e.g. using scipy:
#
#   y = scipy.integrate.solve_ivp(derivs, t[[0, -1]], state, t_eval=t).y.T

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(autoscale_on=False, xlim=(0, 1000), ylim=(0, 1000))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '.-', lw=1, ms=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)  


def animate(i):
    thisx = [0, 400, 500]
    thisy = [0, 500, 400]

    history_x = x2[:i]
    history_y = y2[:i]

    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)
    time_text.set_text(time_template % (i*dt))
    return 0, 0, time_text


ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()