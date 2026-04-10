"""
TIME : 18:20 - 19:10

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 20: Reward fuction

Generate image by simple running script:
python ./figure20.py
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

        # Left triangle

        function1D_heatmap_1 = function1D_heatmap(
            lambda x: -x / 2 + 2,
            points=True,
        )

        function1D_heatmap_1.shift(LEFT * 6.5 + DOWN * 1)

        # Right graph
        function1D_graph_1 = function1D_graph(function=lambda x: -x / 2 + 2, function2=lambda x: (-x / 2 + 2)* 0.3)

        function1D_graph_1.shift(RIGHT * 4)

        # Left triangle scaled

        function1D_heatmap_2 = function1D_heatmap(
            lambda x: (-x / 2 + 2) * 0.3,
            points=True,
            x_label = r"t \cdot_T x",
            y_label = r"t \cdot_T y",
        )

        function1D_heatmap_2.shift(LEFT * 2 + DOWN * 1)

        # Right graph scaled
        #function1D_graph_2 = function1D_graph(function=lambda x: (-x / 2 + 2)* 0.3)

        #function1D_graph_2.shift(RIGHT * 4 + DOWN * 1)

        all_2D = (
            Group(
                function1D_heatmap_1,
                function1D_graph_1,
                function1D_heatmap_2,
            )
            .scale(0.9)
            .shift(UP * 0.6)
        )

        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
