import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


fig, ax = plt.subplots(figsize=(12,6))
xy_pair = {}


def clear():
    ax.clear()
    ax.set_xlim((0,100))
    ax.set_ylim((-100,100))

def onclick(event):
    global xy_pair
    clear()

    xy_pair[float(event.xdata)] = float(event.ydata)
    sorted(xy_pair)
    #ax[0].plot(list(xy_pair.keys()), list(xy_pair.values()))
    ax.plot(list(xy_pair.keys()), list(xy_pair.values()), 'o')
    plt.show()


    if xy_pair and len(xy_pair) >= 2:
        new = basisfunktionen(list(xy_pair.keys()), list(xy_pair.values()))
        sorted(new)
        ax.plot(list(new.keys()), list(new.values()), color="green")
        plt.show()
    #print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % ('double' if event.dblclick else 'single', event.button, event.x, event.y, event.xdata, event.ydata))

def basisfunktionen(x, y):
    arr = np.zeros((len(x), len(x)))
    xy = {}

    for i in range(0, len(x)):  
        for j in range(0, len(x)):
            arr[j][i] = pow(x[j], i)

    c = np.linalg.solve(arr, y)
    print("c: "+str(c))

    for i in np.arange(x[0], x[-1]+1, 1):
        val = 0

        for j in range(0, len(x)):
            val += c[j] * pow(i, j)

        xy[i] = val
        print("xy: "+str(xy))
    return xy


cid = fig.canvas.mpl_connect('button_press_event', onclick)
ax.set_xlim((0,100))
ax.set_ylim((-100,100))
plt.show()