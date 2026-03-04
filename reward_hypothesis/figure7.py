"""
TIME : 10:50 - 11:30

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Set - Order representation - Preorder and Debreu separable - Debreu-Fishburns theorem
Figure 7: Lexicographic order

Generate image by simple running script:
python ./figure7.py
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

        point_A = axes.coords_to_point(1, 1)
        point_B = axes.coords_to_point(1, 1.7)
        point_C = axes.coords_to_point(2, -1)

        dot_A = Dot(point_A, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_B = Dot(point_B, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_C = Dot(point_C, color = node_green, stroke_color = text_black, stroke_width = 1)

        label_A = MathTex("z", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_A, LEFT)
        label_B = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_B, LEFT)
        label_C = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_C, RIGHT)


    #Lines in graph

        line_AB = DashedLine(point_A + UP * 2, point_B + DOWN * 5, dash_length=0.15, color=text_black, stroke_width=3)
        line_C = DashedLine(point_C + UP * 4.3, point_C + DOWN * 1.8, dash_length=0.15, color=text_black, stroke_width=3)

        label = MathTex("x \succsim y \succsim z", font_size = 70, stroke_width = 2).set_color(text_black).next_to(axes, DOWN)


        all_objects = VGroup(axes, line_AB, line_C, dot_A, dot_B, dot_C, labels_axes, label_A, label_B, label_C, label).center().scale(0.8)
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
