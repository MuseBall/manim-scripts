"""
TIME : 10:30 - 11:30
        15:50 - 17:30


Guille - Reward Hypothesis - Dovetail Project

Images for Section in Set - Order representation - Preorder and Debreu separable - Debreu-Fishburns theorem
Figure 14: Expected utility

Generate image by simple running script:
python ./figure14.py
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


    # Triangle

        triangle_1 = Polygon(
            [-1.8, 0.1, 0],
            [-1.8, 0.5, 0],
            [1.8, 0.1, 0],
            color = node_blue, fill_opacity = 1).set_stroke(text_black, 2).set_sheen(0.5, RIGHT)

    #Lines in graph

        line_xy = DashedLine(point_x + RIGHT * 1.5 + UP * 0.1, point_x + RIGHT * 1.5 + DOWN * 0.2, dash_length=0.15, color=text_black, stroke_width=3)

        label_line = MathTex(r"px + (1-p)y", font_size = 60).scale(0.6).set_color(text_black).next_to(line_xy, DOWN)

        label_left_bot = MathTex(f"x,y \in X", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([-2,-3,0])        
        
        label_right_bot = MathTex(f"x,y,z \in X", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([3,-3,0])

    # Axes

        axes_1 = Axes(x_range =[-0.5,3.5], y_range = [-0.5,3], x_length= 4, y_length = 3, x_axis_config={"include_numbers": False, "include_ticks": False}, y_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": StealthTip, "color": text_black})

        labels_axes_1 = axes_1.get_axis_labels(MathTex("X", color = text_black, stroke_width = 1.5).scale(0.8), MathTex(r"f(x) \in \mathbb{R}", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes_1[0].next_to(axes_1.get_x_axis().get_right(), RIGHT)
        labels_axes_1[1].next_to(axes_1.get_y_axis().get_top(), UP)

    # Points in graph

        point_x_1 = axes_1.coords_to_point(0.5, 2)
        point_y_1 = axes_1.coords_to_point(2.5, 1.1)

        dot_x_1 = Dot(point_x_1, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y_1 = Dot(point_y_1, color = node_purple, stroke_color = text_black, stroke_width = 1)

        linexy_1 = Line(point_x_1, point_y_1, color = text_black, stroke_width = 3)

        line_x_1 = DashedLine(point_x_1, point_x_1  + DOWN * 1.7, dash_length=0.15, color="#739b99", stroke_width=3)
        line_y_1 = DashedLine(point_y_1, point_y_1 + DOWN * 0.9, dash_length=0.15, color="#739b99", stroke_width=3)

        label_x_1 = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(line_x_1, DOWN)
        label_y_1 = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(line_y_1, DOWN)


    # Triangle bottom left

        triangle_3 = Polygon(
            [-4, -1, 0],
            [-5.5, -3, 0],
            [-2.5, -3, 0],
            color = node_blue, fill_opacity = 1).set_stroke(text_black, 2).set_sheen(0.5, DL)

        x_3,y_3,z_3 = triangle_3.get_vertices()

        dot_x3_tri = Dot(x_3, color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_y3_tri = Dot(y_3, color = node_green, stroke_color = text_black, stroke_width = 1)
        dot_z3_tri = Dot(z_3, color = node_orange, stroke_color = text_black, stroke_width = 1)

        label_x3_tri = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(x_3, UP)
        label_y3_tri = MathTex("z", font_size = 60).scale(0.6).set_color(text_black).next_to(y_3, DOWN)
        label_z3_tri = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(z_3, DOWN)

        label_zx = MathTex("\succeq", font_size = 70).scale(0.6).set_color(text_black).next_to(label_z3_tri, LEFT).shift(LEFT * 1)

    # Triangle bottom right

        triangle_4 = Polygon(
            [3, -1.5, 0],
            [1, -3, 0],
            [5, -3, 0]
            ).set_stroke(text_black, 2)


        triangle_5 = Polygon(
            [3, -1, 0],
            [1, -2, 0],
            [5, -1, 0]
            ).set_stroke(text_black, 2)

        line_x_4 = DashedLine([3, -1.5,0], [3,-1,0], dash_length=0.15, color="#739b99", stroke_width=3)
        line_y_4 = DashedLine([1,-3,0], [1,-2,0] , dash_length=0.15, color="#739b99", stroke_width=3)
        line_z_4 = DashedLine([5,-3,0], [5,-1,0], dash_length=0.15, color="#739b99", stroke_width=3)

        label_x4 = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(line_x_4, RIGHT)
        label_y4 = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(line_y_4, DOWN)
        label_z4 = MathTex("z", font_size = 60).scale(0.6).set_color(text_black).next_to(line_z_4, DOWN)
        

        label_right = MathTex(r"x \succeq y", font_size = 70).scale(0.6).set_color(text_black).move_to([-4,-3.2,0])

        label_left = MathTex(r"f(x) \geq f(y)", font_size = 70).scale(0.6).set_color(text_black).move_to([3.2,-3.2,0])

        label_left_1 = MathTex(r"f(\sum_i p_i x_i) = \sum_i p_i f(x_i)", font_size = 70).scale(0.6).set_color(text_black).move_to([3.5,-4.1,0])

        label_mid = MathTex(r"\Longleftrightarrow", font_size = 100).scale(0.6).set_color(text_black).move_to([-0.5,-3.2,0])

        triangle_right_top = VGroup(axes, dot_x, dot_y, labels_axes, label_x, label_y,label_line, triangle_1).to_edge(UL).shift(UP * 1.7 + RIGHT * 1)

        graph_left_top = VGroup(linexy_1, axes_1, labels_axes_1, dot_x_1, dot_y_1, label_x_1, label_y_1, line_x_1, line_y_1).to_corner(UR).shift(LEFT * 1 + UP * 0.5).scale(0.85)

        triangle_left_bottom = VGroup(triangle_3, dot_x3_tri, dot_y3_tri, dot_z3_tri, label_x3_tri, label_y3_tri, label_z3_tri,label_zx).shift(UP * 0.9)

        triangle_right_bottom = VGroup(triangle_4, triangle_5, line_x_4, line_y_4, line_z_4, label_x4, label_y4, label_z4).shift(UP * 0.9)

        all_ = VGroup(triangle_right_top, graph_left_top, triangle_right_bottom, triangle_left_bottom, label_right, label_left, label_left_1, label_mid).scale(0.9).center().shift(UP * 0.7)

        self.add(all_)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
