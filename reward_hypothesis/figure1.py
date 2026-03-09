"""
TIME : 22:00 - 00:00

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Introduction
Figure 1: Outer vs Inner alignment.

Generate image by simple running script:
python ./figure2_3.py
"""

import numpy as np
from manim import *
from nodes_and_arrows import (
    make_arrow,
    make_curved_arrow_bot,
    make_curved_arrow_left_to_right,
    make_curved_arrow_right,
    make_curved_arrow_right_to_left,
    make_curved_arrow_top,
    make_node,
)

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
        node_pink = "#c78d9c"
        node_purple = "#b6b3c4"

        # background rectangle with rounded corners
        background_rectangle = RoundedRectangle(
            color="#d6e2e2", fill_opacity=1, corner_radius=0.7, height=8, width=8
        )

        #face1 = Circle(radius = 0.5, color = "#ecbc9c", fill_opacity = 1, stroke_color = text_black, stroke_width = 5)

    # Human

        face1 = Circle(radius = 0.5, color = "#d6af82", fill_opacity = 1, stroke_color = text_black, stroke_width = 5) 

        text = MathTex(r"\succsim", color = text_black, stroke_width = 4).move_to([face1.get_center()])

        body = Line([face1.get_bottom()], [face1.get_bottom() + DOWN * 0.8], color = text_black, stroke_width = 6)

        leg1 = Line([body.get_bottom()], [body.get_bottom() + DOWN * 1 + RIGHT * 0.5], color = text_black, stroke_width = 6)

        leg2 = Line([body.get_bottom()], [body.get_bottom() + DOWN * 1 + LEFT * 0.5], color = text_black, stroke_width = 6)

        hand1 = Line([body.get_center()], [body.get_center() + UP * 0.4 + RIGHT * 0.9], color = text_black, stroke_width = 6)

        hand2 = Line([body.get_center()], [body.get_center() + UP * 0.4 + LEFT * 0.9], color = text_black, stroke_width = 6)

        human = VGroup(face1, body, leg1, leg2, hand1, hand2, text)

    # Alien

        face2 = Circle(radius = 0.5, color = node_green, fill_opacity = 1, stroke_color = text_black, stroke_width = 5) 

        text2 = MathTex(r"\succsim", color = text_black, stroke_width = 4).move_to([face2.get_center()])

        body2 = Line([face1.get_bottom()], [face2.get_bottom() + DOWN * 0.8], color = text_black, stroke_width = 6)

        leg12 = Line([body2.get_bottom()], [body2.get_bottom() + DOWN * 1 + RIGHT * 0.5], color = text_black, stroke_width = 6)

        leg22 = Line([body2.get_bottom()], [body2.get_bottom() + DOWN * 1 + LEFT * 0.5], color = text_black, stroke_width = 6)

        hand12 = Line([body2.get_center()], [body2.get_center() + UP * 0.4 + RIGHT * 0.9], color = text_black, stroke_width = 6)

        hand22 = Line([body2.get_center()], [body2.get_center() + UP * 0.4 + LEFT * 0.9], color = text_black, stroke_width = 6)

        antenna1 = Line([face2.get_top() + RIGHT * 0.2 + DOWN * 0.05], [face2.get_top() + RIGHT * 0.4 + UP * 0.3], color = text_black, stroke_width = 6)

        antenna1_dot = Dot([antenna1.get_top() + RIGHT * 0.1], color = node_green, stroke_color = text_black, stroke_width = 6)

        antenna2 = Line([face2.get_top() + LEFT * 0.2]+ DOWN * 0.05, [face2.get_top() + LEFT * 0.4 + UP * 0.3], color = text_black, stroke_width = 6)

        antenna2_dot = Dot([antenna2.get_top() + LEFT * 0.1], color = node_green, stroke_color = text_black, stroke_width = 6)

        alien = VGroup(face2, body2, leg12, leg22, hand12, hand22, antenna1, antenna2, antenna1_dot, antenna2_dot, text2)

    # Rectangle

        rectangle = Polygon(
            [1,1,0],
            [-1,1,0],
            [-1,-1.5,0],
            [1,-1.5,0], 
            color = text_black, 
            stroke_width = 3
            )

    # Dashed Rectangle

        rectangle1 = Polygon(
            [4,2.5,0],
            [-4,2.5,0],
            [-4,-2.5,0],
            [4,-2.5,0], 
            color = text_black, 
            stroke_width = 3
            )

        dashed_rect = DashedVMobject(rectangle1, num_dashes = 45)

    # Labels

        human_text = Tex("Preferences", color = text_black, stroke_width = 2)

        alien_text = Tex("Learned \\\\ Preferences", color = text_black, stroke_width = 2)

        obj = Tex("Objective \\\\ Function", color = text_black, stroke_width = 2)

        out_align = Tex("Outer \\\\ Alignment", color = text_black, stroke_width = 2)

        in_align = Tex("Inner \\\\ Alignment", color = text_black, stroke_width = 2)

        f = MathTex("f", color = text_black, stroke_width = 2, font_size =70)

    # Arrows

        arrow_in = MathTex(r"\Longrightarrow", color = text_black, stroke_width = 3)

        arrow_out = MathTex(r"\Longrightarrow", color = text_black, stroke_width = 3)

        
    # Adjusting position of each element

        human.shift(LEFT * 4.5 + UP * 1.5)
        human_text.shift(LEFT * 4.5 + DOWN * 1.5)

        alien.shift(RIGHT * 5.5 + UP * 1.5)
        alien_text.shift(RIGHT * 5.5 + DOWN * 1.7)

        rectangle.shift(UP * 1 + RIGHT * 0.5)
        dashed_rect.shift(LEFT * 2)

        obj.shift(DOWN * 1.5 + RIGHT * 0.5)
        out_align.shift(LEFT * 2.1 + UP * 1)
        in_align.shift(RIGHT * 3.3 + UP * 1)
        f.shift(UP * 0.7 + RIGHT * 0.5)

        arrow_in.shift(RIGHT * 3.3 )
        arrow_out.shift(LEFT * 2.1 )

        all_ = VGroup(rectangle, human, alien, dashed_rect, human_text, alien_text, obj, out_align, in_align, arrow_in, arrow_out,f).center()
       
        self.add(all_)

        #self.add(rectangle, human, alien, dashed_rect, human_text, alien_text)

        # debug distance of objects with a grid
        #self.add(NumberPlane())
