"""
TIME : 10:20 - 11:10
       16:20 - 18:45

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Set - Order representation - Preorder and Debreu separable - Debreu-Fishburns theorem
Figure 3: Order representation

Generate image by simple running script:
python ./figure2_1.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_curved_arrow_left_to_right, make_self_loop_top, make_self_loop_bot


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

    # Nodes 
        node_A = make_node(position=[-3, 1.5, 0], label="A", node_color = node_blue)

        node_B = make_node(position=[-6,0,0], label="B", node_color = node_yellow) 

        node_C = make_node(position=[-3,-1.5,0], label="C", node_color = node_red)

        node_D = make_node(position=[0, 0, 0], label="D", node_color = node_green)


    #Label

        label_right = MathTex("\succsim", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 50).move_to([-3,-3,0])

        label_right_bot = MathTex("x \succsim y", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([-3,-4,0])

        label_left = MathTex("f", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 50).move_to([4.3,-3,0])

        label_left_bot = MathTex("f(x) \geq f(y)", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([4.3,-4,0])

        iff_arrow = MathTex("\iff", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([0.3,-4,0])

    # Self loop arrows

        arrow_1 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_A, color = text_black, label = "").shift(UP * 0.11)

        arrow_2 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = node_B, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_C, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_D, color = text_black, label = "").shift(DOWN * 0.11)

    # Arrow

        arrow_5 = make_arrow(start = node_B, end = node_A, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_6 = make_arrow(start = node_B, end = node_C, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_7 = make_arrow(start = node_A, end = node_C, label = "", scale_label = 0.4, label_shift = 0.3).shift(LEFT * 0.1 + UP * 0.03)

        arrow_8 = make_arrow(start = node_C, end = node_A, label = "", scale_label = 0.4, label_shift = 0.3).shift(RIGHT * 0.1 + DOWN * 0.05)

        arrow_9 = make_arrow(start = node_A, end = node_D, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_10 = make_arrow(start = node_C, end = node_D, label = "", scale_label = 0.4, label_shift = 0.3)

    # Curved Arrow

        arrow_11 = CurvedArrow(start_point = node_B.get_top() + DOWN * 0.7, end_point = node_D.get_top() + DOWN * 0.5, radius=-3.1, color = text_black, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07).shift(UP * 0.55)

    #Axes

        axes = Axes(x_range =[0,5], y_range = [0,4], x_length= 5, y_length = 4, x_axis_config={"include_numbers": False}, y_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": StealthTip, "color": text_black}).move_to([4,0,0])

        labels_axes = axes.get_axis_labels(MathTex("X", color = text_black, stroke_width = 1.5).scale(0.7), MathTex(rf"f(x) \in \mathbb{{R}}", color = text_black, stroke_width = 1.5).scale(0.7))

        x_positions = [1, 2, 3, 4]
        labels = ["A", "B", "C", "D"]

        x_labels = VGroup()
        for x, label in zip(x_positions, labels):
            text = MathTex(rf"\mathbf{{{label}}}", font_size = 60).scale(0.6).set_color(text_black)
            text.next_to(axes.c2p(x, 0), DOWN)
            x_labels.add(text)

    # Points in graph

        point_A = axes.coords_to_point(1, 1.4)
        point_B = axes.coords_to_point(2, 0.6)
        point_C = axes.coords_to_point(3, 1.4)
        point_D = axes.coords_to_point(4, 2.9)

        dot_A = Dot(point_A, color = node_blue, stroke_color = text_black, stroke_width = 1)
        dot_B = Dot(point_B, color = node_yellow, stroke_color = text_black, stroke_width = 1)
        dot_C = Dot(point_C, color = node_red, stroke_color = text_black, stroke_width = 1)
        dot_D = Dot(point_D, color = node_green, stroke_color = text_black, stroke_width = 1)

    #Lines in graph

        line_AB = DashedLine(point_A, point_B, dash_length=0.15, color=text_black, stroke_width=3)
        line_BC = DashedLine(point_B, point_C, dash_length=0.15, color=text_black, stroke_width=3)
        line_CD = DashedLine(point_C, point_D, dash_length=0.15, color=text_black, stroke_width=3)

        all_nodes = VGroup(node_A, node_B, node_C, node_D)

        all_arrows = VGroup(*[locals()[f"arrow_{i}"] for i in range(1, 12)])

        all_objects = VGroup(all_arrows, all_nodes, label_right, label_right_bot, axes, x_labels, line_AB, line_BC, line_CD, dot_A, dot_B, dot_C, dot_D, labels_axes, label_left, label_left_bot, iff_arrow).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
