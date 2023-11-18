from manim import *

class Rainbow(Scene):
    def construct(self):
        # Create a Text object
        r = Text("RAINBOW")

        # Assign colors to each character
        r[0].set_color(RED)
        r[1].set_color(ORANGE)
        r[2].set_color(YELLOW)
        r[3].set_color(GREEN)
        r[4].set_color(TEAL)
        r[5].set_color(BLUE)
        r[6].set_color(PURPLE)

        # Animate the text
        
        r.scale(3)

        self.play(Write(r), run_time=5)
        self.wait(2)

class Work(Scene):
    def construct(self):
        # Create a custom TexTemplate
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{bigints}")

        # Use the custom template in the Tex object
        w = Tex(r"$W(s) = \bigints \vec{F}\cdot d\vec{s}$", tex_template=myTemplate)
        self.play(Write(w), run_time=5)



