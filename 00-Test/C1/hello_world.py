from manim import *
import numpy as np 

class HelloWorld(Scene):
    def construct(self):
        T = Text("Hello World");
        self.play(Write(T), run_time=4)
        self.play(FadeOut(T), run_time=1)
        self.wait()

        # Figures
        circle = Circle()
        square = Square()
        line = Line(np.array([-2, -2, 0]), np.array([2, 2, 0]))
        triangle = Polygon(np.array([-2,-2,0]), np.array([2, 2, 0]), np.array([2, -2, 0]))

        # Circle
        self.play(Create(circle), run_time=3)
        self.play(FadeOut(circle), run_time=1)

        # Square
        self.play(Create(square), run_time=3)
        self.play(FadeOut(square), run_time=1)

        # Line
        self.play(Create(line), run_time=3)
        self.play(FadeOut(line), run_time=1)

        # Triangle
        self.play(Create(triangle), run_time=3)
        self.play(FadeOut(triangle), run_time=1)