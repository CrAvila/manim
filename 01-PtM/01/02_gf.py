from manim import *

class GravitationalField(Scene):
    def construct(self):
        # Create a planet
        planet = Sphere(radius=1, color=BLUE_E)
        planet.shift(LEFT*2)
        
        # Create the Laplacian symbol
        laplacian_text = MathTex(r"\nabla^2 V", color=WHITE)
        laplacian_text.shift(RIGHT*3)
        
        # Create gravitational field lines
        field_lines = VGroup()
        for i in range(20):
            line = Line(ORIGIN, UP*3).shift(RIGHT*3)
            line.rotate(TAU / 20 * i, about_point=ORIGIN)
            field_lines.add(line)
        
        # Animate the planet and field lines
        self.play(FadeIn(planet), Write(laplacian_text))
        self.play(ShowCreation(field_lines))
        self.wait(1)
        
        # Animate gravitational potential equation
        equation = MathTex(r"V = -\frac{GM}{r}", color=WHITE)
        equation.next_to(laplacian_text, DOWN)
        self.play(Write(equation))
        self.wait(2)

        # Group everything and fade out
        group = VGroup(planet, laplacian_text, field_lines, equation)
        self.play(FadeOut(group))