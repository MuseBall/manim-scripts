"""
TIME : 17:10 - 18:15

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Set - Order representation - Preorder and Debreu separable - Debreu-Fishburns theorem
Figure 9: Lexicographical linearization: asymptotic

Generate image by simple running script:
python ./figure9.py
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

        labels_axes = axes.get_axis_labels(MathTex("", color = text_black, stroke_width = 1.5).scale(0.8), MathTex("1", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes[1].next_to(axes.get_y_axis().get_top(), UP)

    # Points in graph

        point_0 = axes.coords_to_point(0, 0)
        point_1e = axes.coords_to_point(0, 0.7)
        point_1ek = axes.coords_to_point(0, 1.4)
        point_1 = axes.coords_to_point(0.7, 0)
        point_2 = axes.coords_to_point(1.4, 0)

        dot_0 = Dot(point_0, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_1e = Dot(point_1e, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_1ek = Dot(point_1ek, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_1 = Dot(point_1, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_2 = Dot(point_2, color = node_purple, stroke_color = text_black, stroke_width = 1)

        label_0 = MathTex("0", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_0, LEFT).shift(DOWN * 0.2)
        label_1e = MathTex(r"1 - \frac{1}{e}", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_1e, LEFT)
        label_1ek = MathTex(r"1-e^{-k}", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_1ek, LEFT)
        label_1 = MathTex("1", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_1, UP)
        label_2 = MathTex("2>1", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_2, UP)

        bracket = MathTex(r"\{", font_size = 65).scale(1).set_color(text_black).next_to(dot_0, UP).rotate(-PI/2).shift(LEFT * 3.25 + DOWN * 0.13)

        epsilon = MathTex(r"\epsilon", font_size = 60).scale(0.6).set_color(text_black).next_to(bracket, UP).shift(DOWN * 0.13)

        ellipsis = MathTex(rf"\vdots", font_size = 60).scale(0.6).set_color(text_black).next_to(label_1ek, UP).shift(UP * 0.1)


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

        point_00 = sub_axes.coords_to_point(0.5, 0)
        point_0k = sub_axes.coords_to_point(1.5, 0)
        point_0e0 = sub_axes.coords_to_point(2.5, 0)
        point_10 = sub_axes.coords_to_point(3.5, 0)
        point_sub1 = sub_axes.coords_to_point(0,1.5)
        point_sub2 = sub_axes.coords_to_point(0,3)

        dot_00 = Dot(point_00, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_0k = Dot(point_0k, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_0e0 = Dot(point_0e0, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_10 = Dot(point_10, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_sub1 = Dot(point_sub1, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_sub2 = Dot(point_sub2, color = node_green, stroke_color = text_black, stroke_width = 1)

        label_00 = MathTex("(0,0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_00, DOWN)
        label_0k = MathTex("(0,k)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_0k, DOWN)
        label_0e0 = MathTex("(0+\epsilon, 0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_0e0, DOWN)
        label_10 = MathTex("(1,0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_10, DOWN)
        label_sub1 = MathTex("1", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_sub1, LEFT)
        label_sub2 = MathTex("2", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_sub2, LEFT)

    # Curve in sub-graph
        arc = ArcBetweenPoints(start = point_00 , end = point_0e0 + UP * 0.7, radius= -2.5, color = text_black, stroke_width = 3).shift(UP * 0.05)

    # Lines in Sub-graph
        line_0k = DashedLine(point_0k + UP * 0.6, point_0k, dash_length=0.15, color=text_black, stroke_width=3)
        line_0e0 = DashedLine(point_0e0 + UP * 1.8, point_0e0, dash_length=0.15, color=text_black, stroke_width=3)
        line_10 = DashedLine(point_10 + UP * 1.8, point_10, dash_length=0.15, color=text_black, stroke_width=3)

        line_sub1 = DashedLine(point_sub1, point_sub1 + RIGHT * 3, dash_length=0.15, color=text_black, stroke_width=3)
        line_sub2 = DashedLine(point_sub2, point_sub2 + RIGHT * 3, dash_length=0.15, color=text_black, stroke_width=3)

        label_line_10 = MathTex("?", font_size = 50).scale(0.6).set_color(text_black).next_to(line_10, UP).set_opacity(0)

        self.add(arc, line_0k, line_0e0, line_10, line_sub1, line_sub2, sub_axes, sub_labels, dot_00, label_00, dot_0k, label_0k, dot_0e0, label_0e0, dot_10, label_10, label_line_10, dot_sub1, dot_sub2, label_sub1, label_sub2, bracket, epsilon)


    #Lines in graph

        #line_AB = DashedLine(point_A + UP * 2, point_B + DOWN * 5, dash_length=0.15, color=text_black, stroke_width=3)
        #line_C = DashedLine(point_C + UP * 4.3, point_C + DOWN * 1.8, dash_length=0.15, color=text_black, stroke_width=3)

        label = MathTex("x \succeq y \succeq z", font_size = 70, stroke_width = 2).set_color(text_black).next_to(axes, DOWN * 2).set_opacity(0)


        all_objects = VGroup(axes, dot_0, dot_1e, dot_1ek, dot_1, dot_2, labels_axes, label_0, label_1e, label_1ek, label_1, label_2, label, ellipsis).center().scale(0.8)
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
