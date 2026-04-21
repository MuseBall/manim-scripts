"""
TIME : 11:20 - 11:55


Guille - Reward Hypothesis - Dovetail Project

Images for Section in Mixture space - Expected utility - Indepen-
dence and Continuity - vNM theorem
Figure 16: Constrained MDP and no independence

Generate image by simple running script:
python ./figure16.py
"""

from manim import *
import numpy as np
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
        node_pink ="#c78d9c"
        node_purple = "#b6b3c4"


        # background rectangle with rounded corners
        background_rectangle = RoundedRectangle(color = "#d6e2e2", fill_opacity = 1, corner_radius = 0.7, height = 8, width = 8)

     # Left graph
        function1D_heatmap_2 = function1D_heatmap(lambda x: 0 if x < 1 else x / 2)
        line2 = function1D_heatmap_2.graph.set_opacity(0)

        function1D_heatmap_2.shift(DOWN * 1.5 + LEFT * 4.5)

        graph, surface_graph, point1, point_bottom1, point_bottom_left1, triangle1_p1, triangle1_p2, triangle1_p3 = function2D_graph2(lambda x, y: 0)

        graph2, surface_graph2, point2, point_bottom2, point_bottom_left2,  triangle2_p1, triangle2_p2, triangle2_p3 = function2D_graph2(
            lambda x, y: -x / 4 + 2.5, 
            p1 = np.array([2, -1]),
            p2 = np.array([0, -1]), # shared bottom
            p3 = np.array([0, 2]) )

        surface_graph.shift(DOWN * 4)

        """
        # Left graph
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

        # Right dots
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
        """

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
            Tex("Constrained MDP", font_size=75)
            .scale(0.6)
            .set_color(text_black)
            .move_to([0, 3, 0])
        )

        all_2D = Group(
            function1D_heatmap_2,
            label_right,
        )
        all_3D = Group(
            graph,
            graph2
        ).shift(DOWN * 1 + RIGHT * 2).scale(0.8)

        self.add(all_3D)
        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
        # self.add(NumberPlane())
