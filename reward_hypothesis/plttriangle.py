"""
TIME : ~2 hours
"""

import matplotlib.pyplot as plt
import numpy as np
from manim import *
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.path import Path

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
    "blue_white", ["#041094", "#ffffff"]  # deep blue -> white
)

#  Apply colormap
rgba = cmap(Z_norm)

# Apply triangle mask to alpha channel
rgba[..., -1] = mask.astype(float)


text_black = "#22323b"
node_yellow = "#e1c180"
node_green = "#a9c199"
node_blue = "#9acecc"
node_orange = "#d49870"
node_red = "#d67f86"
node_pink = "#c78d9c"
node_purple = "#b6b3c4"
#gradient_blue = "#769c9a"
gradient_blue = "#71bbb8"
gradient_white = "#fff1e8"



# Save as PNG (origin lower to match Manim)
plt.imsave("triangle_heatmap.png", rgba, origin="lower")


def color_map(value, vmin, vmax):
    # Normalize value to [0,1]
    norm_value = (value - vmin) / (vmax - vmin + 1e-12)
    return interpolate_color(WHITE, ManimColor(gradient_blue), norm_value)


def triangle_heatmap(
    vertices,
    function,
    plotsave=False,
    filename="triangle_heatmap.png",
    canvas_size=(500, 500),
    xlim=(0, 6),
    ylim=(0, 6),
    cmap_colors=["#041094", "#ffffff"],
):

    # fixed meshgrid
    x = np.linspace(xlim[0], xlim[1], canvas_size[0])
    y = np.linspace(ylim[0], ylim[1], canvas_size[1])
    X, Y = np.meshgrid(x, y)

    # function
    Z = function(X, Y)

    # normalize
    Z_norm = (Z - Z.min()) / (Z.max() - Z.min() + 1e-12)

    # --- center triangle using bounding box (visual centering) ---
    xmin, xmax = vertices[:, 0].min(), vertices[:, 0].max()
    ymin, ymax = vertices[:, 1].min(), vertices[:, 1].max()

    triangle_center = np.array([(xmin + xmax) / 2, (ymin + ymax) / 2])

    canvas_center = np.array([(xlim[0] + xlim[1]) / 2, (ylim[0] + ylim[1]) / 2])

    centered_vertices = vertices + (canvas_center - triangle_center)

    # mask
    path = Path(centered_vertices)
    points = np.vstack((X.flatten(), Y.flatten())).T
    mask = path.contains_points(points).reshape(X.shape)

    # colormap
    cmap = LinearSegmentedColormap.from_list("custom", cmap_colors)
    rgba = cmap(Z_norm)

    # alpha mask
    rgba[..., -1] = mask.astype(float)

    # save
    if plotsave:
        plt.imsave(filename, rgba, origin="lower")

    return rgba


def function1D_graph(
    function, 
    function2 = None
):

    if function2 == None :

        axes_1 = Axes(
            x_range=[-0.5, 8],
            y_range=[-0.5, 8],
            x_length=4,
            y_length=3,
            x_axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
            axis_config={"tip_shape": StealthTip, "color": text_black},
        )

    else :

        axes_1 = Axes(
            x_range=[-0.5, 16],
            y_range=[-0.5, 8],
            x_length=5,
            y_length=3,
            x_axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
            axis_config={"tip_shape": StealthTip, "color": text_black},
        )


    labels_axes_1 = axes_1.get_axis_labels(
        MathTex("X", color=text_black, stroke_width=1.5).scale(0.8),
        MathTex(r"f(x) \in \mathbb{R}", color=text_black, stroke_width=1.5).scale(0.8),
    )

    labels_axes_1[0].next_to(axes_1.get_x_axis().get_right(), RIGHT)
    labels_axes_1[1].next_to(axes_1.get_y_axis().get_top(), LEFT)

    # Points in graph
    a = 0
    b = 4
    x = 1
    y = 5
    delta = 1
    point_x_1 = axes_1.coords_to_point(x, 0)
    point_fx_1 = axes_1.coords_to_point(x, function(a) + delta)
    point_y_1 = axes_1.coords_to_point(y, 0)
    point_fy_1 = axes_1.coords_to_point(y, function(b) + delta)

    point_x_2 = axes_1.coords_to_point(x, 0)
    point_fx_2 = axes_1.coords_to_point(x, function2(a) + delta)
    point_y_2 = axes_1.coords_to_point(y, 0)
    point_fy_2 = axes_1.coords_to_point(y, function2(b) + delta)

    dot_x_1 = Dot(point_x_1, color=node_orange, stroke_color=text_black, stroke_width=1)
    dot_y_1 = Dot(point_y_1, color=node_purple, stroke_color=text_black, stroke_width=1)

    dot_x_2 = Dot(point_x_2, color=node_orange, stroke_color=text_black, stroke_width=1)
    dot_y_2 = Dot(point_y_2, color=node_purple, stroke_color=text_black, stroke_width=1)

    curve = axes_1.plot(
        lambda s: function(s - x) + delta, x_range=[x, y], color=text_black, stroke_width = 3
    )

    curve2 = axes_1.plot(
        lambda s: function2(s - x) + delta, x_range=[x, y], color=text_black, stroke_width = 3
    )

    # function2

    line_x_1 = DashedLine(
        point_x_1,
        point_fx_1,
        dash_length=0.15,
        color="#739b99",
        stroke_width=3,
    )
    line_y_1 = DashedLine(
        point_y_1,
        point_fy_1,
        dash_length=0.15,
        color="#739b99",
        stroke_width=3,
    )

    label_x_1 = (
        MathTex("x", font_size=60)
        .scale(0.6)
        .set_color(text_black)
        .next_to(line_x_1, DOWN)
    )
    label_y_1 = (
        MathTex("y", font_size=60)
        .scale(0.6)
        .set_color(text_black)
        .next_to(line_y_1, DOWN)
    )

    # function2

    line_x_2 = DashedLine(
        point_x_2,
        point_fx_2,
        dash_length=0.15,
        color="#739b99",
        stroke_width=3,
    )
    line_y_2 = DashedLine(
        point_y_2,
        point_fy_2,
        dash_length=0.15,
        color="#739b99",
        stroke_width=3,
    )

    label_x_2 = (
        MathTex("t \cdot_T x", font_size=60)
        .scale(0.6)
        .set_color(text_black)
        .next_to(line_x_2, DOWN)
    )
    label_y_2 = (
        MathTex("t \cdot_T y", font_size=60)
        .scale(0.6)
        .set_color(text_black)
        .next_to(line_y_2, DOWN)
    )

    subfig = Group(
        axes_1,
        labels_axes_1,
        line_x_1,
        line_y_1,
        label_x_1,
        label_y_1,
        dot_x_1,
        dot_y_1,
        curve,
        line_x_2,
        line_y_2,
        label_x_2,
        label_y_2,
        dot_x_2,
        dot_y_2,
        curve2,    
    )

    graph2 = Group(line_x_2,
        line_y_2,
        label_x_2,
        label_y_2,
        dot_x_2,
        dot_y_2,
        curve2,).shift(RIGHT * 2)

    return subfig


def function1D_heatmap(
    function,
    points=False,
    x_label = "x",
    y_label = "y",
):

    # Axes
    axes = Axes(
        x_range=[-1.5, 3.5],
        x_length=4,
        tips=False,
        x_axis_config={"include_numbers": False, "include_ticks": False},
        axis_config={"tip_shape": None, "color": text_black},
    )

    axes.y_axis.set_opacity(0)

    labels_axes = axes.get_axis_labels(
        MathTex(r"(\mathbb{R}, >)", color=text_black, stroke_width=1.5).scale(0.8)
    )

    labels_axes[0].set_opacity(0)
    labels_axes[1].set_opacity(0)
    a = 0
    b = 4

    point_x = axes.coords_to_point(a, 0)
    point_y = axes.coords_to_point(b, 0)

    # Points in graph
    line_xy = Line(
        point_x,
        point_y,
        color=text_black,
        stroke_width=2,
    )

    if points:

        dot_x = Dot(point_x, color=node_orange, stroke_color=text_black, stroke_width=1)
        dot_y = Dot(point_y, color=node_purple, stroke_color=text_black, stroke_width=1)

        label_x = (
            MathTex(x_label, font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(dot_x, DOWN)
        )
        label_y = (
            MathTex(y_label, font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(dot_y, DOWN)
        )

    else:
        tick1 = Line(
            axes.c2p(a, 0.1),
            axes.c2p(a, -0.1),
            color=text_black,
            stroke_width=2,
        )
        tick2 = Line(
            axes.c2p(b, 0.1),
            axes.c2p(b, -0.1),
            color=text_black,
            stroke_width=2,
        )
        line_xy.add(tick1, tick2)

    # Plot function
    delta = 0.5
    graph = axes.plot(
        #lambda x: function(x) + 2 * delta, x_range=[a, b], color=text_black,
        lambda x: function(x) + 2 * delta, x_range=[a, b], color=text_black, stroke_width = 2
    )

    # Sample points along curve
    n = 100
    xs = np.linspace(a, b, n)

    curve_points = [axes.c2p(x, function(x) + delta) for x in xs]

    values = [function(x) for x in xs]
    vmin, vmax = min(values), max(values)

    strips = VGroup()
    eps = 1e-2
    for i in range(n - 1):
        x0 = xs[i]
        x1 = xs[i + 1]

        y0 = function(x0) + delta
        y1 = function(x1) + delta

        subarea = Polygon(
            axes.c2p(x0 - eps, y0),
            axes.c2p(x1 + eps, y1),
            axes.c2p(x1 + eps, delta),
            axes.c2p(x0 - eps, delta),
            color=gradient_blue,
            fill_opacity=1,
            fill_color=color_map(function((x0 + x1) / 2), vmin, vmax),
        ).set_stroke(width=0)
        strips.add(subarea)

    # Build polygon (area shape)
    area = Polygon(
        *curve_points,
        axes.c2p(b, delta),
        axes.c2p(a, delta),
        color=text_black,
        fill_opacity=0,
    ).set_stroke(text_black, 2)

    if points:
        subfig = Group(line_xy, dot_x, label_x, dot_y, label_y, strips, area)
        subfig.graph = graph
    else:
        subfig = Group(line_xy, strips, area, graph)
        subfig.graph = graph

    return subfig


def function2D_graph(function, function2=None, points=False, line=False, x_label="x", y_label="y", z_label = "z"):

    p1 = np.array([-2, -1])
    p2 = np.array([2, -1])
    p3 = np.array([0, 2])

    xs = np.linspace(-3, 3, 100)
    ys = np.linspace(-3, 3, 100)
    values = [
        (
            function(x, y)
            if is_inside_triangle(np.array([x, y, 0]), p1, p2, p3)
            else function(0, 0)
        )
        for x in xs
        for y in ys
    ]
    vmin, vmax = min(values), max(values)
    """
    if function2 is not None:
        valuesf2
        vmin2, vax2 
        totalvmin = min(vim, vim2)
    """

    # --- Axes ---
    axes = ThreeDAxes(
        x_range=[-3, 3, 1],
        y_range=[-3, 3, 1],
        z_range=[-3, 3, 1],
    )
    axes.set_opacity(0)

    # --- Surface with clipping ---
    surface = Surface(
        lambda u, v: (
            (1 - u) * p1[0] + u * ((1 - v) * p2[0] + v * p3[0]),
            (1 - u) * p1[1] + u * ((1 - v) * p2[1] + v * p3[1]),
            function(
                (1 - u) * p1[0] + u * ((1 - v) * p2[0] + v * p3[0]),
                (1 - u) * p1[1] + u * ((1 - v) * p2[1] + v * p3[1]),
            ),
        ),
        u_range=[0, 1],
        v_range=[0, 1],
        resolution=(60, 60),
    )

    # --- Color by height ---
    surface.set_fill_by_value(
        axes=axes,
        colors=[
            (WHITE, vmin),
            (gradient_blue, vmax),
        ],
    )

    surface.set_shade_in_3d(False)

    # if function2 is not None:


    # --- Triangle on the floor ---
    triangle_floor = Polygon(
            axes.c2p(*p1 / 1.75, 0),
            axes.c2p(*p2 / 1.75, 0),
            axes.c2p(*p3 / 1.75, 0),
            color=text_black,
            fill_opacity=0,
        ).set_stroke(text_black, 1)

    # --- Sampling grid ---
    resolution = 150
    x_vals = np.linspace(-2.5, 2.5, resolution)
    y_vals = np.linspace(-2.5, 2.5, resolution)

    cells = VGroup()

    # --- Fill triangle ---
    dx = x_vals[1] - x_vals[0]
    eps = 1e-2

    for i in range(len(x_vals)):
        for j in range(len(y_vals)):
            x = x_vals[i]
            y = y_vals[j]
            point = np.array([x, y, 0])

            if is_inside_triangle(point, p1, p2, p3): 
                value = function(x, y)

                cell = Square(
                    side_length=dx + eps,
                    #fill_color=color_map(value, totalvmin, vmax),
                    fill_color=color_map(value, vmax),
                    fill_opacity=1,
                    stroke_width=0,
                ).move_to(point)

                cells.add(cell)

    # --- Line on surface ---
    if line:
        pts = np.linspace(0, 1, 100)
        ip = np.array([-1, 0])
        fp = np.array([1, 0])
        pts = np.array([(1 - t) * ip + t * fp for t in pts])
        fpts = np.array(
            [axes.c2p(pt[0] / 1.75, pt[1] / 1.75, function(pt[0], pt[1])) for pt in pts]
        )
        curve = VMobject()
        curve.set_points_as_corners(fpts)
        curve.set_stroke(color=text_black, width=2)
        surface.line = curve
        surface.add(curve)

    # --- Vertical lines ---
    lines = VGroup()
    linex = DashedLine(
        axes.c2p(*p1 / 1.75, 0),
        axes.c2p(*p1 / 1.75, function(*p1) / 1.1),
        color=text_black,
        stroke_width=1,
    )
    liney = DashedLine(
        axes.c2p(*p2 / 1.75, 0),
        axes.c2p(*p2 / 1.75, function(*p2) / 1.1),
        color=text_black,
        stroke_width=1,
    )
    linez = DashedLine(
        axes.c2p(*p3 / 1.75, 0),
        axes.c2p(*p3 / 1.75, function(*p3) / 1.1),
        color=text_black,
        stroke_width=1,
    )

    lines.add(linex, liney, linez)

    if points:

        dot_x = Dot(
            axes.c2p(p1 / 1.75),
            color=node_orange,
            stroke_color=text_black,
            stroke_width=1,
        )
        dot_y = Dot(
            axes.c2p(p2 / 1.75),
            color=node_purple,
            stroke_color=text_black,
            stroke_width=1,
        )
        dot_z = Dot(
            axes.c2p(p3 / 1.75),
            color=node_green,
            stroke_color=text_black,
            stroke_width=1,
        )

        label_x = (
            MathTex(x_label, font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(dot_x, DOWN)
        )
        label_y = (
            MathTex(y_label, font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(dot_y, DOWN)
        )
        label_z = (
            MathTex(z_label, font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(dot_z, RIGHT)
        )

    if points:

        subfig = Group(
            axes,
            cells,
            triangle_floor,
            lines,
            surface,
            dot_x,
            label_x,
            dot_y,
            label_y,
            dot_z,
            label_z,
        )
        subfig.surface = surface
    else:
        subfig = Group(axes, cells, triangle_floor, lines, surface)
        subfig.surface = surface

    return subfig


def function2D_heatmap(
    function,
    points=False,
):

    side = 4
    h = np.sqrt(3) / 2 * side

    p1 = np.array([-side / 2, -h / 3, 0])
    p2 = np.array([side / 2, -h / 3, 0])
    p3 = np.array([0, 2 * h / 3, 0])

    triangle = Polygon(p1, p2, p3, fill_opacity=0).set_stroke(text_black, 2)
    if points:
        dot_x = Dot(p1, color=node_orange, stroke_color=text_black, stroke_width=1)
        dot_y = Dot(p2, color=node_purple, stroke_color=text_black, stroke_width=1)
        dot_z = Dot(p3, color=node_green, stroke_color=text_black, stroke_width=1)

        label_x = (
            MathTex("x", font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(dot_x, DOWN)
        )
        label_y = (
            MathTex("y", font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(dot_y, DOWN)
        )
        label_z = (
            MathTex("z", font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(dot_z, RIGHT)
        )

    # --- Sampling grid ---
    resolution = 150
    x_vals = np.linspace(-2.5, 2.5, resolution)
    y_vals = np.linspace(-2.5, 2.5, resolution)

    cells = VGroup()

    # Precompute min/max for normalization
    values = []
    for x in x_vals:
        for y in y_vals:
            if is_inside_triangle(np.array([x, y, 0]), p1, p2, p3):
                values.append(function(x, y))
    vmin, vmax = min(values), max(values)

    # --- Fill triangle ---
    dx = x_vals[1] - x_vals[0]
    eps = 1e-2

    for i in range(len(x_vals)):
        for j in range(len(y_vals)):
            x = x_vals[i]
            y = y_vals[j]
            point = np.array([x, y, 0])

            if is_inside_triangle(point, p1, p2, p3):
                value = function(x, y)

                cell = Square(
                    side_length=dx + eps,
                    fill_color=color_map(value, vmin, vmax),
                    fill_opacity=1,
                    stroke_width=0,
                ).move_to(point)

                cells.add(cell)

    if points:
        subfig = Group(cells, triangle, dot_x, label_x, dot_y, label_y, dot_z, label_z)
    else:
        subfig = Group(cells, triangle)
    return subfig


def is_inside_triangle(p, a, b, c):
    # Convert to 2D
    p, a, b, c = p[:2], a[:2], b[:2], c[:2]

    v0 = c - a
    v1 = b - a
    v2 = p - a

    dot00 = np.dot(v0, v0)
    dot01 = np.dot(v0, v1)
    dot02 = np.dot(v0, v2)
    dot11 = np.dot(v1, v1)
    dot12 = np.dot(v1, v2)

    denom = dot00 * dot11 - dot01 * dot01
    if denom == 0:
        return False

    u = (dot11 * dot02 - dot01 * dot12) / denom
    v = (dot00 * dot12 - dot01 * dot02) / denom

    return (u >= 0) and (v >= 0) and (u + v <= 1)
