"""
TIME : 18:00 - 18:20

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Concatenable mixture space - Reward function - γ-indifference - Markov Reward theorem
Figure 20: Reward fuction

Generate image by simple running script:
python ./figure20_3.py
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



        x1 = MathTex(
            r"x \succeq y", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 75
            ).scale(0.6).shift(LEFT * 4)

        arrow = MathTex(
            r"\Longleftrightarrow", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 100
            ).scale(0.8)

        f1 = MathTex(
            r"f(x) \geq f(y)", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 75
            ).scale(0.6).shift(RIGHT * 4)

        f2 = MathTex(
            r"f(\sum_i p_i x_i) = \sum_i p_i f(x_i)", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 75
            ).scale(0.6).shift(RIGHT * 4 + DOWN * 1)

        f3 = MathTex(
            r"f(t \cdot_T x) = f(t)+ \gamma(t)f(x)", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 75
            ).scale(0.6).shift(RIGHT * 4 + DOWN * 2)

        f4 = MathTex(
            r"\gamma : T \rightarrow [0,1]", 
            color = text_black, 
            stroke_width = 1.5, 
            font_size = 75
            ).scale(0.6).shift(RIGHT * 4 + DOWN * 3)

        
        all_ = VGroup(x1, f1, f2, f3, f4, arrow).center() 
        self.add(x1, f1, f2, f3, f4, arrow)


        #debug distance of objects with a grid
        #self.add(NumberPlane())


