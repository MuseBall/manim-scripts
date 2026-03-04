"""
TIME : 14:50 - 16:20

Guille - Reward Hypothesis - Dovetail Project

Images for Section in 3 Set - Order representation - Preorder and De-
breu separable - Debreu-Fishburns theorem
Figure 11: Quotient space.

Generate image by simple running script:
python ./figure11.py
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

        node_1 = make_node(position=[-6,0,0], label="", node_color = node_yellow) 

        node_2 = make_node(position=[-3, 0.8, 0], label="", node_color = node_blue)

        node_3 = make_node(position=[-3,-0.8,0], label="", node_color = node_blue)

        node_4 = make_node(position=[0, 1.6, 0], label="", node_color = node_green)

        node_5 = make_node(position=[0, -1.6, 0], label="", node_color = node_green)


    #Label

        label_right_bot = MathTex(f"(X,\succeq )", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([-2.5,-4,0])

        label_left_bot = MathTex(f"(X, \succeq_Q)", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([4,-2,0])

    # Self loop arrows

        arrow_1 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1, color = text_black, label = "").shift(UP * 0.11)

        arrow_2 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4 , stroke_width = 3, start_node = node_2, color = text_black, label = "").shift(UP * 0.11)

        arrow_3 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_4, color = text_black, label = "").shift(UP * 0.11)

        arrow_5 = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_5, color = text_black, label = "").shift(DOWN * 0.11)

    # Arrow

        stem_1 = Line(node_1.get_right(), [-4.5,0,0], color = text_black, stroke_width =2.5) 

        arrow_6 = make_arrow(start = stem_1.get_right(), end = node_2.get_left(), label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_7 = make_arrow(start = stem_1.get_right(), end = node_3.get_left(), label = "", scale_label = 0.4, label_shift = 0.3)

        stem_2 = Line(node_2.get_right(), [-1.8,0.8,0], color = text_black, stroke_width =2.5)

        arrow_8 = make_arrow(start = stem_2.get_right(), end = node_4.get_left() + UP * 0.08 + RIGHT * 0.02, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_9 = make_arrow(start = stem_2.get_right(), end = node_5.get_left() + UP * 0.2 + RIGHT * 0.03, label = "", scale_label = 0.4, label_shift = 0.3)
        
        stem_3 = Line(node_3.get_right(), [-1.8,-0.8,0], color = text_black, stroke_width =2.5)

        arrow_10 = make_arrow(start = stem_3.get_right(), end = node_4.get_left() + DOWN * 0.2 + RIGHT * 0.03, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_11 = make_arrow(start = stem_3.get_right(), end = node_5.get_left() + DOWN * 0.08 + RIGHT * 0.02, label = "", scale_label = 0.4, label_shift = 0.3)

    # Curved Arrow

        arrow_12 = CurvedArrow(start_point = node_1.get_top() + DOWN * 0.7 + RIGHT * 0.35, end_point = node_4.get_top() + DOWN * 0.7 + LEFT * 0.4, radius=-3, color = text_black, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07).shift(UP * 0.55)

        arrow_13 = CurvedArrow(start_point = node_1.get_bottom() + RIGHT * 0.3, end_point = node_5.get_bottom() + DOWN * 0.4 + LEFT * 0.4, radius= 3, color = text_black, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07).shift(UP * 0.55)

    # Arrows

        arrow_14 = make_arrow(start = node_2.get_bottom(), end = node_3.get_top(), label = "", scale_label = 0.4, label_shift = 0.3).shift(RIGHT * 0.15)

        arrow_15 = make_arrow(start = node_3.get_top(), end = node_2.get_bottom(), label = "", scale_label = 0.4, label_shift = 0.3).shift(LEFT * 0.15)

        arrow_16 = make_arrow(start = node_4.get_bottom(), end = node_5.get_top(), label = "", scale_label = 0.4, label_shift = 0.3).shift(RIGHT * 0.15)

        arrow_17 = make_arrow(start = node_5.get_top(), end = node_4.get_bottom(), label = "", scale_label = 0.4, label_shift = 0.3).shift(LEFT * 0.15)


    # Right Graph

        node_1_right = node_1.copy().move_to([2,0,0])
        circle_1 = Circle(radius = 0.3, stroke_color = text_black, stroke_width = 2).move_to([2,0,0])
        node_2_right = node_2.copy().move_to([4,0,0])
        circle_2 = Circle(radius = 0.3, stroke_color = text_black, stroke_width = 2).move_to([4,0,0])
        node_3_right = node_4.copy().move_to([6,0,0])
        circle_3 = Circle(radius = 0.3, stroke_color = text_black, stroke_width = 2).move_to([6,0,0])

    # Arrows

        arrow_18 = make_arrow(start = node_1_right, end = node_2_right, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_19 = make_arrow(start = node_2_right, end = node_3_right, label = "", scale_label = 0.4, label_shift = 0.3)

        arrow_20 = make_arrow(start = [0.5,0,0], end = [1.2,0,0], label = "", scale_label = 0.4, label_shift = 0.3, stroke_width = 10, tip_length = 1).scale(1.5)

        all_nodes = VGroup(node_1, node_2, node_3, node_4, node_5, node_1_right, node_2_right, node_3_right, circle_1, circle_2, circle_3)

        all_arrows = VGroup(*[locals()[f"arrow_{i}"] for i in range(1, 21)]), stem_1, stem_2, stem_3

        all_objects = VGroup(all_arrows, all_nodes,label_left_bot, label_right_bot).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
