"""
TIME : 17:00 - 17:50

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 20: Reward fuction

Generate image by simple running script:
python ./figure20_2.py
"""

from manim import *
import numpy as np
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
        node_pink ="#c78d9c"
        node_purple = "#b6b3c4"


        # background rectangle with rounded corners

        background_rectangle = RoundedRectangle(color = "#d6e2e2", fill_opacity = 1, corner_radius = 0.7, height = 8, width = 8)

        # Left graph
        function2D_heatmap_1 = function2D_heatmap(
            lambda x, y: 1 / 2 * x + 1,
            points=True,
        )

        function2D_heatmap_1.shift(LEFT * 5 + DOWN * 1).scale(0.9)

        # Right graph
        function2D_graph_1 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label = r"t \cdot_T x", y_label = r"t \cdot_T y", z_label = r"t \cdot_T z")

        function2D_graph_1.shift(RIGHT * 2.5 + DOWN * 1).scale(0.6)

        # Left graph scaled
        function2D_heatmap_2 = function2D_heatmap(
            lambda x, y: (1 / 2 * x + 1) * 1.3,
            points=True,
            x_label = r"t \cdot_T x", y_label = r"t \cdot_T y", z_label = r"t \cdot_T z"
        )

        function2D_heatmap_2.shift(LEFT * 0.7 + DOWN * 1).scale(0.9)

        # Right graph scaled
        function2D_graph_2 = function2D_graph(lambda x, y: (x / 2 + 2.5)*1.3, points=True)

        function2D_graph_2.shift(RIGHT * 5.4 + DOWN * 1.3).scale(0.6)

        
        all_2D = (
            Group(
                function2D_heatmap_1,
                function2D_heatmap_2,
            )
            .scale(0.9)
        )
        all_3D = Group(
            function2D_graph_1,
            function2D_graph_2
        )

        all_ = Group(all_2D, all_3D).center().shift(RIGHT * 0.6)

        self.add(all_3D)
        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
        # self.add(NumberPlane())


