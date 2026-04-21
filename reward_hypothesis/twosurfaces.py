"""
TIME : ~2 hours
"""

import matplotlib.pyplot as plt
import numpy as np
from manim import *
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.path import Path

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

def color_map(value, vmin, vmax):
    # Normalize value to [0,1]
    norm_value = (value - vmin) / (vmax - vmin + 1e-12)
    return interpolate_color(WHITE, ManimColor(gradient_blue), norm_value)


def function2D_graph2(
    function, 
    function2=None, 
    points=False, 
    line=False, 
    x_label="x", 
    y_label="y", 
    z_label = "z",
    p1 = np.array([-2, -1]),
    p2 = np.array([0, -1]), # shared bottom
    p3 = np.array([0, 2]) # shared peak
    ): 

    p1 = p1
    p2 = p2 # shared bottom
    p3 = p3 # shared peak

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

    # --- Triangle on the floor ---
    triangle_floor = Polygon(
        axes.c2p(*p1 / 1.75, 0),
        axes.c2p(*p2 / 1.75, 0),
        axes.c2p(*p3 / 1.75, 0),
        color=text_black,
        fill_opacity=0,
    ).set_stroke(text_black, 0)

    floor_triangle_points_p1 = axes.c2p(*p1 / 1.75, 0)
    floor_triangle_points_p2 = axes.c2p(*p2 / 1.75, 0)
    floor_triangle_points_p3 = axes.c2p(*p3 / 1.75, 0)


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
                    fill_color=color_map(value, vmin, vmax),
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
    ).set_opacity(0)
    linez = DashedLine(
        axes.c2p(*p3 / 1.75, 0),
        axes.c2p(*p3 / 1.75, function(*p3) / 1.1),
        color=text_black,
        stroke_width=1,
    ).set_opacity(0)

    lines.add(linex, liney, linez)

    if points:
        if x_label == "":

            dot_x = Dot(
                axes.c2p(p1 / 1.75),
                color=node_orange,
                stroke_color=text_black,
                stroke_width=1,
            ).set_opacity(0)

        else : 
            dot_x = Dot(
                axes.c2p(p1 / 1.75),
                color=node_orange,
                stroke_color=text_black,
                stroke_width=1,
            )

        if y_label == "":

            dot_y = Dot(
                axes.c2p(p2 / 1.75),
                color=node_purple,
                stroke_color=text_black,
                stroke_width=1,
            ).set_opacity(0)

        else : 
            dot_y = Dot(
                axes.c2p(p2 / 1.75),
                color=node_purple,
                stroke_color=text_black,
                stroke_width=1,
            )

        if z_label == "":

            dot_z = Dot(
                axes.c2p(p3 / 1.75),
                color=node_green,
                stroke_color=text_black,
                stroke_width=1,
            ).set_opacity(0)

        else : 
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

    point = axes.c2p(*p3 / 1.75, function(*p3) / 1.1)
    point_bottom = axes.c2p(*p2 / 1.75, function(*p2) / 1.1)
    point_bottom_left = axes.c2p(*p2 / 1.75, function(*p2) / 1.1)

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

    return subfig, surface, point, point_bottom, point_bottom_left, floor_triangle_points_p1, floor_triangle_points_p2, floor_triangle_points_p3


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

"""

def function2D_graph2(
    function, 
    function2=None, 
    points=False, 
    line=False, 
    x_label="x", 
    y_label="y", 
    z_label = "z",
    p1 = np.array([-2, -1]),
    p2 = np.array([0, -1]), # shared bottom
    p3 = np.array([0, 2])
    )

    p1 = np.array([-2, -1])
    p2 = np.array([2, -1])
    p3 = np.array([0, 2]) # shared peak
    p4 = np.array([0, -1]) # shared bottom

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

    # --- Axes ---
    axes = ThreeDAxes(
        x_range=[-3, 3, 1],
        y_range=[-3, 3, 1],
        z_range=[-3, 3, 1],
    )
    axes.set_opacity(0)

    # --- Surface with clipping ---
    surface1 = Surface(
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
                    fill_color=color_map(value, vmin, vmax),
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
        if x_label == "":

            dot_x = Dot(
                axes.c2p(p1 / 1.75),
                color=node_orange,
                stroke_color=text_black,
                stroke_width=1,
            ).set_opacity(0)

        else : 
            dot_x = Dot(
                axes.c2p(p1 / 1.75),
                color=node_orange,
                stroke_color=text_black,
                stroke_width=1,
            )

        if y_label == "":

            dot_y = Dot(
                axes.c2p(p2 / 1.75),
                color=node_purple,
                stroke_color=text_black,
                stroke_width=1,
            ).set_opacity(0)

        else : 
            dot_y = Dot(
                axes.c2p(p2 / 1.75),
                color=node_purple,
                stroke_color=text_black,
                stroke_width=1,
            )

        if z_label == "":

            dot_z = Dot(
                axes.c2p(p3 / 1.75),
                color=node_green,
                stroke_color=text_black,
                stroke_width=1,
            ).set_opacity(0)

        else : 
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
"""
