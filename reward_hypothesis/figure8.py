"""
TIME : 16:50 - 17:20
        15:40 - 17:00

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Set - Order representation - Preorder and Debreu separable - Debreu-Fishburns theorem
Figure 8: Lexicographical linearization: infinity. 

Generate image by simple running script:
python ./figure8.py
"""

from manim import *
import numpy as np


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

        axes = Axes(x_range =[-1.5,3.5], y_range = [-3,3], x_length= 8, y_length = 7, x_axis_config={"include_numbers": False, "include_ticks": False}, y_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": StealthTip, "color": text_black}).move_to([4,0,0])

        labels_axes = axes.get_axis_labels(MathTex("w_a", color = text_black, stroke_width = 1.5).scale(0.8), MathTex("w_p", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes[0].next_to(axes.get_x_axis().get_right(), RIGHT)
        labels_axes[1].next_to(axes.get_y_axis().get_top(), UP)

    # Points in graph

        point_0 = axes.coords_to_point(0, 0)
        point_1 = axes.coords_to_point(0, 1)
        point_k = axes.coords_to_point(0, 1.7)
        point_inf = axes.coords_to_point(1, 0)

        dot_0 = Dot(point_0, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_1 = Dot(point_1, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_k = Dot(point_k, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_inf = Dot(point_inf, color = node_purple, stroke_color = text_black, stroke_width = 1)

        label_0 = MathTex("0", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_0, LEFT).shift(UP * 0.2)
        label_1 = MathTex("1", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_1, LEFT)
        label_k = MathTex("K", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_k, LEFT)
        label_inf = MathTex("?> \infty", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_inf, UP)

        ellipsis = MathTex(rf"\vdots", font_size = 60).scale(0.6).set_color(text_black).next_to(label_k, UP).shift(UP * 0.1)

        infinity = MathTex(rf"\infty", font_size = 60).scale(0.6).set_color(text_black)
        infinity.next_to(axes.get_y_axis().get_top(), LEFT).shift(DOWN * 0.3 + LEFT *0.1)

    # Sub-Graph

        sub_axes = Axes(
            x_range=[-0.3, 4],
            y_range=[-0.3, 4.5],
            x_length=4,
            y_length=2.5,
            x_axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
            axis_config={"tip_shape": StealthTip, "color": text_black})

        sub_axes.move_to(axes.coords_to_point(0.1, -0.1)).shift(DOWN * 1.2 + LEFT * 1.5)

    # Sub-Graph Labels
        sub_labels = sub_axes.get_axis_labels(
            MathTex("X", color=text_black, stroke_width = 1.2).scale(0.6),
            MathTex("\mathbb{R}", color=text_black, stroke_width = 1.2).scale(0.6))
        sub_labels[0].next_to(sub_axes.get_x_axis().get_right(), RIGHT)
        sub_labels[1].next_to(sub_axes.get_y_axis().get_top(), LEFT).shift(DOWN * 0.2)

    # Sub-Graph Points

        point_00 = sub_axes.coords_to_point(0, 0)
        point_0k = sub_axes.coords_to_point(1, 0)
        point_0e0 = sub_axes.coords_to_point(2, 0)
        point_10 = sub_axes.coords_to_point(3, 0)

        dot_00 = Dot(point_00, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_0k = Dot(point_0k, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_0e0 = Dot(point_0e0, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_10 = Dot(point_10, color = node_green, stroke_color = text_black, stroke_width = 1)

        label_00 = MathTex("(0,0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_00, DOWN)
        label_0k = MathTex("(0,k)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_0k, DOWN)
        label_0e0 = MathTex("(0+\epsilon, 0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_0e0, DOWN)
        label_10 = MathTex("(1,0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_10, DOWN)

    # Curve in sub-graph
        arc = ArcBetweenPoints(start = point_00 , end = point_0e0 + UP * 1.5 + LEFT * 0.1, radius= 1.7, color = text_black, stroke_width = 3).shift(UP * 0.05)

    # Lines in Sub-graph
        line_0k = DashedLine(point_0k + UP * 0.22, point_0k, dash_length=0.15, color=text_black, stroke_width=3)
        line_0e0 = DashedLine(point_0e0 + UP * 1.8, point_0e0, dash_length=0.15, color=text_black, stroke_width=3)
        line_10 = DashedLine(point_10 + UP * 1.8, point_10, dash_length=0.15, color=text_black, stroke_width=3)

        label_line_10 = MathTex("?", font_size = 50).scale(0.6).set_color(text_black).next_to(line_10, UP)

        self.add(arc, line_0k, line_0e0, line_10, sub_axes, sub_labels, dot_00, label_00, dot_0k, label_0k, dot_0e0, label_0e0, dot_10, label_10, label_line_10)


    #Lines in graph

        #line_AB = DashedLine(point_A + UP * 2, point_B + DOWN * 5, dash_length=0.15, color=text_black, stroke_width=3)
        #line_C = DashedLine(point_C + UP * 4.3, point_C + DOWN * 1.8, dash_length=0.15, color=text_black, stroke_width=3)

        label = MathTex("x \succeq y \succeq z", font_size = 70, stroke_width = 2).set_color(text_black).next_to(axes, DOWN * 2).set_opacity(0)


        all_objects = VGroup(axes, dot_0, dot_1, dot_k, dot_inf, label_inf, labels_axes, label_0, label_1, label_k, label, ellipsis, infinity).center().scale(0.8)
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
