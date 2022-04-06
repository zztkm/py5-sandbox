from py5 import Sketch


class FirstSketch(Sketch):
    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.rect_mode(self.CENTER)

    def draw(self):
        self.rect(self.mouse_x, self.mouse_y, 30, 30)
