"""
TIME : 20:40 - 21:10

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 22: gamma - indifference

Generate image by simple running script:
python ./figure22.py
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


        # Bottom right graph 1 (NOT GAMMA INDIFFERENT)
        function2D_graph_1 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_1.shift(LEFT * 4.4).scale(0.65)

        # Bottom right graph 2 (NOT GAMMA INDIFFERENT)
        function2D_graph_2 = function2D_graph(lambda x, y: x / 2 + 1.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_2.shift(LEFT * 1.6).scale(0.65)

        # Bottom left graph 1 (GAMMA INDIFFERENT SCALED)
        function2D_graph_3 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_3.shift(RIGHT * 1.6).scale(0.65)

        # Bottom left graph 2 (GAMMA INDIFFERENT SCALED)
        function2D_graph_4 = function2D_graph(lambda x, y: (x / 2 + 2.5)*0.3, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_4.shift(RIGHT * 4.4).scale(0.65)

        label_left = (
            MathTex(r"\textnormal{Not}~\gamma -\textnormal{Indifferent}", font_size=70, stroke_width = 1.5)
            .scale(0.6)
            .set_color(text_black)
            .move_to([-3.5, 2.5, 0])
        )

        label_right = (
            MathTex(r"\gamma -\textnormal{Indifferent}", font_size=70, stroke_width = 1.5)
            .scale(0.6)
            .set_color(text_black)
            .move_to([3.5, 2.5, 0])
        )

        all_3D = Group(
            function2D_graph_1,
            function2D_graph_2,
            function2D_graph_3,
            function2D_graph_4,
        ).shift(DOWN * 2.5)

        labels = Group(
            label_left,
            label_right,
            )

        #all_ = Group(all_3D).center()

        self.add(all_3D)
        self.add_fixed_in_frame_mobjects(labels)
        #self.add_fixed_in_frame_mobjects(all_2D, labels, NumberPlane())
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
        #self.add(NumberPlane())
        
