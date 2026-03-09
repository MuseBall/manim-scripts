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


config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = config.pixel_height / config.pixel_width * config.frame_width


class Graph(Scene):
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

    #Axes

        axes = Axes(x_range =[-1.5,3.5], x_length= 2.5, tips = False, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": None, "color": text_black})

        axes.y_axis.set_opacity(0)

        labels_axes = axes.get_axis_labels(MathTex(r"(\mathbb{R}, >)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes[0].set_opacity(0)
        labels_axes[1].set_opacity(0)

    # Points in graph

        point_x = axes.coords_to_point(-1.5, 0)
        point_y = axes.coords_to_point(3.5, 0)

        dot_x = Dot(point_x, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y = Dot(point_y, color = node_purple, stroke_color = text_black, stroke_width = 1)

        label_x = MathTex(r"t \cdot_T x", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_x, DOWN)
        label_y = MathTex(r"t \cdot_T y", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_y, DOWN)


    # Triangle

        triangle_1 = Polygon(
            [-1, 0.1, 0],
            [-1, 0.3, 0],
            [1, 0.1, 0],
            color = node_blue, fill_opacity = 1).set_stroke(text_black, 2).set_sheen(0.5, RIGHT)

    #Axes 2

        axes2 = Axes(x_range =[-1.5,3.5], x_length= 2.5, tips = False, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": None, "color": text_black})

        axes2.y_axis.set_opacity(0)

        labels_axes2 = axes2.get_axis_labels(MathTex(r"(\mathbb{R}, >)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes2[0].set_opacity(0)
        labels_axes2[1].set_opacity(0)

    # Points in graph 2

        point_x2 = axes2.coords_to_point(-1.5, 0)
        point_y2 = axes2.coords_to_point(3.5, 0)

        dot_x2 = Dot(point_x, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y2 = Dot(point_y, color = node_purple, stroke_color = text_black, stroke_width = 1)

        label_x2 = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_x2, DOWN)
        label_y2 = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_y2, DOWN)


    # Triangle 2

        triangle_2 = Polygon(
            [-1, 0.1, 0],
            [-1, 0.7, 0],
            [1, 0.1, 0],
            color = node_blue, fill_opacity = 1).set_stroke(text_black, 2).set_sheen(0.5, RIGHT)

    # Axes

        axes_1 = Axes(x_range =[-0.5,6], y_range = [-0.5,4], x_length= 6, y_length = 4, x_axis_config={"include_numbers": False, "include_ticks": False}, y_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": StealthTip, "color": text_black})

        labels_axes_1 = axes_1.get_axis_labels(MathTex("X", color = text_black, stroke_width = 1.5).scale(0.8), MathTex(r"f(x) \in \mathbb{R}", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes_1[0].next_to(axes_1.get_x_axis().get_right(), RIGHT)
        labels_axes_1[1].next_to(axes_1.get_y_axis().get_top(), UP)

    # Points in graph

        point_x_1 = axes_1.coords_to_point(0.5, 2)
        point_y_1 = axes_1.coords_to_point(2, 1.1)

        point_tx_1 = axes_1.coords_to_point(3, 1.3)
        point_ty_1 = axes_1.coords_to_point(4.5, 1.1)

        dot_x_1 = Dot(point_x_1, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y_1 = Dot(point_y_1, color = node_purple, stroke_color = text_black, stroke_width = 1)

        dot_tx_1 = Dot(point_tx_1, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_ty_1 = Dot(point_ty_1, color = node_purple, stroke_color = text_black, stroke_width = 1)

        linexy_1 = Line(point_x_1, point_y_1, color = text_black, stroke_width = 3)
        linetxy_1 = Line(point_tx_1, point_ty_1, color = text_black, stroke_width = 3)

        line_x_1 = DashedLine(point_x_1, point_x_1  + DOWN * 1.7, dash_length=0.15, color="#739b99", stroke_width=3)
        line_y_1 = DashedLine(point_y_1, point_y_1 + DOWN * 0.9, dash_length=0.15, color="#739b99", stroke_width=3)

        line_tx_1 = DashedLine(point_tx_1, point_tx_1  + DOWN * 1.1, dash_length=0.15, color="#739b99", stroke_width=3)
        line_ty_1 = DashedLine(point_ty_1, point_ty_1 + DOWN * 0.9, dash_length=0.15, color="#739b99", stroke_width=3)

        label_x_1 = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(line_x_1, DOWN)
        label_y_1 = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(line_y_1, DOWN)

        label_tx_1 = MathTex(r"t \cdot_T x", font_size = 60).scale(0.6).set_color(text_black).next_to(line_tx_1, DOWN)
        label_ty_1 = MathTex(r"t \cdot_T y", font_size = 60).scale(0.6).set_color(text_black).next_to(line_ty_1, DOWN)

        triangle_right_top = VGroup(axes, dot_x, dot_y, labels_axes, label_x, label_y, triangle_1).to_edge(UL).shift(RIGHT * 3)

        triangle_right_top2 = VGroup(axes2, dot_x2, dot_y2, labels_axes2, label_x2, label_y2, triangle_2).to_edge(UL)

        graph_left_top = VGroup(linexy_1, axes_1, labels_axes_1, dot_x_1, dot_y_1, label_x_1, label_y_1, line_x_1, line_y_1, linetxy_1, dot_tx_1, dot_ty_1, label_tx_1, label_ty_1, line_tx_1, line_ty_1).to_edge(RIGHT)

        self.add(triangle_right_top, triangle_right_top2, graph_left_top)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
