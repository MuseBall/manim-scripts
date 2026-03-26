"""
TIME : ~2 hours
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.colors import LinearSegmentedColormap

# Define the grid
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 1, 400)
X, Y = np.meshgrid(x, y)

# Example heatmap function
Z = -X + Y

# Define triangle mask

verts = np.array([[0, 0], [-3, -3], [3, -3]])
path = Path(verts)
points = np.vstack((X.flatten(), Y.flatten())).T
mask = path.contains_points(points).reshape(X.shape)

# Normalize Z for coloring

Z_norm = (Z - Z.min()) / (Z.max() - Z.min())


# Create custom blue-to-white colormap

cmap = LinearSegmentedColormap.from_list(
    "blue_white",
    ["#749b99", "#ffffff"]  # deep blue -> white
)

#  Apply colormap
rgba = cmap(Z_norm)

# Apply triangle mask to alpha channel
rgba[..., -1] = mask.astype(float)


# Save as PNG (origin lower to match Manim)
plt.imsave("triangle_heatmap.png", rgba, origin='lower')


def triangle_heatmap(vertices, function, plotsave=False, filename="triangle_heatmap.png",
                           canvas_size=(500, 500), xlim=(-3, 3), ylim=(-3, 1), cmap_colors=["#749b99", "#ffffff"]):
    """
    vertices: numpy array of triangle vertices [[x0,y0],[x1,y1],[x2,y2]]
    function: function f(X,Y)
    plotsave: save PNG
    filename: file path
    canvas_size: output pixel size
    xlim, ylim: fixed canvas limits
    cmap_colors: colors for LinearSegmentedColormap
    """

    # fixed meshgrid
    x = np.linspace(xlim[0], xlim[1], canvas_size[0])
    y = np.linspace(ylim[0], ylim[1], canvas_size[1])
    X, Y = np.meshgrid(x, y)

    # apply function
    Z = function(X, Y)

    # normalize
    Z_norm = (Z - Z.min()) / (Z.max() - Z.min() + 1e-12)

    # mask triangle
    path = Path(vertices)
    points = np.vstack((X.flatten(), Y.flatten())).T
    mask = path.contains_points(points).reshape(X.shape)

    # colormap
    cmap = LinearSegmentedColormap.from_list("custom", cmap_colors)
    rgba = cmap(Z_norm)

    # apply mask
    rgba[..., -1] = mask.astype(float)

    # save
    if plotsave:
        plt.imsave(filename, rgba, origin='lower')

    return rgba