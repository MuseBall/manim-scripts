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

def triangle_heatmap(vertices, function, plotsave=False, filename = "triangle_heatmap.png"):
    """
    vertices: numpy array of triangle vertices in a list 
        eg:
        np.array([[0, 0], [-3, -3], [3, -3]])
    function: python function that takes two arguments
        eg: 
        np.sin(X) + np.cos(Y)
    """

    # meshgrid
    A = vertices[0]
    B = vertices[1]
    C = vertices[2]
    xmin, xmax = np.min(A[0], B[0], C[0]), np.max(A[0], B[0], C[0])
    ymin, ymax = np.min(A[1], B[1], C[1]), np.max(A[1], B[1], C[1])

    x = np.linspace(xmin, xmax, 400)
    y = np.linspace(ymin, ymax, 400)
    X, Y = np.meshgrid(x, y)

    # apply function
    Z = function(X, Y)

    # normalize
    Z_norm = (Z - Z.min()) / (Z.max() - Z.min())

    # mask from vertices
    path = Path(vertices)
    points = np.vstack((X.flatten(), Y.flatten())).T
    mask = path.contains_points(points).reshape(X.shape)

    # linear cmap
    cmap = LinearSegmentedColormap.from_list("blue_white",["#749b99", "#ffffff"])
    rgba = cmap(Z_norm)

    # apply alpha mask
    rgba[..., -1] = mask.astype(float)

    # plot as png
    if plotsave:
        plt.imsave(filename, rgba, origin='lower')

    return rgba