"""
TIME : 10:30 - 11:30
        15:50 - 17:30

        11:45 - 12:15


Guille - Reward Hypothesis - Dovetail Project

Images for Section in Mixture space - Expected utility - Indepen-
dence and Continuity - vNM theorem
Figure 14: Expected utility

Generate image by simple running script:
python ./figure14.py
"""

import numpy as np
from manim import *
from nodes_and_arrows import make_arrow
from plttriangle import (
    function1D_graph,
    function1D_heatmap,
    function2D_graph,
    function2D_heatmap,
)

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
            lambda x: -x / 2 + 2,
            points=True,
        )

        function1D_heatmap_1.shift(UP * 1 + LEFT * 4)

        # Top right graph
        function1D_graph_1 = function1D_graph(function=lambda x: -x / 2 + 2)

        function1D_graph_1.shift(UP * 2 + RIGHT * 3)

        # Botoom left graph
        function2D_heatmap_1 = function2D_heatmap(
            lambda x, y: 1 / 2 * x + 1,
            points=True,
        )

        function2D_heatmap_1.shift(DOWN * 2.4 + LEFT * 3).scale(0.9)

        # Bottom right graph
        function2D_graph_1 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True)

        function2D_graph_1.shift(DOWN * 3.4 + RIGHT * 2.5).scale(0.7)

        label_right = (
            MathTex(r"x \succeq y", font_size=70)
            .scale(0.6)
            .set_color(text_black)
            .move_to([-3, -4, 0])
        )

        label_left = (
            MathTex(r"f(x) \geq f(y)", font_size=70)
            .scale(0.6)
            .set_color(text_black)
            .move_to([3.2, -3.7, 0])
        )

        label_left_1 = (
            MathTex(r"f(\sum_i p_i x_i) = \sum_i p_i f(x_i)", font_size=70)
            .scale(0.6)
            .set_color(text_black)
            .move_to([3.5, -4.5, 0])
        )

        label_mid = (
            MathTex(r"\Longleftrightarrow", font_size=100)
            .scale(0.6)
            .set_color(text_black)
            .move_to([0, -4, 0])
        )

        all_2D = (
            Group(
                function1D_heatmap_1,
                function1D_graph_1,
                function2D_heatmap_1,
                label_right,
                label_left,
                label_left_1,
                label_mid,
            )
            .scale(0.9)
            .shift(UP * 0.6)
        )
        all_3D = Group(
            function2D_graph_1,
        )

        self.add(all_3D)
        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
        # self.add(NumberPlane())
