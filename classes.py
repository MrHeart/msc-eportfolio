import math
import turtle

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center=None, radius=0):
        if center is None:
            center = Point()
        self.center = center
        self.radius = radius

class Rectangle:
    def __init__(self, bottom_left=None, width=0, height=0):
        if bottom_left is None:
            bottom_left = Point()
        self.bottom_left = bottom_left
        self.width = width
        self.height = height

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
    # Check all four corners of the rectangle
    bottom_left = rect.bottom_left
    bottom_right = Point(bottom_left.x + rect.width, bottom_left.y)
    top_left = Point(bottom_left.x, bottom_left.y + rect.height)
    top_right = Point(bottom_left.x + rect.width, bottom_left.y + rect.height)
    
    return (point_in_circle(circle, bottom_left) and 
            point_in_circle(circle, bottom_right) and 
            point_in_circle(circle, top_left) and 
            point_in_circle(circle, top_right))

def rect_circle_overlap(circle, rect):
    # Check if any of the rectangle's corners fall inside the circle
    bottom_left = rect.bottom_left
    bottom_right = Point(bottom_left.x + rect.width, bottom_left.y)
    top_left = Point(bottom_left.x, bottom_left.y + rect.height)
    top_right = Point(bottom_left.x + rect.width, bottom_left.y + rect.height)
    
    if (point_in_circle(circle, bottom_left) or 
        point_in_circle(circle, bottom_right) or 
        point_in_circle(circle, top_left) or 
        point_in_circle(circle, top_right)):
        return True
    
    # Check if any part of the rectangle overlaps with the circle
    # Check the edges of the rectangle for overlap with the circle
    for x in range(int(bottom_left.x), int(bottom_left.x + rect.width) + 1):
        if point_in_circle(circle, Point(x, bottom_left.y)) or point_in_circle(circle, Point(x, bottom_left.y + rect.height)):
            return True
    for y in range(int(bottom_left.y), int(bottom_left.y + rect.height) + 1):
        if point_in_circle(circle, Point(bottom_left.x, y)) or point_in_circle(circle, Point(bottom_left.x + rect.width, y)):
            return True
    
    return False

def draw_rect(t, rect):
    """Draw a rectangle using the turtle t"""
    t.penup()
    t.goto(rect.bottom_left.x, rect.bottom_left.y)
    t.pendown()

    for _ in range(2):
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)

def draw_circle(t, circle):
    """Draw a circle using the turtle t"""
    t.penup()
    t.goto(circle.center.x, circle.center.y - circle.radius)
    t.pendown()
    t.circle(circle.radius)

def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.bottom_left = Point()
    box.bottom_left.x = 50.0
    box.bottom_left.y = 50.0

    circle = Circle()
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

     # Drawing the rectangle and circle using turtle
    screen = turtle.Screen()
    t = turtle.Turtle()

    
    draw_rect(t, box)
    draw_circle(t, circle)

    print(point_in_circle(circle, box.bottom_left))
    print(rect_in_circle(circle, box))
    print(rect_circle_overlap(circle, box))

if __name__ == '__main__':
    main()
