"""
TIME : 19:20 - 20:30

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 21: Dynamic Consistencies

Generate image by simple running script:
python ./figure21.py
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

        # Top left graph 1 (Not Dynamically Consistent)

        function1D_heatmap_1 = function1D_heatmap(
            lambda x: -x / 2 + 2,
            points=False,
        )

        function1D_heatmap_1.shift(UP * 1 + LEFT * 6.5)

        # Top left graph 2 (Not Dynamically Consistent)

        function1D_heatmap_2 = function1D_heatmap(
            lambda x: x / 3 + 0,
            points=False,
            a=0,
            b=4
        )

        function1D_heatmap_2.shift(UP * 1 + LEFT * 3)

        # Top right graph 1 (Dynamically Consistent)

        function1D_heatmap_3 = function1D_heatmap(
            lambda x: -x / 2 + 2,
            points=False,
        )

        function1D_heatmap_3.shift(UP * 1 + RIGHT * 1.5)

        # Top right graph 2 (Dynamically Consistent)

        function1D_heatmap_4 = function1D_heatmap(
            lambda x: -x / 3 + 1.5 ,
            points=False,
        )

        function1D_heatmap_4.shift(UP * 1 + RIGHT * 5)

        # Bottom left graph 1 (Not Dynamically Consistent)
        function2D_graph_1 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_1.move_to(function1D_heatmap_1.get_bottom() + DOWN * 3.5 + RIGHT * 1.8).scale(0.6)

        # Bottom left graph 2 (Not Dynamically Consistent)
        function2D_graph_2 = function2D_graph(lambda x, y: -x / 3 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_2.move_to(function1D_heatmap_2.get_bottom() + DOWN * 3.6 + RIGHT * 0.9).scale(0.6)

        # Bottom right graph 1 (Dynamically Consistent)
        function2D_graph_3 = function2D_graph(lambda x, y: x / 2 + 2.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_3.move_to(function1D_heatmap_3.get_bottom() + DOWN * 3.5 + LEFT * 0.9).scale(0.6)

        # Bottom right graph 2 (Dynamically Consistent)
        function2D_graph_4 = function2D_graph(lambda x, y: x / 2 + 1.5, points=True, x_label="", y_label="", z_label = "")

        function2D_graph_4.move_to(function1D_heatmap_4.get_bottom() + DOWN * 3.6 + LEFT * 1.8).scale(0.6)

        label_left = (
            Tex("Not Dynamically Consistent", font_size=70, stroke_width = 1.5)
            .scale(0.6)
            .set_color(text_black)
            .move_to([-3.5, 2.5, 0])
        )

        label_right = (
            Tex("Dynamically Consistent", font_size=70, stroke_width = 1.5)
            .scale(0.6)
            .set_color(text_black)
            .move_to([3.5, 2.5, 0])
        )


        all_2D = (
            Group(
                function1D_heatmap_1,
                function1D_heatmap_2,
                function1D_heatmap_3,
                function1D_heatmap_4,
            )
            .scale(0.9)
            .shift(UP * 0.6)
        )


        all_3D = Group(
            function2D_graph_1,
            function2D_graph_2,
            function2D_graph_3,
            function2D_graph_4,
        )

        labels = Group(
            label_left,
            label_right,
            )

        all_ = Group(all_2D, all_3D).center().shift(DOWN * 3)

        self.add(all_3D)
        self.add_fixed_in_frame_mobjects(all_2D, labels)
        #self.add_fixed_in_frame_mobjects(all_2D, labels, NumberPlane())
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
        #self.add(NumberPlane())
