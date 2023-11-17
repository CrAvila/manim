from manim import *

class MoveToScene(Scene):
    def construct(self):
        s = Circle()
        self.play(s.animate.to_edge(UP + RIGHT))
        self.wait()

        self.play(s.animate.shift(2*DOWN + 2*LEFT))

class MoveToAnotherObject(Scene):
    def construct(self):
        h = Text("Hello")
        s = Square()

        self.add(h, s)

        self.play(h.animate.to_edge(UP))
        self.wait()
        self.play(s.animate.next_to(h, DOWN))
        
        self.wait(2)
