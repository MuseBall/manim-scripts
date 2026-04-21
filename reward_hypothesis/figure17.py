"""
TIME : 12:30 - 13:20

Guille - Reward Hypothesis - Dovetail Project

Images for Section in Mixture space - Expected utility - Indepen-
dence and Continuity - vNM theorem
Figure 17: Continuity

Generate image by simple running script:
python ./figure17.py
"""

from manim import *
import numpy as np
from nodes_and_arrows import make_arrow
from plttriangle import function1D_heatmap, function2D_graph, function2D_heatmap
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

    # Top left graph
        function1D_heatmap_1 = function1D_heatmap(
            lambda x: 2 if x < 1.5 else (0 if x < 2.5 else 2) #x / 3 + 0
        )
        line2 = function1D_heatmap_1.graph.set_opacity(0)

        function1D_heatmap_1.center().shift(LEFT * 2.5 + UP + 0.01).scale(0.8)


        graph, surface_graph, point1, point_bottom1, point_bottom_left1, triangle1_p1, triangle1_p2, triangle1_p3 = function2D_graph2(lambda x, y: x / 2 + 2.8)

        graph2, surface_graph2, point2, point_bottom2, point_bottom_left2,  triangle2_p1, triangle2_p2, triangle2_p3 = function2D_graph2(
            lambda x, y: y / 8 + 2.5, 
            p1 = np.array([2, -1]),
            p2 = np.array([0, -1]), # shared bottom
            p3 = np.array([0, 2]) )

        surface_graph2.rotate(0.1, axis=[0, 0, 1], about_point=point2)

        #line_between_points = Line(point_bottom1, point_bottom2, stroke_width = 10, stroke_color = text_black)

        dot_point_bottom1 = Dot(point=point_bottom1, color=RED).set_opacity(0)
        dot_point_bottom2 = Dot(point=point_bottom_left1, color=BLUE).rotate(0.1, axis=[0, 0, 1], about_point=point2).set_opacity(0)

        triangle_outline = Polygon(triangle1_p1, triangle1_p3, triangle2_p1).set_stroke(text_black, 1.5)

        triangle_outline1 = Polygon(
            point2, 
            point_bottom1 - [0, -0.1, 0], 
            dot_point_bottom2.get_center() - [0.1, 0.7, 0]
            ).set_fill("#436f6d", 1).set_stroke("#436f6d", 1)

        graph_top_right = Group(graph, graph2, triangle_outline, triangle_outline1).shift(RIGHT * 2.5 + UP * 0.5).scale(0.7)


    # Botoom left graph
        function1D_heatmap_2 = function1D_heatmap(
            lambda x: x / 3 + 0,
        )

        function1D_heatmap_2.shift(DOWN * 3 + LEFT * 3.3).scale(0.8)

        # Bottom right graph
        function2D_graph_2 = function2D_graph(lambda x, y: x / 2 + 2.5, points=False)

        function2D_graph_2.shift(DOWN * 4.7 + RIGHT * 2).scale(0.5)

        label_head = (
            Tex("Not Continous", font_size=75)
            .scale(0.6)
            .set_color(text_black)
            .move_to([0, 3, 0])
        )
        label_head1 = (
            Tex("Continous", font_size=75)
            .scale(0.6)
            .set_color(text_black)
            .move_to([0, -0.5, 0])
        )


        all_2D = Group(
            function1D_heatmap_1,
            function1D_heatmap_2,
            label_head,
            label_head1

        )

        """
        all_3D = Group(
            function2D_graph_1,
            graph
        )
        """
        # graph2.rotate(0.1, [0,0,1], about_point=surface_graph2.get_top())

        all_3D = Group(
            graph,
            graph2,
            triangle_outline1,
            triangle_outline,
            dot_point_bottom1,
            dot_point_bottom2,
            function2D_graph_2
        )

        self.add(all_3D)
        self.add_fixed_in_frame_mobjects(all_2D)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-90 * DEGREES)
        # debug distance of objects with a grid
        # self.add(NumberPlane())



