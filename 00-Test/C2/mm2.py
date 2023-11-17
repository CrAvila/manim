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
        self.play(s.animate.next_to(h, DOWN))

        sandt = VGroup(h, s)

        self.play(sandt.animate.rotate(PI/4))

        self.play(sandt.animate.shift(2*DOWN))
        
        self.wait(2)

class ColorChange(Scene):
    def construct(self):
        t = Text("Some Text")
        t.set_color(YELLOW_E)
        self.play(Write(t), run_time=3)
        
        self.play(t.animate.scale(3))

        self.play(t.animate.set_color_by_gradient(GREEN_E, PURPLE_E))

        self.wait()
