"""
TIME : 19:00 - 19:20
       10:50 - 12:40
       14:10 - 14:40

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Set - Order representation - Preorder and Debreu separable - Debreu-Fishburns theorem
Figure 10: Lexicographical linearization: uncountable filled intervals

Generate image by simple running script:
python ./figure10.py
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
        point_2 = axes.coords_to_point(2, 0)

        dot_0 = Dot(point_0, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_1e = Dot(point_1e, color = node_purple, stroke_color = text_black, stroke_width = 1).set_opacity(0)
        dot_1ek = Dot(point_1ek, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_1 = Dot(point_1, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_2 = Dot(point_2, color = node_purple, stroke_color = text_black, stroke_width = 1)

        label_0 = MathTex("0", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_0, LEFT).shift(DOWN * 0.2)
        label_1e = MathTex(r"1 - \frac{1}{e}", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_1e, LEFT).set_opacity(0)
        label_1ek = MathTex(r"1-e^{-k}", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_1ek, LEFT)
        label_1 = MathTex("1", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_1, UP)
        label_2 = MathTex("2", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_2, UP)

        bracket = MathTex(r"\{", font_size = 65).scale(1).set_color(text_black).next_to(dot_0, UP).rotate(-PI/2).shift(RIGHT * 0.5 + DOWN * 0.4).scale(1.2)

        epsilon = MathTex(r"\epsilon", font_size = 60).scale(0.6).set_color(text_black).next_to(bracket, UP).shift(DOWN * 0.13).scale(1.2)

        ellipsis = MathTex(rf"\vdots", font_size = 60).scale(0.6).set_color(text_black).next_to(label_1ek, UP).shift(UP * 0.1)

    # Lines through the main graph
        line_11 = DashedLine(point_1 + UP * 0.1, point_1  + DOWN * 2.5, dash_length=0.15, color="#739b99", stroke_width=3)
        line_11_2 = DashedLine(point_1 + UP * 0.85, point_1 + UP * 2.5, dash_length=0.15, color="#739b99", stroke_width=3)
        
        line_12 = DashedLine(point_1 + RIGHT * 0.4 + UP * 2.5, point_1 + RIGHT * 0.4 + DOWN * 2.5, dash_length=0.15, color="#739b99", stroke_width=3)
        


        line_13 = DashedLine(point_1 + RIGHT * 0.85 + UP * 2.5, point_1 + RIGHT * 0.85 + DOWN * 2.5, dash_length=0.15, color="#739b99", stroke_width=3)
        line_14 = DashedLine(point_1 + RIGHT * 1.3 + UP * 2.5, point_1 + RIGHT * 1.3 + DOWN * 2.5, dash_length=0.15, color="#739b99", stroke_width=3)

        line_12_label = MathTex(rf"1 + \delta", font_size = 60).scale(0.6).set_color(text_black).next_to(line_12, UP)

        ellipsis_1 = MathTex(rf"\dots", font_size = 60).scale(0.6).set_color("#739b99").next_to(line_14, RIGHT).shift(UP * 1.3)


    # Sub-Graph

        sub_axes = Axes(
            x_range=[-0.3, 6],
            y_range=[-0.3, 4.5],
            x_length=6.5,
            y_length=4,
            x_axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
            axis_config={"tip_shape": StealthTip, "color": text_black})

        sub_axes.move_to(axes.coords_to_point(0.1, -0.1)).shift(DOWN * 1.2 + RIGHT * 1.2)

    # Sub-Graph Labels
        sub_labels = sub_axes.get_axis_labels(
            MathTex("X", color=text_black, stroke_width = 1.2).scale(0.6),
            MathTex("\mathbb{R}", color=text_black, stroke_width = 1.2).scale(0.6))
        sub_labels[0].next_to(sub_axes.get_x_axis().get_right(), RIGHT)
        sub_labels[1].next_to(sub_axes.get_y_axis().get_top(), LEFT).shift(DOWN * 0.2)

    # Sub-Graph Points

        point_00 = sub_axes.coords_to_point(0.2, 0)
        point_0e0 = sub_axes.coords_to_point(1.2, 0)
        point_02e0 = sub_axes.coords_to_point(2.4, 0)
        point_1e0 = sub_axes.coords_to_point(4.2, 0)
        point_10 = sub_axes.coords_to_point(5.2, 0)
        point_sub1 = sub_axes.coords_to_point(0,1)
        point_sub2 = sub_axes.coords_to_point(0,3.7)

        point_sub11 = sub_axes.coords_to_point(0,1.7)
        point_sub12 = sub_axes.coords_to_point(0,2.4)

        dot_00 = Dot(point_00, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_02e0 = Dot(point_02e0, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_0e0 = Dot(point_0e0, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_1e0 = Dot(point_1e0, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_10 = Dot(point_10, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_sub1 = Dot(point_sub1, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_sub2 = Dot(point_sub2, color = node_green, stroke_color = text_black, stroke_width = 1)

        dot_sub11 = Dot(point_sub11, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_sub12 = Dot(point_sub12, color = node_green, stroke_color = text_black, stroke_width = 1)

        label_00 = MathTex("(0,0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_00, DOWN)
        label_02e0 = MathTex("(0+2 \epsilon,0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_02e0, DOWN)
        label_0e0 = MathTex("(0+\epsilon, 0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_0e0, DOWN)
        label_1e0 = MathTex("(1-\epsilon,0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_1e0, DOWN)
        label_10 = MathTex("(1,0)", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_10, DOWN)
        label_sub1 = MathTex("1", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_sub1, LEFT)
        label_sub2 = MathTex("2", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_sub2, LEFT)

        ellipsis_sub = MathTex("\dots", font_size = 50).scale(0.6).set_color(text_black).next_to(label_02e0, RIGHT).shift(LEFT * 0.1)

        label_sub11 = MathTex(rf"1 + \delta", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_sub11, LEFT)
        label_sub12 = MathTex(rf"1+ 2 \delta", font_size = 50).scale(0.6).set_color(text_black).next_to(dot_sub12, LEFT)

    # Curve in sub-graph
        arc1 = ArcBetweenPoints(start = point_00 , end = point_0e0 + UP * 0.8, radius= -1, color = text_black, stroke_width = 3).shift(UP * 0.05)
        arc2 = ArcBetweenPoints(start = point_0e0 + UP * 0.8, end = point_02e0 + UP * 1.35, radius= -1, color = text_black, stroke_width = 3).shift(UP * 0.05)
        arc3 = ArcBetweenPoints(start = point_1e0 + UP * 2, end = point_10 + UP * 3, radius= -1, color = text_black, stroke_width = 3).shift(UP * 0.05)

    # Lines in Sub-graph
        line_02e0 = DashedLine(point_02e0 + UP * 3, point_02e0, dash_length=0.15, color="#739b99", stroke_width=3)
        line_0e0 = DashedLine(point_0e0 + UP * 3, point_0e0, dash_length=0.15, color="#739b99", stroke_width=3)
        line_1e0 = DashedLine(point_1e0 + UP * 3, point_1e0, dash_length=0.15, color="#739b99", stroke_width=3)
        line_10 = DashedLine(point_10 + UP * 3, point_10, dash_length=0.15, color="#739b99", stroke_width=3)

        line_sub1 = DashedLine(point_sub1, point_sub1 + RIGHT * 5.5, dash_length=0.15, color="#739b99", stroke_width=3)

        line_sub11 = DashedLine(point_sub11, point_sub11 + RIGHT * 5.5, dash_length=0.15, color="#739b99", stroke_width=3)

        line_sub12 = DashedLine(point_sub12, point_sub12 + RIGHT * 5.5, dash_length=0.15, color="#739b99", stroke_width=3)

        line_sub2 = DashedLine(point_sub2, point_sub2 + RIGHT * 5.5, dash_length=0.15, color="#739b99", stroke_width=3)

        label_ellipsis = MathTex(rf"\vdots", font_size = 50).scale(0.6).set_color(text_black).next_to(label_sub12, UP).shift(RIGHT * 0.3)

        sub_graph = VGroup(label_sub11, label_sub12, line_02e0, line_0e0, line_10, line_sub1, line_sub2,line_1e0, sub_axes, sub_labels, dot_00, label_00, dot_02e0, dot_1e0, label_02e0, dot_0e0, label_0e0, label_1e0, dot_10, label_10, label_ellipsis, dot_sub1, dot_sub2, label_sub1, label_sub2, line_sub11, line_sub12, dot_sub11, dot_sub12, ellipsis_sub, arc1, arc2, arc3).shift(RIGHT * 5.4 + DOWN * 1)

        self.add(sub_graph)


        label = MathTex("x \succeq y \succeq z", font_size = 70, stroke_width = 2).set_color(text_black).next_to(axes, DOWN * 2).set_opacity(0)


        all_objects = VGroup(bracket, epsilon, line_11, line_11_2, line_12, line_13, line_14, line_12_label, axes, dot_0, dot_1e, dot_1ek, dot_1, dot_2, labels_axes, label_0, label_1e, label_1ek, label_1, label_2, label, ellipsis_1, ellipsis, sub_graph).center().scale(0.8)
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
