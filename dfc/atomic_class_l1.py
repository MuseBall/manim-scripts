"""
TIME : 16:55 - 17:45

Robust Finite Policies are Nontrivially Structured
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Images for Section in Atomic Classifier
Fig Caption: A DFC where every input has a unique input alphabet character

Generate image by simple running script:
python ./atomic_class_l1.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_curved_arrow_top, make_curved_arrow_left_to_right


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


        # background rectangle with rounded corners
        background_rectangle = RoundedRectangle(color = "#d6e2e2", fill_opacity = 1, corner_radius = 0.7, 
                                                height = 8, width = 8)

    # Nodes 
        d = make_node(position=[-2, 0, 0], label="", node_color = node_blue)

        a1_top = make_node(position=[2,2.25,0], label="a_1", node_color=node_orange) 

        a2_top = make_node(position=[2,0.75,0], label="a_2", node_color=node_green) 

        a1_bot = make_node(position=[2,-0.75,0], label="a_1", node_color=node_orange) 

        a1_bot_bot = make_node(position=[2,-2.25,0], label="a_1", node_color=node_orange) 
         

    # Arrows
        arrow_1 = make_arrow(start = d, end = a1_top, label = "i_1", scale_label = 0.4, label_shift = 0.3)
        
        arrow_2 = make_arrow(start = d, end = a2_top, label = "i_2", scale_label = 0.4, label_shift = 0.25).shift(UP * 0.04)

        arrow_3 = make_arrow(start = d, end = a1_bot, label = "i_3", scale_label = 0.4, label_shift = 0.25).shift(DOWN * 0.03)
        
        arrow_4 = make_arrow(start = d, end = a1_bot_bot ,label = "i_4", scale_label = 0.4, label_shift = 0.3)

    # Triangle 
        triangle = Triangle(color = text_black, fill_opacity=1).rotate(270*DEGREES)
        triangle.scale(0.3).shift(LEFT * 2.77 + DOWN * 0.25)
   
        all_nodes = VGroup(a1_bot_bot, a1_bot, a2_top, a1_top, d)
       
        all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        all_objects = VGroup(all_arrows, all_nodes, triangle).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())

        
with tempconfig({"preview": False}):
    scene = Graph()
    scene.render()
