"""
TIME : 14:35 - 15:20 

Robust Finite Policies are Nontrivially Structured
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Images for Section in Proof
Fig Caption: Right: Constructed DFA that accepts exactly the inputs that D maps to action a

Generate image by simple running script:
python ./initial_dfc_right.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_curved_arrow_right_to_left, make_self_loop_top, make_curved_arrow_left_to_right, make_curved_arrow_right, make_curved_arrow_bot


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
        a_left= make_node(position=[-5, 0, 0], label="", node_color = node_orange)

        a_top = make_node(position=[-2,2,0], label="", node_color = node_orange) 

        a_bot = make_node(position=[-2,-2,0], label="", node_color = node_orange)

        b_right = make_node(position=[0,0,0], label="", node_color = node_pink) 

        b_right_right = make_node(position=[4,0,0], label="", node_color = node_pink) 

    # Circle
        circle_a_left = Circle(radius = 0.4, stroke_color = text_black, stroke_width = 2.5).move_to(a_left)

        circle_a_top = Circle(radius = 0.4, stroke_color = text_black, stroke_width = 2.5).move_to(a_top)

        circle_a_bot = Circle(radius = 0.4, stroke_color = text_black, stroke_width = 2.5).move_to(a_bot)
         

    # Arrows

        # ARROW 1

        arrow_1 = CurvedArrow(start_point = a_left.get_top(), end_point = a_top.get_top() + 0.35 * LEFT + DOWN * 0.06, radius= -2, color = text_black, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)

        label_arrow_1 = MathTex("0", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 80).move_to(arrow_1.point_from_proportion(0.5)).shift(UP * 0.3)

        label_arrow_1.scale(0.4)

        arrow_1_with_label = VGroup(arrow_1, label_arrow_1)


        # ARROW 2

        arrow_2 = CurvedArrow(start_point = a_bot.get_bottom() + 0.15 * LEFT, end_point = a_left.get_bottom() + 0.05 * DOWN, radius= -2, color = text_black, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)

        label_arrow_2 = MathTex("1", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 80).move_to(arrow_2.point_from_proportion(0.5)).shift(DOWN * 0.3)

        label_arrow_2.scale(0.4)

        arrow_2_with_label = VGroup(arrow_2, label_arrow_2)

        # ARROW 3

        arrow_3 = Arrow(start = a_top, end = a_left, color = text_black, tip_shape = StealthTip, stroke_width = 2.5, buff = 0, tip_length = 0.07).shift(RIGHT * 0.04)

        angle = arrow_3.get_angle()

        label_arrow_3 = MathTex("1", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 80).move_to(arrow_3.point_from_proportion(0.5)).rotate(angle - PI).shift(UP * 0.3)

        label_arrow_3.scale(0.4)

        arrow_3_with_label = VGroup(arrow_3, label_arrow_3)

        # ARROW 4
        
        arrow_4 = make_arrow(start = a_left, end = a_bot, label = "1", scale_label = 0.4, label_shift = 0.3)

        # ARROW 5

        arrow_5 = make_arrow(start = a_bot, end = b_right, label = "0", scale_label = 0.4, label_shift = 0.3)

        # ARROW 6
        
        #arrow_6 = make_arrow(start = b_right, end = a_top, label = "6", scale_label = 0.4)

        arrow_6 = Arrow(start = b_right, end = a_top, color = text_black, tip_shape = StealthTip, stroke_width = 2.5, buff = 0, tip_length = 0.07).shift(RIGHT * 0.04)

        angle = arrow_6.get_angle()

        label_arrow_6 = MathTex("0", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 80).move_to(arrow_6.point_from_proportion(0.5)).rotate(angle - PI).shift(UP * 0.3)

        label_arrow_6.scale(0.4)

        arrow_6_with_label = VGroup(arrow_6, label_arrow_6)

        # ARROW 7

        #arrow_7 = make_arrow(start = b_right_right.get_left() + 0.1 * UP, end = a_top, label = "7", scale_label = 0.4)
        arrow_7 = Arrow(start = b_right_right.get_left() + 0.05 * UP, end = a_top, color = text_black, tip_shape = StealthTip, stroke_width = 2.5, buff = 0, tip_length = 0.07).shift(RIGHT * 0.04)

        angle = arrow_7.get_angle()

        label_arrow_7 = MathTex("1", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 80).move_to(arrow_7.point_from_proportion(0.5)).rotate(angle - PI).shift(UP * 0.25)

        label_arrow_7.scale(0.4)

        arrow_7_with_label = VGroup(arrow_7, label_arrow_7)

        # ARROW 8
        
        #arrow_8 = make_arrow(start = b_right_right.get_left() + 0.1 * DOWN, end =a_bot, label = "8", scale_label = 0.4)

        arrow_8 = Arrow(start = b_right_right.get_left() + 0.05 * DOWN, end = a_bot, color = text_black, tip_shape = StealthTip, stroke_width = 2.5, buff = 0, tip_length = 0.07).shift(RIGHT * 0.04)

        angle = arrow_8.get_angle()

        label_arrow_8 = MathTex("0", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 80).move_to(arrow_8.point_from_proportion(0.5)).rotate(angle - PI).shift(UP * 0.25)

        label_arrow_8.scale(0.4)

        arrow_8_with_label = VGroup(arrow_8, label_arrow_8)

        # ARROW 9

        arrow_9 = make_arrow(start = b_right, end =b_right_right, label = "1", scale_label = 0.4)

        # ARROW 10

        #arrow_10 = make_curved_arrow_top(start_node = a_top, end_node = a_top, color = text_black, label = "0", radius = 0.22, label_scale = 0.4).shift(0.03 * RIGHT)

        arrow_10 = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6 , angle = 5*PI/4, stroke_width = 3, start_node = a_top, color = text_black, label = "0,1", label_scale = 0.4, label_shift = 0.05).shift(0.03 * RIGHT + UP * 0.13)

    # Triangle 
        triangle = Triangle(color = text_black, fill_opacity=1).rotate(270*DEGREES)
        triangle.scale(0.3).shift(LEFT * 5.77 + DOWN * 0.25)

    # Label
        image_label = MathTex("D_a", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 80).move_to([5,2,0])
   
        all_nodes = VGroup(a_left, b_right, a_bot, a_top, b_right_right)
       
        all_arrows = VGroup(arrow_1_with_label, arrow_2_with_label,arrow_3_with_label, arrow_4, arrow_5, arrow_9, arrow_6_with_label, arrow_7_with_label, arrow_8_with_label, arrow_10)       
        #all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8)

        all_objects = VGroup(all_arrows, all_nodes, triangle, circle_a_left, circle_a_bot, circle_a_top, image_label).center()
        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())

        
with tempconfig({"preview": False}):
    scene = Graph()
    scene.render()
