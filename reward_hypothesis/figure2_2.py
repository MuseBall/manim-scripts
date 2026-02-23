"""
TIME : 11:45 - 13:25

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Preferences
Figure 2: Acceptable subset vs Relation preference.

Generate image by simple running script:
python ./figure2_2.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_curved_arrow_top, make_curved_arrow_left_to_right, make_curved_arrow_right, make_curved_arrow_bot, make_self_loop_top


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

        unacceptable_1 = make_node(position=[-1, 1.75, 0], label="", node_color = node_green)

        unacceptable_2 = make_node(position=[-1,-0.25,0], label="", node_color = node_green) 


    #Label

        label = Tex("Preference Relation", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([-3,-3.5,0])

    # Arrows

        arrow_1 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = acceptable_1, color = text_black, label = "1"). shift(UP * 0.08)

        arrow_2 = make_arrow(start = acceptable_3, end = acceptable_2, label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.15 * RIGHT * 0.03)

        arrow_3 = make_arrow(start = acceptable_2, end = acceptable_3, label = "", scale_label = 0.4, label_shift = 0.3).shift(DOWN * 0.15 + RIGHT * 0.07)

        arrow_4 = make_arrow(start = acceptable_2, end = acceptable_1, label = "", scale_label = 0.4, label_shift = 0.3).shift(DOWN * 0.1)

        arrow_5 = make_arrow(start = acceptable_2, end = unacceptable_1, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_6 = make_arrow(start = acceptable_2, end = unacceptable_2, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_7 = make_arrow(start = acceptable_1, end = unacceptable_1, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_8 = make_arrow(start = unacceptable_1, end = unacceptable_2, label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.04)

        all_nodes = VGroup(acceptable_1, acceptable_2, acceptable_3, unacceptable_1, unacceptable_2)
     
        all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8)

        graph = VGroup(all_nodes, all_arrows).shift(DOWN * 1.5)

        all_objects = VGroup(all_arrows, all_nodes, label).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
