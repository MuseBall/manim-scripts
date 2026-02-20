"""
TIME : 10:10 - 13:00
        18:15 - 20:50

Robust Finite Policies are Nontrivially Structured
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Animated Image for Section in Atomic Classifiers
Fig Caption: An atomic classifier sending the string 10 to a unique end state

Generate image by simple running script:
python ./dfc_animation.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_self_loop_right

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = config.pixel_height / config.pixel_width * config.frame_width

class Graph(Scene):
    def make_node(self, position, label="x", radius=0.3, node_color="#e1c180", text_color="#22323b", fill_opacity = 1):
        circle = Circle(radius = radius, color = node_color, fill_opacity = fill_opacity, stroke_color = text_color, stroke_width = 1.8).move_to(position)
    
        shadow = Circle(radius = radius-0.01, color = text_color, fill_opacity = 1).move_to(position + DOWN * 0.015 + RIGHT * 0.015)
        
        border = Circle(radius = radius+0.02, color = "#dce2e1", fill_opacity = 0).move_to(position)
        label = MathTex(label, color = text_color, stroke_color = text_color, stroke_width = 1.3, font_size = 100).move_to(position)

        label.scale(radius)

        node = VGroup(shadow, circle, label)

        return node

    #def make_arrow(self, start, end, label = "x", buff=0.5, color = "#22323b", tip_shape = StealthTip, stroke_width = 7, tip_length = 0.25):

    def make_arrow(self, start, end, label="x", label_shift=0.2, color="#22323b", tip_shape = StealthTip):
        """
        start, end can be numpy arrays showing [x,y,z] or any mobject whose position will be taken by Arrow().
        In this case, it can be node objects from make_node()
        """
        
        arrow = Arrow(start = start, end = end, color = color, tip_shape = tip_shape, stroke_width = 2.5, buff = 0, tip_length = 0.07).shift(LEFT * 0.04)

        angle = arrow.get_angle()

        #label_arrow = Text(label, weight = BOLD, color = color).next_to(arrow.get_center())
        label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(arrow.point_from_proportion(0.5)).rotate(angle).shift(UP * label_shift)

        label_arrow.scale(0.3)

        arrow_with_label = VGroup(arrow, label_arrow)

        return arrow_with_label, label_arrow

    def make_curved_arrow(self, node, color, label):
        """
        node is a vgroup object returned by make_node()
        """
        start = node.get_right() + DOWN * 0.15 
        end = node.get_right() + UP * 0.15
        carrow = CurvedArrow(start_point = start , end_point = end, radius=0.15, color = color, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)
        label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(carrow.point_from_proportion(0.5)).shift( RIGHT * 0.3)

        label_arrow.scale(0.3)

        carrow_with_label = VGroup(carrow, label_arrow)

        return carrow_with_label

    def construct(self):

        # hex code of colours
        self.camera.background_color = "#ffffff" 
        text_black = "#22323b"
        #text_black_fade = "#5a869f"
        text_black_fade = "#86a8bf"
        node_yellow = "#e1c180"
        node_green = "#a9c199"
        node_blue = "#9acecc"
        node_orange = "#d49870"
        node_red = "#d67f86"
        node_purple = "#b6b3c4"
        


        # background rectangle with rounded corners
        background_rectangle = RoundedRectangle(color = "#d6e2e2", fill_opacity = 1, corner_radius = 0.7, 
                                                height = 8, width = 8)

        # Nodes 
        d_left = self.make_node(position=[-3,0,0], label="d")

        d_top = self.make_node(position=[-1.5, 1, 0], label="d")

        d_bot = self.make_node(position=[-1.5, -1, 0], label="d")

        a1_top = self.make_node(position=[0,1.5,0], label="a_1", node_color=node_orange) 

        a2_top = self.make_node(position=[0,0.5,0], label="a_2", node_color=node_green) 

        a1_bot = self.make_node(position=[0,-0.5,0], label="a_1", node_color=node_orange) 

        a3_bot = self.make_node(position=[0,-1.5,0], label="a_3", node_color=node_purple) 

        d_right = self.make_node(position=[3,0,0], label="d") 
        

        # Arrows
        arrow_1 = self.make_arrow(start = d_left, end = d_top, label = "0")
        
        arrow_2, arrow_2_label = self.make_arrow(start = d_left, end = d_bot, label = "1")

        arrow_3 = self.make_arrow(start = d_top, end = a1_top, label = "0")
        
        arrow_4 = self.make_arrow(start = d_top, end = a2_top ,label = "1")
     
        arrow_5, arrow_5_label = self.make_arrow(start = d_bot, end = a1_bot, label = "0")
  
        arrow_6 = self.make_arrow(start = d_bot, end = a3_bot, label = "1")
   
        arrow_7 = self.make_arrow(start = a1_top, end = d_right, label = "0, 1", label_shift=0.15)
        
        arrow_8, arrow_8_label = self.make_arrow(start = a2_top, end = d_right, label = "0, 1", label_shift=0.14)

        arrow_8.shift(UP * 0.07)
       
        arrow_9, arrow_9_label = self.make_arrow(start = a1_bot, end = d_right, label = "0, 1", label_shift=0.13)

        arrow_9.shift(DOWN * 0.07)
   
        arrow_10 = self.make_arrow(start = a3_bot, end = d_right,label = "0, 1", label_shift=0.12)

        arrow_11 = make_self_loop_right(radius = 0.22, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = d_right, color = text_black, label = "0,1", label_scale = 0.4, label_shift = UP * 0.15).shift(0.09 * RIGHT + UP * 0.09).rotate(-PI/2).shift(RIGHT * 0.3 + DOWN * 0.35)

        # Triangle 
        triangle = Triangle(color = text_black, fill_opacity=1).rotate(270*DEGREES)
        triangle.scale(0.2).shift(LEFT * 3.5 + DOWN * 0.25)

        
        all_nodes = VGroup(d_left, d_top, d_bot, d_right, a1_top, a2_top, a1_bot, a3_bot)
       
        all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8, arrow_9, arrow_10, arrow_11)

        all_objects = VGroup(all_arrows, all_nodes, triangle)

        all_objects.shift(LEFT * 2)

        self.add(all_objects)

        # Animation Objects

        #node_animate = d_left.copy().scale(1.5)
        triangle_animate = triangle.copy().scale(1.5).shift(LEFT * 0.23).move_to([4.5,2,0])

        #animate_object = VGroup(node_animate, triangle_animate).move_to([4.5,2,0])

        #selected_node = self.make_node(position=[-5,0,0], label="d", node_color="#5c86a0", fill_opacity = 1)

        selected_node = Circle(radius = 0.4, stroke_color ="#6da4c9", color = "#6da4c9", fill_opacity = 1, stroke_width = 2).move_to([-5,0,0])

        input_1 = MathTex("1", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 70).shift([4, 0.75, 0])

        input_1_faded = MathTex("1", color = text_black_fade, stroke_color = text_black_fade, stroke_width = 1.3, font_size = 70).shift([4, 0.75, 0])

        input_0 = MathTex("0", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 70).shift([5, 0.75, 0])

        input_0_faded = MathTex("0", color = text_black_fade, stroke_color = text_black_fade, stroke_width = 1.3, font_size = 70).shift([5, 0.75, 0])

        self.add(input_1_faded, input_1, input_0_faded, input_0, selected_node, all_objects)

        d_left_and_triangle = VGroup(d_left.copy(), triangle.copy())
        d_bot_copy = d_bot.copy()

        #debug distance of objects with a grid
        #self.add(NumberPlane())

        self.play(FadeIn(selected_node))
        self.wait(0.05)
        self.play(selected_node.animate.scale(1.2))
        self.wait(0.05)
        self.play(selected_node.animate.scale(1/1.2))
        self.wait(0.5)
        self.play(FadeIn(d_left_and_triangle.move_to([4.5,2,0]).scale(1.5)))
        self.wait(0.5)

        self.play(Transform(input_1.copy(), arrow_2_label.copy()), FadeOut(input_1))
        self.wait(1)

        self.play(selected_node.animate.move_to([-3.5, -1, 0]))
        self.wait(0.05)

        self.play(selected_node.animate.scale(1.2), FadeOut(d_left_and_triangle))
        self.wait(0.05)

        self.play(selected_node.animate.scale(1/1.2), FadeIn(d_bot_copy.move_to([4.5,2,0]).scale(1.5)))
        self.wait(0.5)


        self.play(Transform(input_0.copy(), arrow_5_label.copy()), FadeOut(input_0))
        self.wait(1)

        self.play(selected_node.animate.move_to([-2, -0.5, 0]))
        self.wait(0.05)
        self.play(selected_node.animate.scale(1.2), FadeOut(d_bot_copy))
        self.wait(0.05)
        self.play(selected_node.animate.scale(1/1.2), a1_bot.copy().animate.move_to([4.5,2,0]).scale(1.5))

        self.wait(3)



with tempconfig({"preview": False}):
    scene = Graph()
    scene.render()


