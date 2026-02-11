"""
Robust Finite Policies are Nontrivially Structured
post link: https://www.lesswrong.com/posts/ieX8nK2b2i4JDRH5s/robust-finite-policies-are-nontrivially-structured

Images for Section in Atomic Classifiers
Fig Caption: An atomic classifier for strings of length 2

Generate image by simple running script:
python ./atomic_class_l2.py
"""

from manim import *
import numpy as np

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = config.pixel_height / config.pixel_width * config.frame_width

class Graph(Scene):
    def make_node(self, position, label="x", radius=0.3, node_color="#e1c180", text_color="#22323b"):
        circle = Circle(radius = radius, color = node_color, fill_opacity = 1, stroke_color = text_color, stroke_width = 1.8).move_to(position)
    
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
        
        arrow = Arrow(start = start, end = end, color = color, tip_shape = tip_shape, stroke_width = 2.5, buff = 0, tip_length = 0.04).shift(LEFT * 0.04)

        angle = arrow.get_angle()

        #label_arrow = Text(label, weight = BOLD, color = color).next_to(arrow.get_center())
        label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(arrow.point_from_proportion(0.5)).rotate(angle).shift(UP * label_shift)

        label_arrow.scale(0.3)

        arrow_with_label = VGroup(arrow, label_arrow)

        return arrow_with_label

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
        d_left = self.make_node(position=[-3,0,0], label="d")

        d_top = self.make_node(position=[-1.5, 1, 0], label="d")

        d_bot = self.make_node(position=[-1.5, -1, 0], label="d")

        a1_top = self.make_node(position=[0,1.5,0], label="a_1", node_color=node_orange) 

        a2_top = self.make_node(position=[0,0.5,0], label="a_2", node_color=node_green) 

        a1_bot = self.make_node(position=[0,-0.5,0], label="a_1", node_color=node_orange) 

        a1_bot_bot = self.make_node(position=[0,-1.5,0], label="a_1", node_color=node_orange) 

        d_right = self.make_node(position=[3,0,0], label="d") 
        

        # Arrows
        arrow_1 = self.make_arrow(start = d_left, end = d_top, label = "0")
        
        arrow_2 = self.make_arrow(start = d_left, end = d_bot, label = "1")

        arrow_3 = self.make_arrow(start = d_top, end = a1_top, label = "0")
        
        arrow_4 = self.make_arrow(start = d_top, end = a2_top ,label = "1")
     
        arrow_5 = self.make_arrow(start = d_bot, end = a1_bot, label = "0")
  
        arrow_6 = self.make_arrow(start = d_bot, end = a1_bot_bot, label = "1")
   
        arrow_7 = self.make_arrow(start = a1_top, end = d_right, label = "0, 1", label_shift=0.15)
        
        arrow_8 = self.make_arrow(start = a2_top, end = d_right, label = "0, 1", label_shift=0.14).shift(UP * 0.07)
       
        arrow_9 = self.make_arrow(start = a1_bot, end = d_right, label = "0, 1", label_shift=0.13).shift(DOWN * 0.07)
   
        arrow_10 = self.make_arrow(start = a1_bot_bot, end = d_right,label = "0, 1", label_shift=0.12)

        arrow_11 = self.make_curved_arrow(d_right, color=text_black, label= "0, 1")

        


        all_nodes = VGroup(d_left, d_top, d_bot, d_right, a1_top, a2_top, a1_bot, a1_bot_bot)
       
        all_arrows = VGroup(arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8, arrow_9, arrow_10, arrow_11)

        all_objects = VGroup(all_arrows, all_nodes).center()

        self.add(all_objects)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())



with tempconfig({"preview": False}):
    scene = Graph()
    scene.render()


