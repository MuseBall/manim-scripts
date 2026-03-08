"""
TIME : 11:20 - 11:55


Guille - Reward Hypothesis - Dovetail Project

Images for Section in Set - Order representation - Preorder and Debreu separable - Debreu-Fishburns theorem
Figure 16: Constrained MDP and no independence

Generate image by simple running script:
python ./figure15.py
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

    # Triangle left

        polygon_3 = Polygon(
            [-1.6, 0.1, 0],
            [-1.6, 0.1, 0],
            [0.2, 0.1, 0],
            [0.2, 0.3, 0],
            [1.6, 1, 0],
            [1.6, 0.1, 0],
            color = node_blue, fill_opacity = 1).set_sheen(0.5, DL).set_stroke(text_black, 2)

        line_polygon3 = Line([-1.6, 0.7,0], [0.2, 0.7 ,0], stroke_color = text_black, stroke_width = 2).shift(DOWN * 2)

        line_polygon3_2 = Line([0.2, 0.7, 0], [1.7, 1.6 ,0], stroke_color = text_black, stroke_width = 2)

        y_3 = Dot(line_polygon3.point_from_proportion(0.8), color = node_purple, stroke_color = text_black, stroke_width = 1)
        label_y3 = MathTex("y", font_size = 50).scale(0.6).set_color(text_black).next_to(y_3, UP)

        x_3 = Dot(line_polygon3.point_from_proportion(0.5), color = node_orange, stroke_color = text_black, stroke_width = 1)
        label_x3 = MathTex("x", font_size = 50).scale(0.6).set_color(text_black).next_to(x_3, UP)

        y_32 = Dot(line_polygon3_2.point_from_proportion(0.5), color = node_blue, stroke_color = text_black, stroke_width = 1)
        label_y32 = MathTex(r"\frac{1}{2} y + \frac{1}{2} z", font_size = 40).scale(0.6).set_color(text_black).next_to(y_32, UP).shift(RIGHT * 0.3 + UP * 0.2)

        x_32 = Dot(line_polygon3_2.point_from_proportion(0.2), color = node_blue, stroke_color = text_black, stroke_width = 1)
        label_x32 = MathTex(r"\frac{1}{2} x + \frac{1}{2} z", font_size = 40).scale(0.6).set_color(text_black).next_to(x_32, UP).shift(UP * 0.1 + LEFT * 0.2)

        z_32 = Dot(line_polygon3_2.point_from_proportion(0.99), color = node_green, stroke_color = text_black, stroke_width = 1)
        label_z32 = MathTex("z", font_size = 50).scale(0.6).set_color(text_black).next_to(z_32, RIGHT)

        axes2 = Axes(x_range =[-1,1], x_length= 3.5, tips = False, x_axis_config={"include_numbers": False, "include_ticks": True}, axis_config = {"tip_shape": None, "color": text_black}).next_to(polygon_3, DOWN).shift(UP * 3.15)

        axes2.y_axis.set_opacity(0)

        labels_axes2 = axes2.get_axis_labels(MathTex("", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes2[0].set_opacity(0)
        labels_axes2[1].set_opacity(0)

    # Triangle right bottom
        
        triangle_4 = Polygon(
            [-1.8, 0.1, 0],
            [-0.4, 1, 0],
            [1.8, 0.1, 0],
            color = node_blue, 
            fill_opacity = 1).set_sheen(0.5, LEFT).set_stroke(text_black, 2)

        triangle_5 = Polygon(
            [-0.4, 0.6, 0],
            [2, 1.5, 0],
            [0, 1.5 ,0]
            ).set_stroke(text_black, 2)

        triangle_6 = Polygon(
            [-1.6, 0.7, 0],
            [-0.4, 0.6, 0],
            [0, 1.5, 0]
            ).set_stroke(text_black, 2).shift(DOWN * 2)

        line_triangle_5 = Line([-0.4, 0.6, 0], [0, 1.5 ,0], stroke_color = text_black, stroke_width = 2)

        line_triangle_4 = Line([-0.15, 1.2 ,0], [1.2, 1.4 ,0], stroke_color = text_black, stroke_width = 2)

        line_triangle_6 = Line([-0.6, 1.1, 0], [-0.15, 1.2 ,0], stroke_color = text_black, stroke_width = 2).shift(DOWN * 2)

        y_4 = Dot(line_triangle_6.point_from_proportion(0.4), color = node_purple, stroke_color = text_black, stroke_width = 1)

        x_4 = Dot(line_triangle_6.point_from_proportion(0.8), color = node_orange, stroke_color = text_black, stroke_width = 1)

        y_42 = Dot(line_triangle_4.point_from_proportion(0.35), color = node_blue, stroke_color = text_black, stroke_width = 1)

        x_42 = Dot(line_triangle_4.point_from_proportion(0.7), color = node_blue, stroke_color = text_black, stroke_width = 1)


        line_x_4 = DashedLine([3, -1.5,0], [3,-1,0], dash_length=0.15, color="#739b99", stroke_width=3)
        line_y_4 = DashedLine([1,-3,0], [1,-2,0] , dash_length=0.15, color="#739b99", stroke_width=3)
        line_z_4 = DashedLine([5,-3,0], [5,-1,0], dash_length=0.15, color="#739b99", stroke_width=3)

        label_x4 = MathTex("x", font_size = 60).scale(0.6).set_color(text_black).next_to(line_x_4, RIGHT)
        label_y4 = MathTex("y", font_size = 60).scale(0.6).set_color(text_black).next_to(line_y_4, DOWN)
        label_z4 = MathTex("z", font_size = 60).scale(0.6).set_color(text_black).next_to(line_z_4, DOWN)
        

        label_top = Tex("Constrained MDP", font_size = 75).scale(0.6).set_color(text_black).move_to([-1.5,3,0])

        label_inf = MathTex("- \infty", font_size = 60).scale(0.6).set_color(text_black).next_to(line_polygon3, LEFT)

        inf = label_inf.copy().next_to(triangle_6, LEFT)

        triangle_left = VGroup(polygon_3, line_polygon3, line_polygon3_2, y_3, x_3, y_32, x_32, z_32, label_y3, label_y32, label_x3, label_x32, label_z32, axes2, label_inf).to_edge(LEFT).shift(LEFT * 0.5)


        triangle_right = VGroup(line_triangle_6, triangle_4, triangle_5, line_triangle_5, triangle_6, line_triangle_4, x_4,y_4,x_42,y_42, inf).to_edge(LEFT).shift(RIGHT * 5.5)
    
        all_ = VGroup(triangle_left, triangle_right, label_top).center()

        self.add(all_)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
