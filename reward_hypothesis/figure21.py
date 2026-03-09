"""
TIME : 19:20 - 20:30

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 21: Dynamic Consistencies

Generate image by simple running script:
python ./figure21.py
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

    #Axes 1

        axes = Axes(x_range =[-1.5,3.5], x_length= 2.5, tips = False, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": None, "color": text_black})

        axes.y_axis.set_opacity(0)

        labels_axes = axes.get_axis_labels(MathTex(r"(\mathbb{R}, >)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes[0].set_opacity(0)
        labels_axes[1].set_opacity(0)

    # Points in graph 1

        point_x = axes.coords_to_point(-1.5, 0)
        point_y = axes.coords_to_point(3.5, 0)

        dot_x = Dot(point_x, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y = Dot(point_y, color = node_purple, stroke_color = text_black, stroke_width = 1)


    # Triangle 1

        triangle_1 = Polygon(
            [-1, 0.1, 0],
            [1, 0.3, 0],
            [1, 0.1, 0],
            color = node_blue, fill_opacity = 1).set_stroke(text_black, 2).set_sheen(0.5, LEFT)

        line1 = Line([-1, 0.3,0], [1, 0.5, 0], stroke_color = text_black, stroke_width = 2)

    #Axes 2

        axes2 = Axes(x_range =[-1.5,3.5], x_length= 2.5, tips = False, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": None, "color": text_black})

        axes2.y_axis.set_opacity(0)

        labels_axes2 = axes2.get_axis_labels(MathTex(r"(\mathbb{R}, >)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes2[0].set_opacity(0)
        labels_axes2[1].set_opacity(0)

    # Points in graph 2

        point_x2 = axes2.coords_to_point(-1.5, 0)
        point_y2 = axes2.coords_to_point(3.5, 0)

        dot_x2 = Dot(point_x, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y2 = Dot(point_y, color = node_purple, stroke_color = text_black, stroke_width = 1)


    # Triangle 2

        triangle_2 = Polygon(
            [-1, 0.1, 0],
            [-1, 0.6, 0],
            [1, 0.1, 0],
            color = node_blue, fill_opacity = 1).set_stroke(text_black, 2).set_sheen(0.5, RIGHT)

        line2 = Line([1, 0.3,0], [-1, 0.8, 0], stroke_color = text_black, stroke_width = 2)

    #Axes 3

        axes3 = Axes(x_range =[-1.5,3.5], x_length= 2.5, tips = False, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": None, "color": text_black})

        axes3.y_axis.set_opacity(0)

        labels_axes3 = axes.get_axis_labels(MathTex(r"(\mathbb{R}, >)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes3[0].set_opacity(0)
        labels_axes3[1].set_opacity(0)

    # Points in graph 3

        point_x3 = axes3.coords_to_point(-1.5, 0)
        point_y3 = axes3.coords_to_point(3.5, 0)

        dot_x3 = Dot(point_x3, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y3 = Dot(point_y3, color = node_purple, stroke_color = text_black, stroke_width = 1)


    # Triangle 3

        triangle_3 = Polygon(
            [-1, 0.1, 0],
            [-1, 0.6, 0],
            [1, 0.1, 0],
            color = node_blue, fill_opacity = 1).set_stroke(text_black, 2).set_sheen(0.5, RIGHT)

        line3 = Line([1, 0.3,0], [-1, 0.8, 0], stroke_color = text_black, stroke_width = 2)

    #Axes 4

        axes4 = Axes(x_range =[-1.5,3.5], x_length= 2.5, tips = False, x_axis_config={"include_numbers": False, "include_ticks": False}, axis_config = {"tip_shape": None, "color": text_black})

        axes4.y_axis.set_opacity(0)

        labels_axes4 = axes4.get_axis_labels(MathTex(r"(\mathbb{R}, >)", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes4[0].set_opacity(0)
        labels_axes4[1].set_opacity(0)

    # Points in graph 4

        point_x4 = axes4.coords_to_point(-1.5, 0)
        point_y4 = axes4.coords_to_point(3.5, 0)

        dot_x4 = Dot(point_x4, color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_y4 = Dot(point_y4, color = node_purple, stroke_color = text_black, stroke_width = 1)


    # Triangle 4

        triangle_4 = Polygon(
            [-1, 0.1, 0],
            [-1, 0.3, 0],
            [1, 0.1, 0],
            color = node_blue, fill_opacity = 1).set_stroke(text_black, 2).set_sheen(0.5, RIGHT)

        line4 = Line([1, 0.3,0], [-1, 0.5, 0], stroke_color = text_black, stroke_width = 2)

    # Bottom triangles

    # Triangle 5  

        triangle5 = Polygon(
            [0,0.8,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1
            ).set_sheen(0.5, LEFT)

        triangle5top = Polygon(
            [0,1.5,0],
            [-1.5, -0.5,0],
            [1.5, 1, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

    # Triangle 6  

        triangle6 = Polygon(
            [0,0.8,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1
            ).set_sheen(0.5, RIGHT)

        triangle6top = Polygon(
            [0,1.5,0],
            [-1.5, 0.8,0],
            [1.5, -0.5, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

    # Triangle 7  

        triangle7 = Polygon(
            [0,0.8,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1
            ).set_sheen(0.5, LEFT)

        triangle7top = Polygon(
            [0,1.5,0],
            [-1.5, -0.5,0],
            [1.7, 0.6, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

    # Triangle 8  

        triangle8 = Polygon(
            [0,0.8,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1
            ).set_sheen(0.5, LEFT)

        triangle8top = Polygon(
            [0,1.2,0],
            [-1.5, -0.5,0],
            [1.7, 0.9, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

        label_left = Tex("Not Dynamically \\\\ Consistent", color = text_black, font_size = 70, stroke_width = 1.5).scale(0.6).to_edge(UL).shift(RIGHT * 1.5)

        label_right = Tex("Dynamically \\\\ Consistent", color = text_black, font_size = 70, stroke_width = 1.5).scale(0.6).to_edge(UR).shift(LEFT * 1.5)


        triangle_right_top = VGroup(line3, axes3, dot_x3, dot_y3, labels_axes3,  triangle_3).to_edge(UR).shift(LEFT * 2 + UP * 1)

        triangle_right_top2 = VGroup(line4, axes4, dot_x4, dot_y4, labels_axes4, triangle_4).to_edge(UR).shift(RIGHT * 1 + UP * 1)

        triangle_left_top = VGroup(line1, axes, dot_x, dot_y, labels_axes, triangle_1).to_edge(UL).shift(RIGHT * 3 + UP * 1)

        triangle_left_top2 = VGroup(line2, axes2, dot_x2, dot_y2, labels_axes2, triangle_2).to_edge(UL).shift(UP * 1)

        triangle_left_bot = VGroup(triangle5, triangle5top).to_edge(DL).shift(UP * 1)

        triangle_left_bot2 = VGroup(triangle6, triangle6top).to_edge(DL).shift(RIGHT * 3.2 + UP * 1)

        triangle_right_bot = VGroup(triangle7, triangle7top).to_edge(DR).shift(LEFT * 3.2 + UP * 1)

        triangle_right_bot2 = VGroup(triangle8, triangle8top).to_edge(DR).shift(UP * 1)


        self.add(triangle_right_top, triangle_right_top2, triangle_left_top, triangle_left_top2, triangle_left_bot, triangle_left_bot2, triangle_right_bot, triangle_right_bot2, label_right, label_left)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
