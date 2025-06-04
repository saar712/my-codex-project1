#!/usr/bin/env python3
"""Real-time mouse position tracker using matplotlib."""

import pyautogui
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update(frame):
    x, y = pyautogui.position()
    xs.append(x)
    ys.append(y)
    scatter.set_offsets(list(zip(xs, ys)))
    ax.relim()
    ax.autoscale_view()
    return scatter,


fig, ax = plt.subplots()
ax.set_title('Live Mouse Position')
ax.set_xlabel('X')
ax.set_ylabel('Y')
scatter = ax.scatter([], [])
xs, ys = [], []
ani = FuncAnimation(fig, update, interval=50, blit=True)
plt.show()

