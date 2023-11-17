from manim import *

class MoveToScene(Scene):
    def construct(self):
        s = Circle()
        self.play(s.animate.to_edge(UP + RIGHT))