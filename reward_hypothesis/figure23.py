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

        left_top = Group(
            function2D_graph_1,
            function2D_graph_2,
            )

        ##### TOP RIGHT GRAPH 22L

         # Bottom left graph 1 (GAMMA INDIFFERENT SCALED)
        function2D_graph_3 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_3.shift(RIGHT * 1.6).scale(0.65)

        # Bottom left graph 2 (GAMMA INDIFFERENT SCALED)
        function2D_graph_4 = function2D_graph(lambda x, y: (x / 2 + 2.5)*0.3, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_4.shift(RIGHT * 4.4).scale(0.65)

        right_top = Group(
            function2D_graph_3,
            function2D_graph_4,
            )

        ##### BOTTOM RIGHT GRAPH 21L

        # Bottom left graph 1 (Not Dynamically Consistent)
        function2D_graph_5 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_5.shift(RIGHT * 1.6).scale(0.65)

        # Bottom left graph 2 (Not Dynamically Consistent)
        function2D_graph_6 = function2D_graph(lambda x, y: -x / 3 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_6.shift(RIGHT * 4.4).scale(0.65)

        right_bot = Group(
            function2D_graph_5,
            function2D_graph_6,
            )

        ##### BOTTOM LEFT TEXT

        text1 = MathTex(r" \gamma - \text{Indifferent}", color = text_black).shift(UP * 0.7)
        text2 = MathTex(r"\Downarrow", color = text_black)
        text3 = MathTex(r"\text{Dynamically Consistent}", color = text_black).shift(DOWN * 0.7)

        text = Group(text1, text2, text3)

        # Table

        
        row1 = Tex(
            "Dynamically \\\\ Consistent", 
            color=text_black, 
            font_size=65
            ).scale(0.7).move_to([-5.6,1,0])

        row2 = Tex(
            "Not \\\\ Dynamically \\\\ Consistent", 
            color=text_black, 
            font_size=65
            ).scale(0.7).move_to([-5.6,-2,0])

        col1 = MathTex(
            r"\gamma - \textnormal{Indifferent}", 
            color=text_black, 
            font_size=65
            ).scale(0.7).move_to([-1.3,3,0])

        col2 = MathTex(
            r"\textnormal{Not} ~ \gamma - \textnormal{Indifferent}",
            color=text_black, 
            font_size=65
            ).scale(0.7).move_to([4.3,3,0])

        left_top.move_to([-1.3,1,0]).scale(0.85)
        right_top.move_to([4.3,1,0]).scale(0.85)
        text.move_to([-1.3,-2,0]).scale(0.7)
        right_bot.move_to([3.4,-4,0]).scale(0.65)

        line_row1 = Line([-4, 3.5, 0], [-4, -3.5,0], stroke_width = 3, stroke_color = text_black)
        line_row1.set_cap_style(CapStyleType.ROUND)

        line_row2 = Line([1.5, 3.5, 0], [1.5, -3.5,0], stroke_width = 3, stroke_color = text_black)
        line_row2.set_cap_style(CapStyleType.ROUND)

        line_col1 = Line([-7, 2.5, 0], [7, 2.5,0], stroke_width = 3, stroke_color = text_black)
        line_col1.set_cap_style(CapStyleType.ROUND)

        line_col2 = Line([-7, -0.5, 0], [7, -0.5,0], stroke_width = 3, stroke_color = text_black)
        line_col2.set_cap_style(CapStyleType.ROUND)
    
        all_3D = Group(
            function2D_graph_1,
            function2D_graph_2,
            function2D_graph_3,
            function2D_graph_4,
            function2D_graph_5,
            function2D_graph_6,
        )

        all_2D = Group(text, row1, row2, col1, col2, line_row1, line_row2, line_col1, line_col2)

        self.add(all_3D)
        #self.add_fixed_in_frame_mobjects(table)
        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
    