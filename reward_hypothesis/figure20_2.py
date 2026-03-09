"""
TIME : 17:00 - 17:50

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 20: Reward fuction

Generate image by simple running script:
python ./figure20_2.py
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

    # Traingle 1

        triangle1 = Polygon(
            [0,1,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity =1).set_sheen(0.5, LEFT)

        dot_x1 = Dot([0,1,0], color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_y1 = Dot([-1.5, -1, 0], color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_z1 = Dot([1.5, -1, 0], color = node_green, stroke_color = text_black, stroke_width = 1)

        x1 = MathTex("x", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_x1, UP)
        y1 = MathTex("y", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_y1, DOWN)
        z1 = MathTex("z", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_z1, DOWN)

        triangle_1 = VGroup(triangle1, dot_x1, dot_y1, dot_z1, x1, y1, z1).shift(LEFT * 5)

    # Traingle 2

        triangle2 = Polygon(
            [0,1,0],
            [-1.2, -1,0],
            [1.2, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1).set_sheen(0.5, LEFT)

        dot_x2 = Dot([0,1,0], color = node_purple, stroke_color = text_black, stroke_width = 1)
        dot_y2 = Dot([-1.2, -1, 0], color = node_orange, stroke_color = text_black, stroke_width = 1)
        dot_z2 = Dot([1.2, -1, 0], color = node_green, stroke_color = text_black, stroke_width = 1)

        x2 = MathTex(r"t \cdot_T x", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_x2, UP)
        y2 = MathTex(r"t \cdot_T y", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_y2, DOWN)
        z2 = MathTex(r"t \cdot_T z", color = text_black, stroke_width = 1.5, font_size = 60).scale(0.6).next_to(dot_z2, DOWN)

        triangle_2 = VGroup(triangle2, dot_x2, dot_y2, dot_z2, x2, y2, z2).shift(LEFT * 1.5)


    # Traingle 3

        triangle3 = Polygon(
            [0,1,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

        triangle3top = Polygon(
            [0,1.8,0],
            [-1.5, -0.2,0],
            [1.5, 1.7, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

        line_x3 = DashedLine(
            [0,1,0],
            [0,1.8,0],
            dash_length=0.15, 
            color="#739b99", 
            stroke_width=3
            )

        line_y3 = DashedLine(
            [-1.5,-1,0],
            [-1.5,-0.2,0],
            dash_length=0.15, 
            color="#739b99", 
            stroke_width=3
            )

        line_z3 = DashedLine(
            [1.5, -1, 0],
            [1.5, 1.7, 0],
            dash_length=0.15, 
            color="#739b99", 
            stroke_width=3
            )

        dot_x3 = Dot(
            [0,1,0],
            color = node_purple,
            stroke_color = text_black,
            stroke_width = 1
            )

        dot_y3 = Dot(
            [-1.5, -1, 0],
            color = node_orange, 
            stroke_color = text_black, 
            stroke_width = 1
            )

        dot_z3 = Dot(
            [1.5, -1, 0], 
            color = node_green, 
            stroke_color = text_black, 
            stroke_width = 1
            )

        x3 = MathTex(
            "x", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 60
            ).scale(0.6).next_to(dot_x3, UR)

        y3 = MathTex(
            "y", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 60
            ).scale(0.6).next_to(dot_y3, DOWN)

        z3 = MathTex(
            "z", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 60
            ).scale(0.6).next_to(dot_z3, DOWN)

        triangle_3 = VGroup(line_x3,line_y3,line_z3,triangle3, triangle3top, dot_x3, dot_y3, dot_z3, x3, y3, z3).shift(RIGHT * 1.9)

    # Traingle 4

        triangle4 = Polygon(
            [0,1,0],
            [-1.2, -1,0],
            [1.2, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )
        
        triangle4top = Polygon(
            [0,1.8,0],
            [-1.2, -0.2,0],
            [1.2, 1.7, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

        line_x4 = DashedLine(
            [0,1,0],
            [0,1.8,0],
            dash_length=0.15, 
            color="#739b99", 
            stroke_width=3
            )

        line_y4 = DashedLine(
            [-1.2,-1,0],
            [-1.2,-0.2,0],
            dash_length=0.15, 
            color="#739b99", 
            stroke_width=3
            )

        line_z4 = DashedLine(
            [1.2, -1, 0],
            [1.2, 1.7, 0],
            dash_length=0.15, 
            color="#739b99", 
            stroke_width=3
            )

        dot_x4 = Dot(
            [0,1,0],
            color = node_purple,
            stroke_color = text_black,
            stroke_width = 1
            )
        dot_y4 = Dot(
            [-1.2, -1, 0],
            color = node_orange, 
            stroke_color = text_black, 
            stroke_width = 1
            )
        dot_z4 = Dot(
            [1.2, -1, 0], 
            color = node_green, 
            stroke_color = text_black, 
            stroke_width = 1
            )

        x4 = MathTex(
            r"t \cdot_T x", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 60
            ).scale(0.6).next_to(dot_x4, UR)

        y4 = MathTex(
            r"t \cdot_T y", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 60
            ).scale(0.6).next_to(dot_y4, DOWN)

        z4 = MathTex(
            r"t \cdot_T z", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 60
            ).scale(0.6).next_to(dot_z4, DOWN)

        triangle_4 = VGroup(line_x4, line_y4, line_z4, triangle4top, triangle4, dot_x4, dot_y4, dot_z4, x4, y4, z4).shift(RIGHT * 5.3)

        self.add(triangle_1, triangle_2, triangle_3, triangle_4)

        #debug distance of objects with a grid
        #self.add(NumberPlane())


