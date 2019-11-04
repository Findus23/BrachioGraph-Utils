import turtle


def goto(t: turtle.Turtle, x, y, scale, xoffset, yoffset):
    t.setposition(x * scale + xoffset, y * scale + yoffset)


def plot(lines, *args, **kwargs):
    t = turtle.Turtle()

    t.penup()
    goto(t, *lines[0][0], *args, **kwargs)
    t.pendown()
    for line in lines:
        # t.penup()
        t.color("red")
        goto(t, *line[0], *args, **kwargs)
        t.color("black")
        # t.pendown()
        for point in line[1:]:
            goto(t, *point, *args, **kwargs)

    turtle.done()
