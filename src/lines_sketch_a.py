import random

from typing import List
from py5 import Sketch


class Line:
    def __init__(self, ax: int, ay: int, bx: int, by: int, color: str) -> None:
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.color = color

    def set_stroke(self, stroke) -> None:
        self.stroke = stroke

    def set_line(self, line) -> None:
        self.line = line

    def draw(self) -> None:
        r = int(self.color[0:2], 16)
        g = int(self.color[2:4], 16)
        b = int(self.color[4:], 16)
        self.stroke(r, g, b)
        self.line(self.ax, self.ay, self.bx, self.by)

    def update_ax(self, ax) -> None:
        self.ax = ax


class LinesSketchA(Sketch):
    def settings(self):
        self.lines: List[Line] = []
        self.size(600, 600)

    def setup(self):
        self.frame_rate(5)
        self.color_mode(self.HSB, 360, 100, 100, 100)
        self.background(1)

        urls: List[str] = [
            "https://coolors.co/757bc8-8187dc-8e94f2-9fa0ff-ada7ff-bbadff-cbb2fe-dab6fc-ddbdfc-e0c3fc",
            "https://coolors.co/fec5bb-fcd5ce-fae1dd-f8edeb-e8e8e4-d8e2dc-ece4db-ffe5d9-ffd7ba-fec89a",
            "https://coolors.co/03045e-023e8a-0077b6-0096c7-00b4d8-48cae4-90e0ef-ade8f4-caf0f8",
        ]
        url = random.choice(urls)
        # urlからカラーコード部分を取得し、`-` 区切りのリストを生成
        # 生成されたリストの要素それぞれに `#` を付け足す
        palette = url.split("/").pop().split("-")
        print(palette)

        n = random.randint(50, 300)
        for i in range(n):
            c = random.choice(palette)
            px = self.random(self.width)
            py = self.random(self.height)
            line = Line(px, py, self.width, py, c)
            line.set_line(self.line)
            line.set_stroke(self.stroke)
            line.draw()
            self.lines.append(line)

    def draw(self):
        self.background(1)
        for line in self.lines:
            line.update_ax(self.random(self.width))
            line.draw()
