#!/usr/bin/env python3
"""Real-time mouse position tracker using a 3D matplotlib plot."""

import pyautogui
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import time


def update(frame):
    x, y = pyautogui.position()
    z = time.time() - start_time
    xs.append(x)
    ys.append(y)
    zs.append(z)
    line.set_data(xs, ys)
    line.set_3d_properties(zs)
    ax.relim()
    ax.autoscale_view()
    return line,


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Live Mouse Position in 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time (s)')

line, = ax.plot([], [], [], lw=2)
xs, ys, zs = [], [], []
start_time = time.time()

ani = FuncAnimation(fig, update, interval=50, blit=True)
plt.show()

