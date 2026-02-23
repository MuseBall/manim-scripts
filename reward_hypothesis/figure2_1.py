"""
TIME : 9:20 - 11:30

Guille - Reward Hypothesis - Dovetail Project∗
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Images for Section in Introduction
Fig Caption: A DFC with 2 absorbing states

Generate image by simple running script:
python ./figure2_1.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_curved_arrow_top, make_curved_arrow_left_to_right, make_curved_arrow_right, make_curved_arrow_bot


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

        unacceptable_1 = make_node(position=[0, 1.75, 0], label="", node_color = node_green)

        unacceptable_2 = make_node(position=[0,-0.25,0], label="", node_color = node_green) 

    #Ellipse

        ellipse_acceptable = Ellipse(width = 4.0, height = 4.0, color = text_black)

        ellipse_acceptable.move_to([-4, 0.75, 0])

        ellipse_unacceptable = Ellipse(width = 2.0, height = 4, color = text_black)

        ellipse_unacceptable.move_to([0, 0.75, 0])

    #Label
        label_acceptable = Tex("Acceptable", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 45).move_to([-4,-2,0])

        label_unacceptable = Tex("Unacceptable", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 45).move_to([0,-2,0])

        label = Tex("Acceptable Set", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([-2,-3.5,0])

        all_nodes = VGroup(acceptable_1, acceptable_2, acceptable_3, unacceptable_1, unacceptable_2)
       
        all_objects = VGroup(all_nodes, ellipse_acceptable, ellipse_unacceptable, label_acceptable, label_unacceptable, label).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
