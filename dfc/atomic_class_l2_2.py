"""
TIME : 18:00 - 19:15

Robust Finite Policies are Nontrivially Structured
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Images for Section in Atomic Classifier
Fig Caption: A minimized atomic classifier for strings of length 2

Generate image by simple running script:
python ./atomic_class_l2_2.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_self_loop_top, make_curved_arrow_left_to_right, make_self_loop_right


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
        d_left= make_node(position=[-3, 0, 0], label="d")

        d_top = make_node(position=[-0.75,2.25,0], label="d") 

        d_bot = make_node(position=[-0.75,-2.25,0], label="d")

        a2_top = make_node(position=[1.75,2.25,0], label="a_2", node_color=node_green) 

        a1_bot = make_node(position=[1.75,-2.25,0], label="a_1", node_color=node_orange) 

        d_right = make_node(position=[4,0,0], label="d") 
         

    # Arrows
        arrow_1 = make_arrow(start = d_left, end = d_top, label = "0", scale_label = 0.4, label_shift = 0.3)

        arrow_2 = make_arrow(start = d_left, end = d_bot, label = "1", scale_label = 0.4, label_shift = 0.3)
        
        arrow_3 = make_arrow(start = d_top, end = a2_top, label = "1", scale_label = 0.4)
        
        arrow_4 = make_arrow(start = d_top, end = a1_bot, label = "0", scale_label = 0.4, label_shift = 0.4)

        arrow_5 = make_arrow(start = d_bot, end = a1_bot, label = "0,1", scale_label = 0.4)
        
        arrow_6 = make_arrow(start = a2_top, end = d_right, label = "0,1", scale_label = 0.4)

        arrow_7 = make_arrow(start = a1_bot, end = d_right, label = "0,1", scale_label = 0.4)
        
        #arrow_8 = make_curved_arrow_right(start_node = d_right, end_node = d_right, color=text_black, label= "0,1", radius = 0.25, label_scale = 0.4).shift(LEFT * 0.03)

        arrow_8 = make_self_loop_right(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = d_right, color = text_black, label = "0,1", label_scale = 0.4, label_shift = UP * 0.15).shift(0.09 * RIGHT + UP * 0.09).rotate(-PI/2).shift(RIGHT * 0.3 + DOWN * 0.3)

    # Triangle 
        triangle = Triangle(color = text_black, fill_opacity=1).rotate(270*DEGREES)
        triangle.scale(0.3).shift(LEFT * 3.77 + DOWN * 0.25)
   
        all_nodes = VGroup(d_left, d_right, d_bot, d_top, a1_bot, a2_top)
       
        all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8)

        all_objects = VGroup(all_arrows, all_nodes, triangle)
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())

        
with tempconfig({"preview": False}):
    scene = Graph()
    scene.render()
