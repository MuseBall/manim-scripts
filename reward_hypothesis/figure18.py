"""
TIME : 13:50 : 15:10

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Mixture space - Expected utility - Indepen-
dence and Continuity - vNM theorem
Figure 18: Independence vs Continuity

Generate image by simple running script:
python ./figure18.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_arrow
from plttriangle import (
    function1D_graph,
    function1D_heatmap,
    function2D_graph,
    function2D_heatmap,
)
from twosurfaces import function2D_graph2


config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = config.pixel_height / config.pixel_width * config.frame_width


class Graph(ThreeDScene):
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

        ##### TOP LEFT GRAPH 17R

        # Top left graph 1

        function1D_heatmap_1 = function1D_heatmap(
            lambda x: x / 3 + 0,
        )

        function1D_heatmap_1.shift(LEFT * 3.8 + DOWN * 0.7).scale(0.8)

        # Top left graph 2
        function2D_graph_1 = function2D_graph(lambda x, y: x / 2 + 2.5, points=False)

        function2D_graph_1.shift(LEFT * 0.1).scale(0.65)

        left_top = Group(
            function1D_heatmap_1,
            function2D_graph_1,
            ).shift(UP * 0.5)

        ##### TOP RIGHT GRAPH 15TL

        # Top right graph 1
        function1D_heatmap_2 = function1D_heatmap(
            lambda x: x / 2 if x < 2.5 else -x / 2 + 2.5
        )

        function1D_heatmap_2.shift(RIGHT * 1.8 + DOWN * 0.8).scale(0.8)

        # Top right graph 2
        function2D_graph_2 = function2D_graph(
            lambda x, y: x / 2 + 2 if x < 1 / 2 else -x / 2 + 2.5, line=True
        )

        function2D_graph_2.shift(RIGHT * 5.6).scale(0.7)

        right_top = Group(
            function1D_heatmap_2,
            function2D_graph_2,
            ).shift(UP * 0.5)

        ##### BOTTOM RIGHT GRAPH (Similar to 17L)

        # Bottom right graph
        function1D_heatmap_3 = function1D_heatmap(
            lambda x: 2 if x < 1.5 else (0 if x < 2.5 else 2) #x / 3 + 0
        )
        line2 = function1D_heatmap_3.graph.set_opacity(0)

        function1D_heatmap_3.center().shift(RIGHT * 2.5 + DOWN * 2).scale(0.8)


        graph, surface_graph, point1, point_bottom1, point_bottom_left1, triangle1_p1, triangle1_p2, triangle1_p3 = function2D_graph2(lambda x, y: x / 2 + 2.8)

        graph2, surface_graph2, point2, point_bottom2, point_bottom_left2,  triangle2_p1, triangle2_p2, triangle2_p3 = function2D_graph2(
            lambda x, y: y / 8 + 2.5, 
            p1 = np.array([2, -1]),
            p2 = np.array([0, -1]), # shared bottom
            p3 = np.array([0, 2]) )

        surface_graph2.rotate(0.5, axis=[0, 0, 1], about_point=point2)
        surface_graph.rotate(-0.5, axis=[0, 0, 1], about_point=point2)

        #line_between_points = Line(point_bottom1, point_bottom2, stroke_width = 10, stroke_color = text_black)

        dot_point_bottom1 = Dot(point=point_bottom1, color=RED).set_opacity(0).rotate(-0.5, axis=[0, 0, 1], about_point=point2)
        dot_point_bottom2 = Dot(point=point_bottom_left1, color=BLUE).rotate(0.1, axis=[0, 0, 1], about_point=point2).set_opacity(0)

        triangle_outline = Polygon(triangle1_p1, triangle1_p3, triangle2_p1).set_stroke(text_black, 1.5)

        triangle_outline1 = Polygon(
            point2, 
            point_bottom1 - [1.6, -0.4, 0], 
            dot_point_bottom2.get_center() - [-0.9, 0.15, 0]
            ).set_fill("#436f6d", 1).set_stroke("#436f6d", 1)

        graph_bottom_right = Group(graph, graph2, triangle_outline, triangle_outline1).shift(RIGHT * 4.5 + DOWN * 5.2).scale(0.7)

        bottom_right = Group(
            function1D_heatmap_3,
            graph_bottom_right,
            ).shift(DOWN * -0.5 + LEFT * 0.5)


        ##### BOTTOM LEFT 17L

        # Bottom left graph
        function1D_heatmap_4 = function1D_heatmap(
            lambda x: 2 if x < 1.5 else (0 if x < 2.5 else 2) #x / 3 + 0
        )
        line2 = function1D_heatmap_4.graph.set_opacity(0)

        function1D_heatmap_4.shift(LEFT * 4.3 + DOWN * 0.1).scale(0.8)


        graph3, surface_graph3, point3, point_bottom3, point_bottom_left3, triangle3_p3, triangle3_p2, triangle3_p1 = function2D_graph2(lambda x, y: x / 2 + 2.8)

        graph4, surface_graph4, point4, point_bottom4, point_bottom_left4,  triangle4_p1, triangle4_p2, triangle4_p3 = function2D_graph2(
            lambda x, y: y / 8 + 2.5, 
            p1 = np.array([2, -1]),
            p2 = np.array([0, -1]), # shared bottom
            p3 = np.array([0, 2]) )

        surface_graph4.rotate(0.1, axis=[0, 0, 1], about_point=point4)

        #line_between_points = Line(point_bottom1, point_bottom2, stroke_width = 10, stroke_color = text_black)

        dot_point_bottom3 = Dot(point=point_bottom3, color=RED).set_opacity(0)
        dot_point_bottom4 = Dot(point=point_bottom_left4, color=BLUE).rotate(0.1, axis=[0, 0, 1], about_point=point4).set_opacity(0)

        triangle_outline34 = Polygon(triangle3_p1, triangle3_p3, triangle4_p1).set_stroke(text_black, 1.5)

        triangle_outline341 = Polygon(
            point4, 
            point_bottom3 - [0, -0.1, 0], 
            dot_point_bottom4.get_center() - [0.01, 0, 0]
            ).set_fill("#436f6d", 1).set_stroke("#436f6d", 1)

        graph_bottom_left = Group(graph3, graph4, triangle_outline34, triangle_outline341).shift(LEFT * -0.1 + DOWN * 2).scale(0.7)

        bottom_left = Group(
            function1D_heatmap_4,
            graph_bottom_left,
            ).shift(DOWN * 2.5)


        # Table
        
        row1 = Tex(
            "Continuous", 
            color=text_black, 
            font_size=65
            ).scale(0.7).move_to([-5.6,1,0])

        row2 = Tex(
            "Not \\\\ Continuous", 
            color=text_black, 
            font_size=65
            ).scale(0.7).move_to([-5.6,-2,0])

        col1 = Tex(
            "Independent", 
            color=text_black, 
            font_size=65
            ).scale(0.7).move_to([-1.3,3,0])

        col2 = Tex(
            "Not Independent",
            color=text_black, 
            font_size=65
            ).scale(0.7).move_to([4.3,3,0])

        #left_top.move_to([-1.3,1,0]).scale(0.85)
        #right_top.move_to([4.3,1,0]).scale(0.85)
        #bottom_left.move_to([-1.3,-2,0]).scale(0.7)
        #bottom_right.move_to([3.4,-4,0]).scale(0.65)

        left_top.scale(0.85)
        right_top.scale(0.85)
        bottom_left.scale(0.65)
        bottom_right.scale(0.65)

        line_row1 = Line([-4, 3.5, 0], [-4, -3.5,0], stroke_width = 3, stroke_color = text_black)
        line_row1.set_cap_style(CapStyleType.ROUND)

        line_row2 = Line([1.5, 3.5, 0], [1.5, -3.5,0], stroke_width = 3, stroke_color = text_black)
        line_row2.set_cap_style(CapStyleType.ROUND)

        line_col1 = Line([-7, 2.5, 0], [7, 2.5,0], stroke_width = 3, stroke_color = text_black)
        line_col1.set_cap_style(CapStyleType.ROUND)

        line_col2 = Line([-7, -0.5, 0], [7, -0.5,0], stroke_width = 3, stroke_color = text_black)
        line_col2.set_cap_style(CapStyleType.ROUND)
    
        all_3D = Group(
            function2D_graph_1,
            function2D_graph_2,
            graph_bottom_left,
            graph_bottom_right
        )

        all_2D = Group(row1, row2, col1, col2, line_row1, line_row2, line_col1, line_col2, function1D_heatmap_1, function1D_heatmap_2, function1D_heatmap_3, function1D_heatmap_4)

        self.add(all_3D)
        #self.add_fixed_in_frame_mobjects(table)
        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
    


