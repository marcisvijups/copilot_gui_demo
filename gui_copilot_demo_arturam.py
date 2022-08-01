# import a gui for the copilot demo

import tkinter as tk
import random


def main():
    root = tk.Tk()
    root.title("Copilot Demo")
    root.geometry("800x600")
    # create a canvas
    canvas = tk.Canvas(root, width=600, height=600)
    # add a button at the top of the window
    button = tk.Button(root, text="Draw Random Lines",
                       command=lambda: draw_random_lines(canvas))
    # add anothe button at the top of the window to draw circles and rectangles
    button2 = tk.Button(root, text="Draw Random Circles and Rectangles",
                        command=lambda: draw_random_circles_and_rectangles(canvas))
    button2.pack()
    # add a button next to other buttons that draws random circles and rectangles
    button.pack()
    # pack the canvas
    canvas.pack()

    # start the event loop  and wait for the window to be closed   (this is the main loop)
    root.mainloop()


# function that draws random circles and rectangles
def draw_random_circles_and_rectangles(canvas):
    # randomise the colour of the shapes
    colour = random.choice(
        ["red", "green", "blue", "yellow", "orange", "purple"])
    # get a random number of circles and rectangles to draw
    num_circles = random.randint(100, 1000)
    num_rectangles = random.randint(100, 1000)
    # draw the circles and rectangles
    for i in range(num_circles):
        # get random coordinates
        x1 = random.randint(0, 600)
        y1 = random.randint(0, 600)
        x2 = random.randint(0, 600)
        y2 = random.randint(0, 600)
        # draw the circle
        canvas.create_oval(x1, y1, x2, y2, fill=colour)
    for i in range(num_rectangles):
        # get random coordinates
        x1 = random.randint(0, 600)
        y1 = random.randint(0, 600)
        x2 = random.randint(0, 600)
        y2 = random.randint(0, 600)
        # draw the rectangle
        canvas.create_rectangle(x1, y1, x2, y2, fill=colour)


# function that draws random lines on the canvas
def draw_random_lines(canvas):
    # get a random number of lines to draw
    num_lines = random.randint(100, 1000)
    # draw the lines
    for i in range(num_lines):
        # get random coordinates
        x1 = random.randint(0, 600)
        y1 = random.randint(0, 600)
        x2 = random.randint(0, 600)
        y2 = random.randint(0, 600)
        # draw the line
        canvas.create_line(x1, y1, x2, y2)


if __name__ == "__main__":
    main()
