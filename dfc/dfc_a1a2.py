"""
TIME : 14:35 - 16:10

Robust Finite Policies are Nontrivially Structured
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Images for Section in Definitions
Fig Caption: A DFC for a policy which sends inputs that end in 0 to action a1 and sends inputs ending in 1 to action a2

Generate image by simple running script:
python ./dfc_a1a2.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_curved_arrow_top, make_curved_arrow_left_to_right, make_self_loop_top


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
        a1 = make_node(position=[-2,0,0], radius=0.4, label="a_1", node_color=node_orange) 

        a2 = make_node(position=[2,0,0], radius=0.4, label="a_2", node_color=node_green) 

    # Arrows
        arrow_1 = make_curved_arrow_left_to_right(start_node = a1, end_node = a2, color=text_black, label= "1", radius = 6).shift(DOWN * 0.05 + LEFT * 0.04)
        
        arrow_2 = make_curved_arrow_right_to_left(start_node = a2, end_node = a1, color=text_black, label= "0", radius = 6).shift(UP * 0.05 + RIGHT * 0.04)

        #arrow_3 = make_curved_arrow_top(start_node = a1, end_node = a1, color=text_black, label= "0", radius = 0.27).shift(DOWN * 0.06)

        arrow_3 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = a1, color = text_black, label = "0"). shift(UP * 0.08)

        #arrow_4 = make_curved_arrow_top(start_node = a2, end_node = a2, color=text_black, label= "1", radius = 0.27).shift(DOWN * 0.06)

        arrow_4 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = a2, color = text_black, label = "1"). shift(UP * 0.08)

    # Triangle 
        triangle = Triangle(color = text_black, fill_opacity=1).rotate(270*DEGREES)
        triangle.scale(0.3).shift(LEFT * 2.67 + DOWN * 0.25)
   
        all_nodes = VGroup(a1, a2)
       
        all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4)

        all_objects = VGroup(all_arrows, all_nodes, triangle).center()

        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())

        
with tempconfig({"preview": False}):
    scene = Graph()
    scene.render()
