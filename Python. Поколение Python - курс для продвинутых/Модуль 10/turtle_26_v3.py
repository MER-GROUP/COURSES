import turtle as t


rad = 100  # main radius (adjustable)

bear = {
    "face": [(0, 0), rad],
    "nose": [(0, 0), rad*0.6],
    "ear_right": [(rad*0.8, rad*2-rad*0.28), rad*0.3],
    "ear_left": [(-rad*0.8, rad*2-rad*0.28), rad*0.3],
    "nose_tip": [((0, rad*0.8)), rad*0.1],
    "eye_right": [(rad*0.5, rad+rad*0.2), rad*0.2],
    "eye_left": [(-rad*0.5, rad+rad*0.2), rad*0.2],
    "mouth": [(0, rad*0.8), (0, rad*0.3)],
}

for name, value in bear.items():
    t.penup()
    if 'eye' in name:
        t.goto(value[0])
        t.pendown()
        t.dot(value[1])
    elif name == "mouth":
        t.goto(value[0])
        t.pendown()
        t.goto(value[1])
    else:
        t.goto(value[0])
        t.pendown()
        t.circle(value[1])

t.hideturtle()
t.done()