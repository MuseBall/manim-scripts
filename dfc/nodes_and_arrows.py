from manim import *
import numpy as np

def make_node(position, label="x", radius=0.5, node_color="#e1c180", text_color="#22323b"):
    circle = Circle(radius = radius, color = node_color, fill_opacity = 1, stroke_color = text_color, stroke_width = 1.8).move_to(position)

    shadow = Circle(radius = radius-0.01, color = text_color, fill_opacity = 1).move_to(position + DOWN * 0.015 + RIGHT * 0.015)
    
    border = Circle(radius = radius+0.02, color = "#dce2e1", fill_opacity = 0).move_to(position)
    label = MathTex(label, color = text_color, stroke_color = text_color, stroke_width = 1.3, font_size = 100).move_to(position)

    label.scale(radius)

    node = VGroup(shadow, circle, label)

    return node

#def make_arrow(self, start, end, label = "x", buff=0.5, color = "#22323b", tip_shape = StealthTip, stroke_width = 7, tip_length = 0.25):

def make_arrow(start, end, label="x", label_shift=0.2, color="#22323b", tip_shape = StealthTip,  scale_label = 0.3, tip_length = 0.07):
    """
    start, end can be numpy arrays showing [x,y,z] or any mobject whose position will be taken by Arrow().
    In this case, it can be node objects from make_node()
    """
    
    arrow = Arrow(start = start, end = end, color = color, tip_shape = tip_shape, stroke_width = 2.5, buff = 0, tip_length = tip_length).shift(LEFT * 0.04)

    angle = arrow.get_angle()

    #label_arrow = Text(label, weight = BOLD, color = color).next_to(arrow.get_center())
    label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(arrow.point_from_proportion(0.5)).rotate(angle).shift(UP * label_shift)

    label_arrow.scale(scale_label)

    arrow_with_label = VGroup(arrow, label_arrow)

    return arrow_with_label

def make_curved_arrow_top(start_node, end_node, color, label, radius, label_scale = 0.3):
    """
    node is a vgroup object returned by make_node()
    """
    start = start_node.get_top() + RIGHT * 0.27 + DOWN * 0.02
    end = end_node.get_top() + LEFT * 0.27 + DOWN * 0.02
    carrow = CurvedArrow(start_point = start , end_point = end, radius=radius, color = color, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)
    label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(carrow.point_from_proportion(0.5)).shift(UP * 0.2)

    label_arrow.scale(label_scale)

    carrow_with_label = VGroup(carrow, label_arrow)

    return carrow_with_label

def make_curved_arrow_right(start_node, end_node, color, label, radius, label_scale = 0.3):
        """
        node is a vgroup object returned by make_node()
        """
        start = start_node.get_right() + DOWN * 0.25
        end = end_node.get_right() + UP * 0.25
        carrow = CurvedArrow(start_point = start , end_point = end, radius=radius, color = color, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)
        label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(carrow.point_from_proportion(0.5)).shift( RIGHT * 0.3)

        label_arrow.scale(label_scale)

        carrow_with_label = VGroup(carrow, label_arrow)

        return carrow_with_label

def make_curved_arrow_right_to_left(start_node, end_node, color, label, radius, label_scale = 0.3):
    """
    node is a vgroup object returned by make_node()
    """
    start = start_node.get_left() 
    end = end_node.get_right() 
    carrow = CurvedArrow(start_point = start , end_point = end, radius=radius, color = color, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)
    label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(carrow.point_from_proportion(0.5)).shift(UP * 0.2 + LEFT * 0.06)

    label_arrow.scale(label_scale)

    carrow_with_label = VGroup(carrow, label_arrow)

    return carrow_with_label

def make_curved_arrow_left_to_right(start_node, end_node, color, label, radius, label_scale = 0.3):
    """
    node is a vgroup object returned by make_node()
    """
    start = start_node.get_right() 
    end = end_node.get_left() 
    carrow = CurvedArrow(start_point = start , end_point = end, radius=radius, color = color, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)
    label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(carrow.point_from_proportion(0.5)).shift(DOWN * 0.2 + RIGHT * 0.06)

    label_arrow.scale(label_scale)

    carrow_with_label = VGroup(carrow, label_arrow)

    return carrow_with_label

def make_curved_arrow_bot(start_node, end_node, color, label, radius, label_scale = 0.3):
    """
    node is a vgroup object returned by make_node()
    """
    start = start_node.get_bottom() + DOWN * 0.04
    end = end_node.get_bottom() + DOWN * 0.02
    carrow = CurvedArrow(start_point = start , end_point = end, radius=radius, color = color, tip_shape = StealthTip, stroke_width = 3, tip_length = 0.07)
    label_arrow = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(carrow.point_from_proportion(0.5)).shift(UP * 0.2)

    label_arrow.scale(label_scale)

    carrow_with_label = VGroup(carrow, label_arrow)

    return carrow_with_label
    
def make_self_loop_top(start_node, label, color, label_shift = UP * 0, radius = 1.4, start_angle = PI/6, angle = 3*PI/2, stroke_width = 3, label_scale = 0.3):


    start = start_node.get_top()
    loop = Arc(
            radius=radius,
            start_angle= start_angle,   # controls where it begins
            angle= angle,       # 270 degrees
            stroke_width= stroke_width,
            color = color
        )

    # Move loop above the node
    loop.move_to(start)

    # Add arrow tip (optional)
    loop.add_tip(tip_shape = StealthTip, tip_length = 0.07)

    label_loop = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(loop.point_from_proportion(0.5)).shift(UP * 0.17 + LEFT * 0.05)

    label_loop.scale(label_scale)

    label_loop.shift(label_shift)

    loop_with_label = VGroup(loop, label_loop)

    return loop_with_label

def make_self_loop_right(start_node, label, color, label_shift = RIGHT * 0.03, radius = 1.4, start_angle = PI/6, angle = 3*PI/2, stroke_width = 3, label_scale = 0.3):


    start = start_node.get_right()
    loop = Arc(
            radius=radius,
            start_angle= start_angle,   # controls where it begins
            angle= angle,       # 270 degrees
            stroke_width= stroke_width,
            color = color
        )

    # Move loop above the node
    loop.move_to(start)

    # Add arrow tip (optional)
    loop.add_tip(tip_shape = StealthTip, tip_length = 0.07)

    label_loop = MathTex(label, color = color, stroke_color = color, stroke_width = 1.3, font_size = 80).move_to(loop.point_from_proportion(0.5)).shift(UP * 0.17 + LEFT * 0.05)

    label_loop.scale(label_scale)
    label_loop.rotate(PI/2)

    label_loop.shift(label_shift)
    

    loop_with_label = VGroup(loop, label_loop)

    return loop_with_label
