"""
TIME : 16:15 - 16:50

Robust Finite Policies are Nontrivially Structured
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Images for Section in Special Policies
Fig Caption: A DFC for a default policy which always outputs the action d

Generate image by simple running script:
python ./dfc_d.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_self_loop_top, make_curved_arrow_left_to_right


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
        background_color = "#dce2e1" 


        # background rectangle with rounded corners
        background_rectangle = RoundedRectangle(color = "#d6e2e2", fill_opacity = 1, corner_radius = 0.7, 
                                                height = 8, width = 8)

    # Nodes 
        d = make_node(position=[0,0,0], radius=0.4, label="d") 

    # Arrows
        #arrow_1 = make_curved_arrow_top(start_node = d, end_node = d, color=text_black, label= "0,1", radius = 0.21)

        arrow_1 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = d, color = text_black, label = "0,1"). shift(UP * 0.08)

    # Triangle 
        triangle = Triangle(color = text_black, fill_opacity=1).rotate(270*DEGREES)
        triangle.scale(0.3).shift(LEFT * 0.68 + DOWN * 0.25)

        #triangle_tip = Triangle(color = background_color, fill_opacity=1).rotate(270*DEGREES)
        #triangle_tip.scale(0.06).shift(LEFT * 0.6 + DOWN * 0.25)
   
        all_nodes = VGroup(d)
       
        all_arrows = VGroup(arrow_1)

        #all_objects = VGroup(all_arrows, all_nodes, triangle, triangle_tip).center()
        all_objects = VGroup(all_arrows, all_nodes, triangle).center()

        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
    


        
with tempconfig({"preview": False}):
    scene = Graph()
    scene.render()
