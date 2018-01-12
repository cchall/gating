import matplotlib.pyplot as plt
from draw_bounds import DrawBounds


"""
Prototype of new create_canvas:

def create_canvas(user adds existince plot, DrawBounds instance, other options):
    af = DrawBounds(ax=users plotting space)
    fig.canvas.mpl_connect('button_press_event', af)
    set things from other options
    plt.show()
"""

def create_canvas(xlim=[0, 1.], ylim=[0., 1.]):
    fig, ax = plt.subplots()
    af = DrawBounds(ax=ax)
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    fig.canvas.mpl_connect('button_press_event', af)
    plt.show()

def create_canvas_2(fig, ax, xlim=[0, 1.], ylim=[0., 1.]):
    af = DrawBounds(ax=ax)
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    fig.canvas.mpl_connect('button_press_event', af)
