"""
TIME : 18:45 - 19:30

Robust Finite Policies are Nontrivially Structured
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Images for Section in Proof
Fig Caption: A DFC with a loop that is not a self-loop

Generate image by simple running script:
python ./dfc_loop.py
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


        # background rectangle with rounded corners
        background_rectangle = RoundedRectangle(color = "#d6e2e2", fill_opacity = 1, corner_radius = 0.7, 
                                                height = 8, width = 8)

    # Nodes 
        c = make_node(position=[-5, 0, 0], label="c", node_color = node_blue)

        a = make_node(position=[-2,0,0], label="a", node_color = node_orange) 

        b = make_node(position=[1,0,0], label="b", node_color = node_pink)

    # Arrows

        arrow_1 = make_arrow(start = c, end = a, label = "0,1", scale_label = 0.4, label_shift = 0.3)

        arrow_2 = make_curved_arrow_left_to_right(start_node = a, end_node = b, color = text_black, label = "0,1", radius = 2, label_scale = 0.4).shift(0.2 * DOWN)

        arrow_3 = make_curved_arrow_right_to_left(start_node = b, end_node = a, color = text_black, label = "0,1", radius = 2, label_scale = 0.4).shift(0.2 * UP)

    # Triangle 
        triangle = Triangle(color = text_black, fill_opacity=1).rotate(270*DEGREES)
        triangle.scale(0.3).shift(LEFT * 5.77 + DOWN * 0.25)
   
        all_nodes = VGroup(c, b, a)
       
        all_arrows = VGroup(arrow_1, arrow_2, arrow_3)       
        #all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8)

        all_objects = VGroup(all_arrows, all_nodes, triangle).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())

        
with tempconfig({"preview": False}):
    scene = Graph()
    scene.render()
