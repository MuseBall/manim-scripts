"""
TIME : 18:50 - 20:00

Guille - Reward Hypothesis - Dovetail Project

Images for Section in 3 Set - Order representation - Preorder and De-
breu separable - Debreu-Fishburns theorem
Figure 4: Completeness

Generate image by simple running script:
python ./figure4.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_self_loop_top, make_self_loop_bot


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

    # Right Nodes 
        node_1 = make_node(position=[-4, 2, 0], label="", node_color = node_blue)

        node_2 = make_node(position=[-3,0,0], label="", node_color = node_blue) 

        node_3 = make_node(position=[-5,0,0], label="", node_color = node_blue)


    #Label

        label = Tex("Not Complete", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([-4,-2,0])

    # Arrows

        arrow_1 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1, color = text_black, label = "").shift(UP * 0.11)

        arrow_2 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = node_2, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4 = make_arrow(start = node_3, end = node_2, label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.15 * RIGHT * 0.03)

        arrow_5 = make_arrow(start = node_2, end = node_3, label = "", scale_label = 0.4, label_shift = 0.3).shift(DOWN * 0.15 + RIGHT * 0.07)

        arrow_6 = make_arrow(start = node_1, end = node_2.get_top(), label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.04)

    # Dotted line and label

        line_13 = DashedLine(node_1, node_3.get_top(), dash_length=0.15, color= "#a36066", stroke_width=3).shift(LEFT * 0.15)

        line_label = Tex("Incomplete", color = text_black, stroke_color = "#a36066" , 
        stroke_width = 1.3, font_size = 25).next_to(line_13, LEFT).shift(RIGHT * 0.3)

    # Right Nodes

        node_1_right = node_1.copy().move_to([4, 2, 0])
        node_2_right = node_2.copy().move_to([3, 0, 0])
        node_3_right = node_3.copy().move_to([5, 0, 0])

    # Right Arrows

        arrow_1_right = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1_right, color = text_black, label = "").shift(UP * 0.11)

        arrow_2_right = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = node_2_right, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3_right = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3_right, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4_right = make_arrow(start = node_3_right, end = node_2_right, label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.15 + RIGHT * 0.06)

        arrow_5_right = make_arrow(start = node_2_right, end = node_3_right, label = "", scale_label = 0.4, label_shift = 0.3).shift(DOWN * 0.15 + RIGHT * 0.01)

        arrow_6_right = make_arrow(start = node_2_right.get_top(), end = node_1_right, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_7_right = make_arrow(start = node_1_right, end = node_3_right.get_top(), label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.03)

    # Right Label

        label_right = Tex("Complete", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([4,-2,0])

        label_right_small = Tex("Indifferent", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 25).move_to([4,-0.5,0])

        label_small = label_right_small.copy().move_to([-4,-0.5,0])

    # Adjusting the two graphs to be closer

        graph_right = VGroup(label_right, label_right_small,node_1_right, node_2_right, node_3_right, arrow_1_right, arrow_2_right, arrow_3_right, arrow_4_right, arrow_5_right, arrow_6_right, arrow_7_right).shift(LEFT * 1)

        graph_right = VGroup(label, label_small, node_1, node_2, node_3, arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, line_13, line_label).shift(RIGHT * 1)

        all_nodes = VGroup(node_1, node_2, node_3, node_1_right, node_2_right, node_3_right)
     
        all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, line_13, arrow_1_right, arrow_2_right, arrow_3_right, arrow_4_right, arrow_5_right, arrow_6_right, arrow_7_right)

        all_objects = VGroup(all_arrows, all_nodes, label, line_label, label_right, label_right_small, label_small).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
