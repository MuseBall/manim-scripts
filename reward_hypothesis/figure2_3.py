"""
TIME : 14:00 - 14:30
       17:50 - 19:30

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Preferences
Figure 2: Acceptable subset vs Relation preference.

Generate image by simple running script:
python ./figure2_1.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_curved_arrow_left_to_right, make_curved_arrow_right, make_self_loop_top, make_self_loop_bot


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
        background_rectangle = RoundedRectangle(color = "#d6e2e2", fill_opacity = 1, corner_radius = 0.7, 
                                                height = 8, width = 8)

    # Nodes 
        acceptable_1 = make_node(position=[-4, 2, 0], label="", node_color = node_blue)

        acceptable_2 = make_node(position=[-3,0,0], label="", node_color = node_blue) 

        acceptable_3 = make_node(position=[-5,0,0], label="", node_color = node_blue)

        unacceptable_1 = make_node(position=[-1, 2, 0], label="", node_color = node_green)

        unacceptable_2 = make_node(position=[-1,0,0], label="", node_color = node_green) 


    #Label

        label = Tex("From A.S to Relation", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([-3,-3.5,0])

    # Arrows

        arrow_1 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = acceptable_1, color = text_black, label = "").shift(UP * 0.11)

        arrow_2 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = acceptable_2, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = acceptable_3, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = unacceptable_1, color = text_black, label = "").shift(UP * 0.11)

        arrow_5 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = unacceptable_2, color = text_black, label = "").shift(DOWN * 0.11)


        arrow_6 = make_arrow(start = acceptable_3, end = acceptable_2, label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.15 + RIGHT * 0.02)

        arrow_7 = make_arrow(start = acceptable_2, end = acceptable_3, label = "", scale_label = 0.4, label_shift = 0.3).shift(DOWN * 0.15 + RIGHT * 0.06)

        arrow_8 = make_arrow(start = acceptable_2, end = acceptable_1, label = "", scale_label = 0.4, label_shift = 0.3).shift(LEFT * 0.08 + DOWN * 0.15)

        arrow_9 = make_arrow(start = acceptable_2, end = unacceptable_1, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_10 = make_arrow(start = acceptable_2, end = unacceptable_2, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_11 = make_arrow(start = acceptable_1, end = unacceptable_1, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_12 = make_arrow(start = unacceptable_1, end = unacceptable_2, label = "", scale_label = 0.4, label_shift = 0.3).shift(RIGHT * 0.15 + UP * 0.03)

        arrow_13 = make_arrow(start = acceptable_1, end = acceptable_2, label = "", scale_label = 0.4, label_shift = 0.3).shift(RIGHT * 0.1 + UP * 0.09)

        arrow_14 = make_arrow(start = acceptable_1, end = acceptable_3, label = "", scale_label = 0.4, label_shift = 0.3).shift(RIGHT * 0.15 + DOWN * 0.07)

        arrow_15 = make_arrow(start = acceptable_1, end = unacceptable_2, label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.07 + RIGHT * 0.07)

        arrow_16 = make_arrow(start = acceptable_3, end = acceptable_1, label = "", scale_label = 0.4, label_shift = 0.3).shift(LEFT * 0.07 + UP * 0.1)

        arrow_17 = CurvedArrow(start_point = acceptable_3.get_top() + LEFT * 0.5 + DOWN * 0.5, end_point = unacceptable_1.get_top() + LEFT * 0.38 + DOWN * 0.13, radius=-2.4, color = text_black, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)
        #arrow_17 = make_arrow(start = acceptable_3, end = unacceptable_1, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_18 = CurvedArrow(start_point = acceptable_3.get_bottom() + RIGHT * 0.3 + UP * 0.3, end_point = unacceptable_2.get_bottom() + LEFT * 0.4 + UP * 0.1, radius=2.4, color = text_black, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)
        #arrow_18 = make_arrow(start = acceptable_3, end = unacceptable_2, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_19 = make_arrow(start = unacceptable_1, end = acceptable_1, label = "", scale_label = 0.4, label_shift = 0.3).shift(DOWN * 0.15 + RIGHT *0.07).set_opacity(0)

        arrow_20 = make_arrow(start = unacceptable_1, end = acceptable_2, label = "", scale_label = 0.4, label_shift = 0.3).set_opacity(0)

        arrow_21 = make_arrow(start = unacceptable_1, end = acceptable_3, label = "", scale_label = 0.4, label_shift = 0.3).set_opacity(0)

        arrow_22 = make_arrow(start = unacceptable_2, end = acceptable_1, label = "", scale_label = 0.4, label_shift = 0.3).set_opacity(0)

        arrow_23 = make_arrow(start = unacceptable_2, end = acceptable_2, label = "", scale_label = 0.4, label_shift = 0.3).shift(DOWN * 0.15 + RIGHT * 0.08).set_opacity(0)

        arrow_24 = make_arrow(start = unacceptable_2, end = acceptable_3, label = "", scale_label = 0.4, label_shift = 0.3).set_opacity(0)

        arrow_25 = make_arrow(start = unacceptable_2, end = unacceptable_1, label = "", scale_label = 0.4, label_shift = 0.3).shift(LEFT * 0.15 + DOWN * 0.02)

        all_nodes = VGroup(acceptable_1, acceptable_2, acceptable_3, unacceptable_1, unacceptable_2)
     
        #all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8, arrow_9, arrow_10, arrow_11, arrow_12)

        all_arrows = VGroup(*[locals()[f"arrow_{i}"] for i in range(1, 26)])

        graph = VGroup(all_nodes, all_arrows).shift(DOWN * 1.5)

        all_objects = VGroup(all_arrows, all_nodes, label).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
