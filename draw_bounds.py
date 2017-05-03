import matplotlib.pyplot as plt
import numpy as np
# TODO: Need to access DrawBounds instances created inside create_canvas
# May not be possible, or at least practical
# Instead user will create an instance of drawbounds they intend to use for a data set
# Will pass that into the create_canvas and the interaction will be setup there.


class DrawBounds(object):
    """
    Callback function that can be used to draw polygons on a plot.
    ax: Subplot Axes object to use.
    """

    def __init__(self, ax=None, xtol=None, ytol=None):
        if ax is None:
            self.ax = plt.gca()
        else:
            self.ax = ax

        # TODO: Current tolerance settings are just based off one test.
        # Need to think about what other factors could break.

        if xtol is None:
            self.xtol = abs(self.ax.get_xlim()[1] - self.ax.get_xlim()[0]) / 85.
        else:
            self.xtol = xtol
        if ytol is None:
            self.ytol = abs(self.ax.get_xlim()[1] - self.ax.get_xlim()[0]) / 85.
        else:
            self.ytol = ytol

        self._bounds = np.array([[self.xtol, self.ytol],
                                 [self.ax.get_xlim()[0], self.ax.get_ylim()[0]],
                                 [self.ax.get_xlim()[1], self.ax.get_ylim()[1]]])
        self.vertices = []
        self.edges = []
        self.button = []
        self.called = []

    def __call__(self, event):

        if event.inaxes:
            if event.button == 1:
                x_click = event.xdata
                y_click = event.ydata
                self.button.append(event.button)
                self.draw_vertex(x_click, y_click)
                if len(self.vertices) > 1:
                    self.draw_edge()
            elif event.button == 2 or event.button == 3:
                self.button.append(event.button)
                self.remove_vertex()
                self.remove_edge()
            else:
                pass

    def draw_vertex(self, x, y):
        # TODO: Would be nice to have a visual indication of when the point is snapped to new position
        for vertex in self.vertices:
            test_x, test_y = vertex.get_offsets()[0]
            if abs(test_x - x) <= self.xtol and abs(test_y - y) <= self.ytol:
                x = test_x
                y = test_y

        m = self.ax.scatter(x, y, marker='d', c='r', zorder=100)
        self.vertices.append(m)
        self.ax.figure.canvas.draw_idle()

    def remove_vertex(self):
        try:
            m = self.vertices[-1]
        except IndexError:
            return

        m.set_visible(not m.get_visible())
        self.vertices.pop()
        self.ax.figure.canvas.draw_idle()

    def draw_edge(self):
        x1, y1 = self.vertices[-2].get_offsets()[0]
        x2, y2 = self.vertices[-1].get_offsets()[0]
        l = self.ax.plot([x1, x2], [y1, y2], c='b', zorder=100)
        self.edges.append(l)
        self.ax.figure.canvas.draw_idle()

    def remove_edge(self):
        try:
            l = self.edges[-1][0]
        except IndexError:
            return

        l.remove()
        self.edges.pop()
        self.ax.figure.canvas.draw_idle()
