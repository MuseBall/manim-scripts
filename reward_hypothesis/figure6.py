"""
TIME : 14:20 - 14:45
       8:45 - 10:50

Guille - Reward Hypothesis - Dovetail Project

Images for Section in 3 Set - Order representation - Preorder and De-
breu separable - Debreu-Fishburns theorem
Figure 6: Completeness and Transitivity.  

Generate image by simple running script:
python ./figure4.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_node, make_arrow, make_self_loop_top, make_self_loop_bot


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
        background_rectangle = RoundedRectangle(color = "#d6e2e2", fill_opacity = 1, corner_radius = 0.7, 
                                                height = 8, width = 8)

    # Right Nodes 
        node_1_bl = make_node(position=[-4, 2, 0], label="", node_color = node_blue)

        node_2_bl = make_node(position=[-3,0,0], label="", node_color = node_blue) 

        node_3_bl = make_node(position=[-5,0,0], label="", node_color = node_blue)


    # Arrows

        arrow_1_bl = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1_bl, color = text_black, label = "").shift(UP * 0.11)

        arrow_2_bl = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = node_2_bl, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3_bl = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3_bl, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4_bl = make_arrow(start = node_3_bl, end = node_2_bl, label = "").shift(DOWN * 0.2 + RIGHT * 0.03)

        arrow_5_bl = make_arrow(start = node_2_bl, end = node_3_bl, label = "", color = "#a960a0").shift(UP * 0.17 + RIGHT * 0.07)

        arrow_6_bl = make_arrow(start = node_1_bl, end = node_2_bl.get_top(), label = "", color = "#a960a0").shift(UP * 0.0)

        arrow_7_bl = make_arrow(start = node_3_bl.get_top(), end = node_1_bl, label = "", color = "#a960a0").shift(UP * 0.03)


    # Right Nodes

        node_1_tl = node_1_bl.copy().move_to([4, 2, 0])
        node_2_tl = node_2_bl.copy().move_to([3, 0, 0])
        node_3_tl = node_3_bl.copy().move_to([5, 0, 0])

    # Right Arrows

        arrow_1_tl = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1_tl, color = text_black, label = "").shift(UP * 0.11)

        arrow_2_tl = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = node_2_tl, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3_tl = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3_tl, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4_tl = make_arrow(start = node_3_tl, end = node_2_tl, label = "").shift(UP * 0.15 + RIGHT * 0.06)

        arrow_5_tl = make_arrow(start = node_2_tl, end = node_3_tl, label = "").shift(DOWN * 0.15 + RIGHT * 0.01)

        arrow_6_tl = make_arrow(start = node_1_tl, end = node_2_tl.get_top(), label = "").shift(UP * 0.03)

        arrow_7_tl = make_arrow(start = node_1_tl, end = node_3_tl.get_top(), label = "").shift(UP * 0.03)

    #Top Left Label

        equiv = MathTex("\equiv", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([1.9,1,0])


    # Rotated right graph nodes

        node_1_rotated_tl = node_1_bl.copy().move_to([3, 1, 0])
        node_2_rotated_tl = node_2_bl.copy().move_to([6, 2, 0])
        node_3_rotated_tl = node_3_bl.copy().move_to([6, 0, 0])


    # Rotated right graph arrows

        arrow_1_rotated_tl = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1_rotated_tl, color = text_black, label = "").shift(UP * 0.11)

        arrow_2_rotated_tl = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4 , stroke_width = 3, start_node = node_2_rotated_tl, color = text_black, label = "").shift(UP * 0.11)

        arrow_3_rotated_tl = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3_rotated_tl, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4_rotated_tl = make_arrow(start = node_3_rotated_tl, end = node_2_rotated_tl, label = "").shift(RIGHT * 0.1 + DOWN * 0.05)

        arrow_5_rotated_tl = make_arrow(start = node_2_rotated_tl, end = node_3_rotated_tl, label = "").shift(LEFT * 0.1 + UP * 0.03)

    # Split Y arrow

        stem_tl = Line(node_1_rotated_tl.get_right(), [4.5,1,0], color = text_black, stroke_width =2.5)
        
        arrow_6_rotated_tl = make_arrow(start = stem_tl, end = node_2_rotated_tl, label = "")

        arrow_7_rotated_tl = make_arrow(start = stem_tl, end = node_3_rotated_tl, label = "")

    
    # Top Right Nodes 

        node_1_tr = make_node(position=[-4, 2, 0], label="", node_color = node_blue)

        node_2_tr = make_node(position=[-3,0,0], label="", node_color = node_blue) 

        node_3_tr = make_node(position=[-5,0,0], label="", node_color = node_blue)


    # Arrows

        arrow_1_tr = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1_tr, color = text_black, label = "").shift(UP * 0.11)

        arrow_2_tr = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = node_2_tr, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3_tr = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3_tr, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4_tr = make_arrow(start = node_3_tr, end = node_2_tr, label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.15 * RIGHT * 0.03)

        arrow_5_tr = make_arrow(start = node_2_tr, end = node_3_tr, label = "", scale_label = 0.4, label_shift = 0.3).shift(DOWN * 0.15 + RIGHT * 0.07)

        arrow_6_tr = make_arrow(start = node_1_tr, end = node_2_tr.get_top(), label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.04)

    # Dotted line and label

        line_13_tr = DashedLine(node_1_tr, node_3_tr.get_top(), dash_length=0.15, color= "#24867e", stroke_width=3).shift(LEFT * 0.15) 

    # Bottom Right Nodes 

        node_1_br = make_node(position=[-4, 2, 0], label="", node_color = node_blue)

        node_2_br = make_node(position=[-3,0,0], label="", node_color = node_blue) 

        node_3_br = make_node(position=[-5,0,0], label="", node_color = node_blue)


    # Arrows

        arrow_1_br = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1_br, color = text_black, label = "").shift(UP * 0.11)

        arrow_2_br = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = node_2_br, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3_br = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3_br, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4_br = make_arrow(start = node_3_br, end = node_2_br, label = "", scale_label = 0.4, label_shift = 0.3).shift(UP * 0.2 + RIGHT * 0.03)

        arrow_5_br = make_arrow(start = node_2_br, end = node_3_br, label = "", scale_label = 0.4, label_shift = 0.3, color = "#a960a0" ).shift(DOWN * 0.17 + RIGHT * 0.07)

        arrow_6_br = make_arrow(start = node_1_br, end = node_2_br.get_top(), label = "", scale_label = 0.4, label_shift = 0.3 , color = "#a960a0").shift(UP * 0.04)

    # Dotted line and label

        line_13_br = DashedLine(node_1_br, node_3_br.get_top(), dash_length=0.15, color= "#24867e", stroke_width=3).shift(LEFT * 0.15)

    # Right Nodes

        node_1_tr = node_1_bl.copy().move_to([4, 2, 0])
        node_2_tr = node_2_bl.copy().move_to([3, 0, 0])
        node_3_tr = node_3_bl.copy().move_to([5, 0, 0])

    # Right Arrows

        arrow_1_tr = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1_tr, color = text_black, label = "").shift(UP * 0.11)

        arrow_2_tr = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4 , stroke_width = 3, start_node = node_2_tr, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_3_tr = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3_tr, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4_tr = make_arrow(start = node_3_tr, end = node_2_tl, label = "").shift(UP * 0.15 + RIGHT * 0.06).set_opacity(0)

        arrow_5_tr = make_arrow(start = node_2_tr, end = node_3_tr, label = "").shift(DOWN * 0.15 + RIGHT * 0.01)

        arrow_6_tr = make_arrow(start = node_1_tr, end = node_3_tr.get_top(), label = "").shift(UP * 0.03)

    # Dotted line and label

        line_13_tr = DashedLine(node_1_tr, node_2_tr.get_top(), dash_length=0.15, color= "#24867e", stroke_width=3).shift(LEFT * 0.15)

    #Top Left Label

        equiv_tr = MathTex("\equiv", color = text_black, stroke_color = text_black, stroke_width = 1.3, font_size = 65).move_to([1.9,1,0])


    # Rotated right graph nodes

        node_1_rotated_tr = node_1_bl.copy().move_to([6, 1, 0])
        node_2_rotated_tr = node_2_bl.copy().move_to([3, 2, 0])
        node_3_rotated_tr = node_3_bl.copy().move_to([3, 0, 0])


    # Rotated right graph arrows

        arrow_1_rotated_tr = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4, stroke_width = 3, start_node = node_1_rotated_tr, color = text_black, label = "").shift(UP * 0.11)

        arrow_2_rotated_tr = make_self_loop_top(radius = 0.3, start_angle = 11*PI/6, angle = 5*PI/4 , stroke_width = 3, start_node = node_2_rotated_tr, color = text_black, label = "").shift(UP * 0.11)

        arrow_3_rotated_tr = make_self_loop_bot(radius = 0.3, start_angle = -11*PI/6, angle = -5*PI/4, stroke_width = 3, start_node = node_3_rotated_tr, color = text_black, label = "").shift(DOWN * 0.11)

        arrow_4_rotated_tr = make_arrow(start = node_3_rotated_tr, end = node_2_rotated_tr, label = "").shift(RIGHT * 0.1 + DOWN * 0.05).set_opacity(0)

        arrow_5_rotated_tr = make_arrow(start = node_2_rotated_tr, end = node_3_rotated_tr, label = "").shift(LEFT * 0.1 + UP * 0.03).set_opacity(0)

    # Dotted line

        line_13_tr = DashedLine(node_1_tr, node_2_tr.get_top(), dash_length=0.15, color= "#24867e", stroke_width=3).shift(LEFT * 0.15)

    # Split Y arrow

        stem_tr_1 = Line([4.5,1,0],node_3_rotated_tr, color = text_black, stroke_width =2.5)
        stem_tr_2 = Line([4.5,1,0],node_2_rotated_tr, color = text_black, stroke_width =2.5)
        
        arrow_6_rotated_tr = make_arrow(start = [4.5,1,0], end = [5.5,1,0], label = "")

    # Dotted line rotated

        line_13_rotated_tr = DashedLine(node_2_rotated_tr.get_bottom(), node_3_rotated_tr.get_top(), dash_length=0.15, color= "#24867e", stroke_width=3)

    # Adjusting the three graphs to be closer

        graph_tl = VGroup(arrow_1_tl, arrow_2_tl, arrow_3_tl, arrow_4_tl, arrow_5_tl, arrow_6_tl, arrow_7_tl, node_1_tl, node_2_tl, node_3_tl).shift(LEFT * 3.7)

        graph_rotated_tl = VGroup(arrow_1_rotated_tl, arrow_2_rotated_tl, arrow_3_rotated_tl, arrow_4_rotated_tl, arrow_5_rotated_tl, arrow_6_rotated_tl, arrow_7_rotated_tl, stem_tl ,node_1_rotated_tl, node_2_rotated_tl, node_3_rotated_tl)

        graph_tr = VGroup(arrow_1_tr, arrow_2_tr, arrow_3_tr, arrow_4_tr, arrow_5_tr, arrow_6_tr, line_13_tr ,node_1_tr, node_2_tr, node_3_tr).shift(LEFT * 3.7)

        graph_rotated_tr = VGroup(arrow_1_rotated_tr, arrow_2_rotated_tr, arrow_3_rotated_tr, arrow_4_rotated_tr, arrow_5_rotated_tr, arrow_6_rotated_tr, stem_tr_1, stem_tr_2, line_13_rotated_tr ,node_1_rotated_tr, node_2_rotated_tr, node_3_rotated_tr)

        graph_bl = VGroup(arrow_1_bl, arrow_2_bl, arrow_3_bl, arrow_4_bl, arrow_5_bl, arrow_6_bl, arrow_7_bl ,node_1_bl, node_2_bl, node_3_bl).shift(LEFT * 0.5)

        graph_br = VGroup(arrow_1_br, arrow_2_br, arrow_3_br, arrow_4_br, arrow_5_br, arrow_6_br ,line_13_br ,node_1_br, node_2_br, node_3_br)

        top_left = VGroup(graph_tl, graph_rotated_tl, equiv)
        top_right = VGroup(graph_tr, graph_rotated_tr, equiv_tr)
        bot_left = VGroup(graph_bl)
        bot_right = VGroup(graph_br)


    # Table 

        table = Table(
            [
                [top_left, top_right],
                [bot_left, bot_right]
            ],
            row_labels=[Tex("Transitive", color = text_black, font_size = 60), Tex("Not \\\\ Transitive", color = text_black, font_size = 60)],
            col_labels=[Tex("Complete", color = text_black, font_size = 60), Tex("Not \\\\ Complete", color = text_black, font_size = 60)],
            element_to_mobject=lambda m: m

        )

        table.scale(0.65).center()
        table.get_horizontal_lines().set_color(text_black)
        table.get_vertical_lines().set_color(text_black)

        self.add(table)
        
        #debug distance of objects with a grid
        #self.add(NumberPlane())

        
