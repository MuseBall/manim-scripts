"""
TIME : 16:30 - 17:20

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Set - Order representation - Preorder and Debreu separable - Debreu-Fishburns theorem
Figure 12: Denseness.

Generate image by simple running script:
python ./figure12.py
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

        axes = Axes(x_range =[-1.5,3.5], x_length= 4, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": StealthTip, "color": text_black})

        axes.y_axis.set_opacity(0)

        labels_axes = axes.get_axis_labels(MathTex(r"(\mathbb{R}, >)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes[0].next_to(axes.get_x_axis().get_right(), RIGHT)
        labels_axes[1].set_opacity(0)

    # Points in graph

        point_x = axes.coords_to_point(0.5, 0)
        point_y = axes.coords_to_point(2.5, 0)

        dot_x = Dot(point_x, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y = Dot(point_y, color = node_purple, stroke_color = text_black, stroke_width = 1)

        label_x = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_x, DOWN)
        label_y = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_y, DOWN)


    #Lines in graph

        line_xy = DashedLine(point_x + RIGHT * 0.75 + UP * 1, point_x + RIGHT * 0.75, dash_length=0.15, color="#739b99", stroke_width=3)

        label_line = MathTex(r"q \in \mathbb{Q}", font_size = 60).scale(0.6).set_color(text_black).next_to(line_xy, UP)


    ### RIGHT
    #Axes

        axes_right = Axes(x_range =[-1.5,3.5], x_length= 4, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": StealthTip, "color": text_black})

        axes_right.y_axis.set_opacity(0)

        labels_axes_right = axes_right.get_axis_labels(MathTex(r"(X \setminus \sim, \succsim_Q)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes_right[0].next_to(axes.get_x_axis().get_right(), RIGHT)
        labels_axes_right[1].set_opacity(0)

    # Points in graph

        point_x_right = axes_right.coords_to_point(0.5, 0)
        point_y_right = axes_right.coords_to_point(2.5, 0)

        dot_x_right = Dot(point_x_right, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y_right = Dot(point_y_right, color = node_purple, stroke_color = text_black, stroke_width = 1)

        label_x_right = MathTex("[x]", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_x_right, DOWN)
        label_y_right = MathTex("[y]", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_y_right, DOWN)


    #Lines in graph

        line_xy_right = DashedLine(point_x + RIGHT * 0.75 + UP * 1, point_x + RIGHT * 0.75, dash_length=0.15, color="#739b99", stroke_width=3)

        label_line_right = MathTex(r"d \in D", font_size = 60).scale(0.6).set_color(text_black).next_to(line_xy, UP)

        label_middle = MathTex(r"\equiv", font_size = 100).scale(0.6).set_color(text_black).shift(LEFT * 3.1)


        all_objects = VGroup(axes, line_xy, dot_x, dot_y, labels_axes, label_x, label_y,label_line).scale(0.8).shift(LEFT * 3)
        all_objects_right = VGroup(axes_right, line_xy_right, dot_x_right, dot_y_right, labels_axes_right, label_x_right, label_y_right,label_line_right, label_middle).scale(0.8).shift(RIGHT * 3)
        all_ = VGroup(all_objects, all_objects_right).center()
        self.add(all_objects, all_objects_right)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
