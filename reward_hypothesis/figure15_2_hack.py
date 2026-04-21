"""
TIME : 23:50 - 00:10


Guille - Reward Hypothesis - Dovetail Project

Images for Section in Mixture space - Expected utility - Indepen-
dence and Continuity - vNM theorem
Figure 15: Independence

Generate image by simple running script:
python ./figure15_2.py
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

        axes = Axes(x_range =[-1,1], x_length= 4, tips = False, x_axis_config={"include_numbers": False, "include_ticks": True}, axis_config = {"tip_shape": None, "color": text_black})

        axes.y_axis.set_opacity(0)

        labels_axes = axes.get_axis_labels(MathTex("", color = text_black, stroke_width = 1.5).scale(0.8))

        labels_axes[0].set_opacity(0)
        labels_axes[1].set_opacity(0)

    # Triangle left

        triangle_5 = Polygon(
            [-1.8, 0.1, 0],
            [1.8, 0.7, 0],
            [1.8, 0.1, 0],
            color = node_blue,
            fill_opacity =1
            ).set_stroke(text_black, 2).set_sheen(0.5, LEFT)

        line = Line([-1.8, 0.3,0], [0.6, 1, 0], stroke_color = text_black, stroke_width = 2)

    # Triangle right
        
        triangle_1 = Polygon(
            [-1.8, 0.1, 0],
            [-0.3, 1, 0],
            [1.8, 0.1, 0],
            color = node_blue, 
            fill_opacity = 1).set_sheen(0.5, LEFT).set_stroke(text_black, 2)

        triangle_2 = Polygon(
            [-1.8, 0.5, 0],
            [-0.1, 0.7, 0],
            [-0.1, 1.3, 0]
            ).set_stroke(text_black, 2)

        triangle_3 = Polygon(
            [0.1, 1, 0],
            [-0.1, 0.7, 0],
            [-0.1, 1.3, 0],
            color = "#739b99",
            fill_opacity = 1
            ).set_stroke(text_black, 2)
        
        triangle_4 = Polygon(
            [0.1, 1, 0],
            [2.2, 1.4, 0],
            [-0.1, 1.3, 0] 
            ).set_stroke(text_black, 2)
        

        label_top = Tex("Independent", font_size = 75).scale(0.6).set_color(text_black).move_to([0,3,0])


        triangle_right = VGroup(triangle_1, triangle_2, triangle_3 ,triangle_4).shift(RIGHT * 3)

        triangle_left = VGroup(triangle_5, axes).shift(LEFT * 3)
    
        all_ = VGroup(triangle_right, triangle_left, label_top)

        self.add(all_)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())


