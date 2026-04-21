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
from twosurfaces import function2D_graph2

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
            lambda x: x / 3 + 0
        )

        function1D_heatmap_1.center().shift(LEFT * 3.5 + DOWN * 1)


        graph, surface_graph, point1, point_bottom1, point_bottom_left1, triangle1_p1, triangle1_p2, triangle1_p3 = function2D_graph2(lambda x, y: x / 2 + 2.5)

        graph2, surface_graph2, point2, point_bottom2, point_bottom_left2,  triangle2_p1, triangle2_p2, triangle2_p3 = function2D_graph2(
            lambda x, y: -x / 4 + 2.5, 
            p1 = np.array([2, -1]),
            p2 = np.array([0, -1]), # shared bottom
            p3 = np.array([0, 2]) )

        surface_graph2.rotate(0.1, axis=[0, 0, 1], about_point=point2)

        #line_between_points = Line(point_bottom1, point_bottom2, stroke_width = 10, stroke_color = text_black)

        dot_point_bottom1 = Dot(point=point_bottom1, color=RED).set_opacity(0)
        dot_point_bottom2 = Dot(point=point_bottom_left1, color=BLUE).rotate(0.1, axis=[0, 0, 1], about_point=point2).set_opacity(0)

        triangle_outline = Polygon(triangle1_p1, triangle1_p3, triangle2_p1).set_stroke(text_black, 1.5)

        triangle_outline1 = Polygon(
            point2, 
            point_bottom1 - [0, -0.1, 0], 
            dot_point_bottom2.get_center() - [0, -0.1, 0]
            ).set_fill("#436f6d", 1).set_stroke("#436f6d", 1)

        
        """
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
        """

        label_head = (
            Tex("Independent", font_size=75)
            .scale(0.6)
            .set_color(text_black)
            .move_to([0, 3, 0])
        )

        all_2D = Group(
            function1D_heatmap_1,
            label_head,
        )

        """
        all_3D = Group(
            function2D_graph_1,
            graph
        )
        """
        # graph2.rotate(0.1, [0,0,1], about_point=surface_graph2.get_top())

        all_3D = Group(
            graph,
            graph2,
            triangle_outline1,
            triangle_outline,
            dot_point_bottom1,
            dot_point_bottom2
        ).center().shift(DOWN * 2.5 + RIGHT * 2.5)

        self.add(all_3D)
        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
        # self.add(NumberPlane())
