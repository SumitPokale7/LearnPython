# import colorgram
import turtle, random

t = turtle.Turtle()
s = turtle.Screen()


# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpeg', 6)
# def get_rgb(colors):
#     rgb = []
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         rgb.append(new_color)     
#     return rgb


colors = [
    (234, 232, 227), (230, 233, 239), (239, 231, 235), 
    (228, 235, 231), (199, 162, 100), (62, 91, 128)
]

# Set up turtle
turtle.colormode(255)
t.hideturtle()
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
t.speed(0)


# def draw_dots():
#     """Draw a row of 10 dots with random colors."""
#     for _ in range(10):
#         t.forward(20)
#         t.dot(20, random.choice(colors))
#         t.forward(20)


# def reset_position():
#     """Move turtle up to start a new row."""
#     t.penup()
#     t.forward(10)
#     t.setheading(90)
#     t.forward(30)
#     t.setheading(180)

#     for _ in range(10):
#         t.forward(41)

#     t.setheading(0)

# # Draw multiple rows
# for _ in range(5):
#     draw_dots()
#     reset_position()
#     draw_dots()
#     reset_position()


# Simple Version
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(colors))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


s.exitonclick()