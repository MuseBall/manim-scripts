"""
TIME : 20:40 - 21:50

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

        ##### TOP LEFT GRAPH 22R

        # Bottom right graph 1 (NOT GAMMA INDIFFERENT)
        function2D_graph_1 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_1.shift(LEFT * 4.4).scale(0.65)

        # Bottom right graph 2 (NOT GAMMA INDIFFERENT)
        function2D_graph_2 = function2D_graph(lambda x, y: x / 2 + 1.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_2.shift(LEFT * 1.6).scale(0.65)

        left_top_graphs = Group(
            function2D_graph_1,
            function2D_graph_2,
            )

        left_top = self.add(left_top_graphs).set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)


        ##### TOP RIGHT GRAPH 22L

         # Bottom left graph 1 (GAMMA INDIFFERENT SCALED)
        function2D_graph_3 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_3.shift(RIGHT * 1.6).scale(0.65)

        # Bottom left graph 2 (GAMMA INDIFFERENT SCALED)
        function2D_graph_4 = function2D_graph(lambda x, y: (x / 2 + 2.5)*0.3, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_4.shift(RIGHT * 4.4).scale(0.65)

        right_top_graphs = Group(
            function2D_graph_3,
            function2D_graph_4,
            )

        right_top = self.add(right_top_graphs).set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)

        ##### BOTTOM RIGHT GRAPH 21L

        # Bottom left graph 1 (Not Dynamically Consistent)
        function2D_graph_5 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_5.shift(RIGHT * 1.8).scale(0.65)

        # Bottom left graph 2 (Not Dynamically Consistent)
        function2D_graph_6 = function2D_graph(lambda x, y: -x / 3 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_6.shift(RIGHT * 0.9).scale(0.65)

        right_bot_graph = Group(
            function2D_graph_5,
            function2D_graph_6,
            )

        right_bot = self.add(right_bot_graph).set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)

        ##### BOTTOM LEFT TEXT

        text1 = MathTex(r" \gamma - \text{Indifferent}", color = text_black).shift(UP * 0.7)
        text2 = MathTex(r"\Downarrow", color = text_black)
        text3 = MathTex(r"\text{Dynamically Consistent}", color = text_black).shift(DOWN * 0.7)

        text = Group(text1, text2, text3)

    # Table

        table = Table(
            [[left_top, right_top], [text, right_bot]],
            row_labels=[
                Tex("Dynamically \\\\ Consistent", color=text_black, font_size=65),
                Tex("Not \\\\ Dynamically \\\\ Consistent", color=text_black, font_size=65),
            ],
            col_labels=[
                MathTex(r"\gamma - \textnormal{Indifferent}", color=text_black, font_size=65),
                MathTex(r"\textnormal{Not} ~ \gamma - \textnormal{Indifferent}", color=text_black, font_size=65),
            ],
            element_to_mobject=lambda m: m,
        )

        table.scale(0.69).center()
        table.get_horizontal_lines().set_color(text_black)
        table.get_vertical_lines().set_color(text_black)

        all_3D = Group(
            function2D_graph_1,
            function2D_graph_2,
            function2D_graph_3,
            function2D_graph_4,
            function2D_graph_5,
            function2D_graph_6,
        )

        #self.add(all_3D)
        self.add_fixed_in_frame_mobjects(table)
        #self.add_fixed_in_frame_mobjects(all_2D, labels, NumberPlane())
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
