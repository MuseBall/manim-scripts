"""
TIME : 15:10 - 16 :50

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 19: Concatenatable mixture space

Generate image by simple running script:
python ./figure18.py
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

        axes = Axes(x_range =[-1,1], x_length= 3, tips = False, x_axis_config={"include_numbers": False, "include_ticks": True}, axis_config = {"tip_shape": None, "color": text_black})

        axes.y_axis.set_opacity(0)

        labels_axes = axes.get_axis_labels(MathTex("", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes[0].set_opacity(0)
        labels_axes[1].set_opacity(0)

        x = MathTex("x", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(axes, DL).shift(UP * 3 + RIGHT * 0.3)

        y = MathTex("y", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(axes, DR).shift(UP * 3 + LEFT * 0.3)

        p_position = axes.coords_to_point(-0.4, 0)

        dot_p = Dot(p_position, color = node_green, stroke_color = text_black, stroke_width = 1)

        p = MathTex("px + (1-p)y", color = text_black, stroke_width = 1, font_size = 50).scale(0.6).next_to(dot_p, UP)

        label1 = MathTex(r"x, y \in X", color = text_black, stroke_width = 1, font_size = 70).scale(0.6).next_to(axes, UP).shift(DOWN * 2.2)


        axes_1 = VGroup(axes, x, y, dot_p, p, label1).shift(LEFT * 3.2 + UP * 1.5)

    #Axes 2

        axes2 = Axes(x_range =[-1,1], x_length= 3, tips = False, x_axis_config={"include_numbers": False, "include_ticks": True}, axis_config = {"tip_shape": None, "color": text_black})

        axes2.y_axis.set_opacity(0)

        labels_axes2 = axes2.get_axis_labels(MathTex("", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes2[0].set_opacity(0)
        labels_axes2[1].set_opacity(0)

        tx = MathTex(r"t \cdot_T x", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(axes2, DL).shift(UP * 3 + RIGHT * 0.7)

        ty = MathTex(r"t \cdot_T y", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(axes2, DR).shift(UP * 3 + LEFT * 0.7)

        tp_position = axes2.coords_to_point(-0.4, 0)

        dot_tp = Dot(tp_position, color = node_green, stroke_color = text_black, stroke_width = 1)

        tp = MathTex(r"t \cdot_T (px + (1-p)y)", color = text_black, stroke_width = 1, font_size = 50).scale(0.6).next_to(dot_tp, UP)

        label2 = MathTex(r"t \in T \subseteq X", color = text_black, stroke_width = 1, font_size = 70).scale(0.6).next_to(axes2, UP).shift(DOWN * 2.2)

        axes_2 = VGroup(axes2, tx, ty, dot_tp, tp, label2).shift(UP * 1.5 + RIGHT * 3.2)

    # Traingle 1

        triangle1 = Polygon(
            [0,1,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2)

        dot_x1 = Dot([0,1,0], color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_y1 = Dot([-1.5, -1, 0], color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_z1 = Dot([1.5, -1, 0], color = node_green, stroke_color = text_black, stroke_width = 1)

        x1 = MathTex("x", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_x1, UP)
        y1 = MathTex("y", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_y1, DOWN)
        z1 = MathTex("z", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_z1, DOWN)

        dot_p1 = Dot([0.75,0,0], color = node_blue, stroke_color = text_black, stroke_width = 1)
        p1 = MathTex("px + (1+p)z", color = text_black, stroke_width = 1, font_size = 50).scale(0.6).next_to(dot_p1, RIGHT)

        dot_pp1 = Dot([0.8,-0.7,0], color = node_blue, stroke_color = text_black, stroke_width = 1)
        pp1 = MathTex(r"t \cdot_T (px + (1-p)y)", color = text_black, stroke_width = 1, font_size = 50).scale(0.6).next_to(dot_pp1, RIGHT).shift(RIGHT * 0.4)


        arrow1 = make_arrow(start = dot_pp1.get_right() + RIGHT * 0.1, end = pp1.get_left() + LEFT * 0.15 , label = "", color = text_black).shift(RIGHT * 0.04)

        label3 = MathTex(r"x, y, z \in X", color = text_black, stroke_width = 1, font_size = 70).scale(0.6).next_to(triangle1, UP).shift(UP * 0.7 + RIGHT * 0.7)

        triangle_1 = VGroup(triangle1, dot_x1, dot_y1, dot_z1, x1, y1, z1, dot_p1, p1, dot_pp1, pp1, arrow1, label3).shift(LEFT * 4 + DOWN * 2)

    # Traingle 2

        triangle2 = Polygon(
            [0,1,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2)

        dot_x2 = Dot([0,1,0], color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_y2 = Dot([-1.5, -1, 0], color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_z2 = Dot([1.5, -1, 0], color = node_green, stroke_color = text_black, stroke_width = 1)

        x2 = MathTex(r"t \cdot_T x", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_x2, UP)
        y2 = MathTex(r"t \cdot_T y", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_y2, DOWN)
        z2 = MathTex(r"t \cdot_T z", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_z2, DOWN)

        dot_p2 = Dot([0.75,0,0], color = node_blue, stroke_color = text_black, stroke_width = 1)
        p2 = MathTex(r"t \cdot_T (px + (1-p)y)", color = text_black, stroke_width = 1, font_size = 50).scale(0.6).next_to(dot_p2, RIGHT)

        dot_pp2 = Dot([0.8,-0.7,0], color = node_blue, stroke_color = text_black, stroke_width = 1)
        pp2 = MathTex(r"t \cdot_T (px + (1-p)y)", color = text_black, stroke_width = 1, font_size = 50).scale(0.6).next_to(dot_pp2, RIGHT).shift(RIGHT * 0.4)

        arrow2 = make_arrow(start = dot_pp2.get_right() + RIGHT * 0.1, end = pp2.get_left() + LEFT * 0.15 , label = "", color = text_black).shift(RIGHT * 0.04)

        label4 = MathTex(r"t \in T \subseteq X", color = text_black, stroke_width = 1, font_size = 70).scale(0.6).next_to(triangle2, UP).shift(UP * 0.7 + RIGHT * 0.7)

        triangle_2 = VGroup(triangle2, dot_x2, dot_y2, dot_z2, x2, y2, z2, dot_p2, p2, dot_pp2, pp2, arrow2, label4).shift(DOWN * 2 + RIGHT * 2.4)

    # Labels

        self.add(axes_1, axes_2, triangle_1, triangle_2)


        #debug distance of objects with a grid
        #self.add(NumberPlane())


