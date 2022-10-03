import py5

r = None
x = None
s = "0"


def setup():
    py5.size(600, 300)
    py5.background(0)
    global r
    r = min(py5.width, py5.height)
    global x
    x = r


def draw():
    global x
    x += 10
    if x > py5.width + r:
        x = -r

    py5.background(0)
    py5.circle(x, py5.height / 2, r)

    if py5.frame_count % 30 == 0:
        global s
        s = int(py5.get_frame_rate())

    py5.push()
    py5.no_stroke()
    py5.fill(240)
    py5.text(s, 20, 20)
    py5.pop()


py5.run_sketch()
