"""
TIME : 20:40 - 21:10

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 22: gamma - indifference

Generate image by simple running script:
python ./figure22.py
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

    # Triangle 1  

        triangle1 = Polygon(
            [0,0.8,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1
            ).set_sheen(0.5, LEFT)

        triangle1top = Polygon(
            [0,1.5,0],
            [-1.5, -0.5,0],
            [1.5, 1, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

    # Triangle 2  

        triangle2 = Polygon(
            [0,0.8,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1
            ).set_sheen(0.5, RIGHT)

        triangle2top = Polygon(
            [0,1.5,0],
            [-1.5, -0.5,0],
            [1.5, 0.6, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

    # Triangle 3  

        triangle3 = Polygon(
            [0,0.8,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1
            ).set_sheen(0.5, LEFT)

        triangle3top = Polygon(
            [0,1.5,0],
            [-1.5, -0.5,0],
            [1.7, 0.6, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

    # Triangle 4  

        triangle4 = Polygon(
            [0,0.8,0],
            [-1.5, -1,0],
            [1.5, -1, 0],
            stroke_color = text_black, 
            stroke_width = 2,
            color = node_blue,
            fill_opacity = 1
            ).set_sheen(0.5, LEFT)

        triangle4top = Polygon(
            [0,1.2,0],
            [-1.5, -0.6,0],
            [1.7, 0.9, 0],
            stroke_color = text_black, 
            stroke_width = 2
            )

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

        text1 = MathTex(r" \gamma - \text{Indifferent}", color = text_black).shift(UP * 0.7)
        text2 = MathTex(r"\Downarrow", color = text_black)
        text3 = MathTex(r"\text{Dynamically Consistent}", color = text_black).shift(DOWN * 0.7)

        text = VGroup(text1, text2, text3)


        triangle_left_bot = VGroup(triangle1, triangle1top).to_edge(LEFT).shift(UP * 1)

        triangle_left_bot2 = VGroup(triangle2, triangle2top).to_edge(LEFT).shift(RIGHT * 3.2 + UP * 1)

        triangle_right_bot = VGroup(triangle3, triangle3top).to_edge(RIGHT).shift(LEFT * 3.2 + UP * 1)

        triangle_right_bot2 = VGroup(triangle4, triangle4top).to_edge(RIGHT).shift(UP * 1)

        triangle_right_bot21 = VGroup(triangle5, triangle5top).to_edge(RIGHT).shift(UP * 1)

        triangle_right_bot22 = VGroup(triangle6, triangle6top).to_edge(RIGHT).shift(UP * 1 + LEFT * 3.2)

        all_=VGroup(triangle_left_bot, triangle_left_bot2, triangle_right_bot, triangle_right_bot2).center()

        left_top = VGroup(triangle_left_bot, triangle_left_bot2)
        right_top = VGroup(triangle_right_bot, triangle_right_bot2)
        right_bot = VGroup(triangle_right_bot21, triangle_right_bot22)



    # Table

        table = Table(
            [[left_top, right_top], [text, right_bot]],
            row_labels=[
                Tex("Dynamically \\\\ Consistent", color=text_black, font_size=65),
                Tex("Not \\\\ Dynamically \\\\ Consistent", color=text_black, font_size=65),
            ],
            col_labels=[
                MathTex(r"\gamma - \textnormal{Indifferent}", color=text_black, font_size=65),
                MathTex(r"\textnormal{Not} ~ \gamma - \textnormal{Indifferent}", color=text_black, font_size=65),
            ],
            element_to_mobject=lambda m: m,
        )

        table.scale(0.69).center()
        table.get_horizontal_lines().set_color(text_black)
        table.get_vertical_lines().set_color(text_black)


        self.add(table)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())
