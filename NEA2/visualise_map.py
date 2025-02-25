import matplotlib.pyplot as plt
from data_types2 import vec2
from map_layout import MAP_LAYOUT

def visualize_map(layout):
    fig, ax = plt.subplots()
    for segment in layout:
        (x0, y0), (x1, y1) = segment
        ax.plot([x0, x1], [y0, y1], 'k-')  # Draw the segment as a black line

    ax.set_aspect('equal')
    ax.set_xlim(-1, 33)
    ax.set_ylim(-1, 33)
    ax.grid(True)
    plt.show()

if __name__ == '__main__':
    visualize_map(MAP_LAYOUT)