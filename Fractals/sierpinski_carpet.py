import turtle
PROGNAME = 'Sierpinski Carpet'
SIZE = 200
CENTER = [0,0]

#Disable screen refreshing
turtle.tracer(0, 0)

myPen = turtle.Turtle()
myPen.color("#000000")
myPen.penup()

# This function change the size for creating new boxes
def newSize(oldSize):
    return oldSize/3

# This function draws a box by drawing each side of the square and using the fill function
# parameters are the center of box and length of edge
def box(boxSize, middle):
    myPen.goto(middle[0]-(boxSize/2), middle[1]-(boxSize/2))
    myPen.pendown()
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 90 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 180 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 270 deg.
    myPen.forward(boxSize)
    myPen.end_fill()
    myPen.setheading(0)
    myPen.penup()

# function doing recursion for carpet
def carpet(depth, middle, size):
    box(size, middle)
    if depth > 0:
        # Drawing box under
        carpet(depth-1, [middle[0],middle[1]-size], newSize(size))

        #Drawing box above
        carpet(depth-1, [middle[0],middle[1]+size], newSize(size))

        #Drawing 3 boxes on the left
        for i in range(3):
            carpet(depth-1, [middle[0]-size, middle[1]-size + (i * size)], newSize(size))
        #Drawing 3 boxes on the right
        for i in range(3):
            carpet(depth-1, [middle[0]+size, middle[1]-size + (i * size)], newSize(size))

carpet(4, CENTER, SIZE)

# This line couse the window not to close
turtle.mainloop()
