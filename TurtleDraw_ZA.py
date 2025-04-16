# TurtleDraw
# Author: Zain Ahmed
# Credit: Eric Pougue and ChatGPT

import turtle
import math

print("TurtleDraw Starting...")

filename = input("Enter input file name (e.g., turtledraw.txt): ")

# Set up the screen and turtle
screen = turtle.Screen()
screen.setup(450, 450)

td = turtle.Turtle()
td.speed(0)
td.penup()

try:
    file = open(filename, "r")
except:
    print("File not found.")
    exit()

total = 0
prev_x = None
prev_y = None

for line in file:
    line = line.strip()
    parts = line.split()

    if len(parts) == 1 and parts[0].lower() == "stop":
        td.penup()
        prev_x = None
        prev_y = None
    elif len(parts) == 3:
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        td.color(color)
        td.goto(x, y)

        if prev_x is not None and prev_y is not None:
            distance = math.hypot(x - prev_x, y - prev_y)
            total += distance
            td.pendown()
        else:
            td.penup()

        prev_x = x
        prev_y = y

# Display total distance
td.penup()
td.goto(100, -200)
td.color("black")
td.write(f"Total Distance: {round(total, 2)}", font=("Arial", 12, "bold"))

file.close()

input("Press Enter to exit...")
turtle.done()
