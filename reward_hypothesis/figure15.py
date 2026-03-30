"""
TIME : 17:30 - 19:15
       22:30 - 23:50


Guille - Reward Hypothesis - Dovetail Project

Images for Section in Mixture space - Expected utility - Indepen-
dence and Continuity - vNM theorem
Figure 15: Independence

Generate image by simple running script:
python ./figure15.py
"""

import numpy as np
from manim import *
from nodes_and_arrows import make_arrow
from plttriangle import function1D_heatmap, function2D_graph

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = config.pixel_height / config.pixel_width * config.frame_width


class Graph(ThreeDScene):
    def construct(self):

        # hex code of colours
        self.camera.background_color = "#dce2e1"
        text_black = "#22323b"
        node_yellow = "#e1c180"
        node_green = "#a9c199"
        node_blue = "#9acecc"
        node_orange = "#d49870"
        node_red = "#d67f86"
        node_pink = "#c78d9c"
        node_purple = "#b6b3c4"

        # background rectangle with rounded corners
        background_rectangle = RoundedRectangle(
            color="#d6e2e2", fill_opacity=1, corner_radius=0.7, height=8, width=8
        )

        # Top left graph
        function1D_heatmap_1 = function1D_heatmap(
            lambda x: x / 2 if x < 2.5 else -x / 2 + 2.5
        )

        function1D_heatmap_1.shift(LEFT * 5.5)

        # Top right graph
        function2D_graph_1 = function2D_graph(
            lambda x, y: x / 2 + 2 if x < 1 / 2 else -x / 2 + 2.5, line=True
        )

        function2D_graph_1.shift(UP * 1).scale(0.8)

        # Bottom left graph
        function1D_heatmap_2 = function1D_heatmap(lambda x: 0.5 if x < 1 else x / 2)

        function1D_heatmap_2.shift(DOWN * 3 + LEFT * 5.5)

        # Bottom right graph
        function2D_graph_2 = function2D_graph(
            lambda x, y: 2 if x < -1 / 2 else x / 2 + 2.25, line=True
        )

        function2D_graph_2.shift(DOWN * 4).scale(0.65)

        # Points on the lines
        # Top left graph
        line1 = function1D_heatmap_1.graph
        y_1 = Dot(
            line1.point_from_proportion(0.4),
            color=node_blue,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_y1 = (
            MathTex("y", font_size=50)
            .scale(0.6)
            .set_color(text_black)
            .next_to(y_1, DOWN)
            .shift(UP * 0.2)
        )

        x_1 = Dot(
            line1.point_from_proportion(0.5),
            color=node_red,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_x1 = (
            MathTex("x", font_size=50)
            .scale(0.6)
            .set_color(text_black)
            .next_to(x_1, DOWN)
            .shift(UP * 0.2)
        )

        y_2 = Dot(
            line1.point_from_proportion(0.7),
            color=node_green,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_y2 = (
            MathTex(r"\frac{1}{2} y + \frac{1}{2} z", font_size=40)
            .scale(0.6)
            .set_color(text_black)
            .next_to(y_2, UP)
            .shift(RIGHT * 0.2)
        )

        x_2 = Dot(
            line1.point_from_proportion(0.75),
            color=node_orange,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_x2 = (
            MathTex(r"\frac{1}{2} x + \frac{1}{2} z", font_size=40)
            .scale(0.6)
            .set_color(text_black)
            .next_to(x_2, RIGHT)
            .shift(UP * 0.2)
        )

        z_2 = Dot(
            line1.point_from_proportion(0.99),
            color=node_yellow,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_z2 = (
            MathTex("z", font_size=50)
            .scale(0.6)
            .set_color(text_black)
            .next_to(z_2, DOWN)
            .shift(UP * 0.2)
        )
        dots1 = Group(
            y_1, label_y1, x_1, label_x1, y_2, label_y2, x_2, label_x2, z_2, label_z2
        )

        # Bottom left graph
        line2 = function1D_heatmap_2.graph
        y_tri_1 = Dot(
            line2.point_from_proportion(0.2),
            color=node_blue,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_tri_y1 = (
            MathTex("y", font_size=50)
            .scale(0.6)
            .set_color(text_black)
            .next_to(y_tri_1, DOWN)
        ).shift(UP * 0.2)

        x_tri_1 = Dot(
            line2.point_from_proportion(0.1),
            color=node_red,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_tri_x1 = (
            MathTex("x", font_size=50)
            .scale(0.6)
            .set_color(text_black)
            .next_to(x_tri_1, DOWN)
        ).shift(UP * 0.2)

        y_tri_2 = Dot(
            line2.point_from_proportion(0.6),
            color=node_green,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_tri_y2 = (
            MathTex(r"\frac{1}{2} y + \frac{1}{2} z", font_size=40)
            .scale(0.6)
            .set_color(text_black)
            .next_to(y_tri_2, LEFT)
        )

        x_tri_2 = Dot(
            line2.point_from_proportion(0.55),
            color=node_orange,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_tri_x2 = (
            MathTex(r"\frac{1}{2} x + \frac{1}{2} z", font_size=40)
            .scale(0.6)
            .set_color(text_black)
            .next_to(x_tri_2, UP)
        )

        z_tri_2 = Dot(
            line2.point_from_proportion(0.99),
            color=node_yellow,
            stroke_color=text_black,
            stroke_width=1,
        )
        label_tri_z2 = (
            MathTex("z", font_size=50)
            .scale(0.6)
            .set_color(text_black)
            .next_to(z_tri_2, DOWN)
        ).shift(UP * 0.2)
        dots2 = Group(
            y_tri_1,
            label_tri_y1,
            x_tri_1,
            label_tri_x1,
            y_tri_2,
            label_tri_y2,
            x_tri_2,
            label_tri_x2,
            z_tri_2,
            label_tri_z2,
        )

        # Top right dots
        line3 = function2D_graph_1.surface.line
        y_3 = Ellipse(
            width=0.13,
            height=0.3,
            fill_color=node_blue,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line3.point_from_proportion(0.6))

        x_3 = Ellipse(
            width=0.13,
            height=0.3,
            fill_color=node_red,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line3.point_from_proportion(0.7))

        y_32 = Ellipse(
            width=0.13,
            height=0.3,
            fill_color=node_green,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line3.point_from_proportion(0.8))

        x_32 = Ellipse(
            width=0.13,
            height=0.3,
            fill_color=node_orange,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line3.point_from_proportion(0.85))

        z_32 = Ellipse(
            width=0.13,
            height=0.3,
            fill_color=node_yellow,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line3.point_from_proportion(0.99))
        dots3 = Group(y_3, x_3, y_32, x_32, z_32)

        # Bottom right dots
        line4 = function2D_graph_2.surface.line
        y_4 = Ellipse(
            width=0.1,
            height=0.2,
            fill_color=node_blue,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line4.point_from_proportion(0.2))

        x_4 = Ellipse(
            width=0.1,
            height=0.2,
            fill_color=node_red,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line4.point_from_proportion(0.1))

        y_42 = Ellipse(
            width=0.1,
            height=0.2,
            fill_color=node_green,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line4.point_from_proportion(0.6))

        x_42 = Ellipse(
            width=0.1,
            height=0.2,
            fill_color=node_orange,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line4.point_from_proportion(0.55))

        z_42 = Ellipse(
            width=0.1,
            height=0.2,
            fill_color=node_yellow,
            fill_opacity=1,
            stroke_color=text_black,
            stroke_width=1,
        ).move_to(line4.point_from_proportion(0.99))
        dots4 = Group(y_4, x_4, y_42, x_42, z_42)

        line_x_4 = DashedLine(
            [3, -1.5, 0], [3, -1, 0], dash_length=0.15, color="#739b99", stroke_width=3
        )
        line_y_4 = DashedLine(
            [1, -3, 0], [1, -2, 0], dash_length=0.15, color="#739b99", stroke_width=3
        )
        line_z_4 = DashedLine(
            [5, -3, 0], [5, -1, 0], dash_length=0.15, color="#739b99", stroke_width=3
        )

        label_x4 = (
            MathTex("x", font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(line_x_4, RIGHT)
        )
        label_y4 = (
            MathTex("y", font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(line_y_4, DOWN)
        )
        label_z4 = (
            MathTex("z", font_size=60)
            .scale(0.6)
            .set_color(text_black)
            .next_to(line_z_4, DOWN)
        )

        label_right = (
            Tex("Not Independent", font_size=75)
            .scale(0.6)
            .set_color(text_black)
            .move_to([0, 3, 0])
        )

        label_left = (
            Tex("Not Monotonic", font_size=70)
            .scale(0.6)
            .set_color(text_black)
            .move_to([4.5, 1.5, 0])
        )

        label_left_1 = (
            Tex("Not if Constant, \\\\ Fully Constant", font_size=70)
            .scale(0.6)
            .set_color(text_black)
            .move_to([4.5, -1.2, 0])
        )

        all_2D = Group(
            function1D_heatmap_1,
            function1D_heatmap_2,
            label_right,
            label_left,
            label_left_1,
            dots1,
            dots2,
        )
        all_3D = Group(
            function2D_graph_1,
            function2D_graph_2,
            dots3,
            dots4,
        )

        self.add(all_3D)
        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
        # self.add(NumberPlane())
