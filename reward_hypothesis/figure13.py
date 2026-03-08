"""
TIME : 17:40 - 19:00

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Mixture space - Expected utility - Indepen-
dence and Continuity - vNM theorem
Figure 13: Mixture space

Generate image by simple running script:
python ./figure13.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_arrow


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

    #Axes

        axes = Axes(x_range =[-1.5,3.5], x_length= 4, tips = False, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": None, "color": text_black})

        axes.y_axis.set_opacity(0)

        labels_axes = axes.get_axis_labels(MathTex(r"(\mathbb{R}, >)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes[0].set_opacity(0)
        labels_axes[1].set_opacity(0)

    # Points in graph

        point_x = axes.coords_to_point(-1.5, 0)
        point_y = axes.coords_to_point(3.5, 0)

        dot_x = Dot(point_x, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y = Dot(point_y, color = node_purple, stroke_color = text_black, stroke_width = 1)

        label_x = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_x, DOWN)
        label_y = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_y, DOWN)


    #Lines in graph

        line_xy = DashedLine(point_x + RIGHT * 1.5 + UP * 0.1, point_x + RIGHT * 1.5 + DOWN * 0.2, dash_length=0.15, color=text_black, stroke_width=3)

        label_line = MathTex(r"px + (1-p)y", font_size = 60).scale(0.6).set_color(text_black).next_to(line_xy, DOWN)


        bracket1 = BraceBetweenPoints(point_x, line_xy.get_top(),[0,1,0], color =text_black, stroke_width = 0.01)
        p1 = MathTex(r"p", font_size = 60).scale(0.6).set_color(text_black).next_to(bracket1, UP).scale(1.2)

        bracket2 = BraceBetweenPoints(line_xy.get_top(), point_y, [0,1,0], color = text_black, stroke_width = 0.01)
        p2 = MathTex(r"1-p", font_size = 60).scale(0.6).set_color(text_black).next_to(bracket2, UP).scale(1.2)


        triangle_1 = Triangle(color = text_black, stroke_width = 2).move_to([3,0,0]).scale(1.5)

        x,y,z = triangle_1.get_vertices()

        dot_x_tri = Dot(x, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y_tri = Dot(y, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_z_tri = Dot(z, color = node_green, stroke_color = text_black, stroke_width = 1)

        dot_xz = Dot((x+z)/2, color = node_blue, stroke_color = text_black, stroke_width = 1)
        label_xz = MathTex("px + (1-p)z", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_xz, RIGHT)

        dot_yz = Dot((y+z)/2, color = node_blue, stroke_color = text_black, stroke_width = 1).shift(UP * 0.4 + RIGHT * 0.5)
        label_yz = MathTex("p_x x + p_y y + (1-(p_x + p_y))z", font_size = 60).scale(0.6).set_color(text_black).next_to(dot_yz, DOWN).shift(DOWN * 0.7)

        arrow = make_arrow(start = dot_yz.get_bottom() + DOWN * 0.1, end = label_yz.get_top() + UP * 0.15 , label = "", color = text_black).shift(RIGHT * 0.04)

        label_x_tri = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(x, UP)
        label_y_tri = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(y, DOWN)
        label_z_tri = MathTex("z", font_size = 60).scale(0.6).set_color(text_black).next_to(z, DOWN)

        label_left_bot = MathTex(f"x,y \in X", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([-2,-3,0])        
        
        label_right_bot = MathTex(f"x,y,z \in X", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([3,-3,0])


        all_objects = VGroup(axes, line_xy, dot_x, dot_y, labels_axes, label_x, label_y,label_line, bracket1, p1, bracket2, p2).scale(0.8).shift(LEFT * 2 + DOWN * 1)
        all_ = VGroup(all_objects, triangle_1, label_x_tri, label_y_tri, label_z_tri, dot_x_tri, dot_y_tri, dot_z_tri, dot_xz, label_xz, dot_yz, label_yz, arrow, label_left_bot, label_right_bot).center()

        self.add(all_)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
