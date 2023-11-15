from manim import *

class IntroScene(MovingCameraScene):
    def construct(self):
        # Configuración de título y subtítulos
        title = Text("El Laplaciano en la Ciencia", font_size=36).to_edge(UP)
        subtitle = Text("Un patrón universal en las matemáticas y la física", font_size=24).next_to(title, DOWN)
        
        # Mostrar el título y el subtítulo
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)

        # Desvanecer el subtítulo y prepararse para la próxima escena
        self.play(FadeOut(subtitle))
        
        # Introducción del Laplaciano
        laplacian_def = MathTex("\\Delta^2 V", "=", "\\frac{\\partial^2 V}{\\partial x^2}", "+", "\\frac{\\partial^2 V}{\\partial y^2}", "+", "\\frac{\\partial^2 V}{\\partial z^2}", font_size=32)
        self.play(Write(laplacian_def))
        self.wait(2)
        
        # Transición a la representación gráfica
        self.play(FadeOut(laplacian_def))
        
        # Representación gráfica del espacio y la curvatura
        axes = ThreeDAxes()
        func = lambda pos: np.sin(pos[0]) * np.cos(pos[1])
        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(axes.c2p(u, v))),
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            resolution=(32, 32)
        )
        
        # Configurar la orientación de la cámara en 3D
        self.camera.set_euler_angles(phi=75 * DEGREES, theta=30 * DEGREES)

        # Agregar la rotación continua a la cámara
        self.camera.add_updater(lambda m, dt: m.increment_theta(0.1 * dt))
        self.add(axes, surface)
        self.wait(10)  # Duración de la rotación de la cámara

        # Detener la rotación de la cámara
        self.camera.remove_updater(lambda m, dt: m.increment_theta(0.1 * dt))

        # Añadir ejes y superficie
        self.play(Create(axes), Create(surface))
        self.wait(4)
        
        # Explicar la fórmula del Laplaciano con la superficie
        self.play(FadeOut(axes), FadeOut(surface))
        
        # Separación de la ecuación del Laplaciano
        laplacian_terms = laplacian_def[2:].copy()
        self.play(TransformMatchingShapes(laplacian_def, laplacian_terms))
        self.wait(2)
        
        # Crear íconos para representar cada término de la derivada
        icons = VGroup(
            MathTex("\\frac{\\partial}{\\partial x}").set_color(RED),
            MathTex("\\frac{\\partial}{\\partial y}").set_color(GREEN),
            MathTex("\\frac{\\partial}{\\partial z}").set_color(BLUE)
        ).arrange(RIGHT, buff=1).next_to(laplacian_terms, DOWN)
        
        # Animar los íconos junto con los términos de las derivadas
        self.play(FadeIn(icons))
        for icon, term in zip(icons, laplacian_terms[::2]):
            self.play(
                Indicate(icon),
                Indicate(term)
            )
        self.wait(2)
        
        # Conclusión enfatizando la importancia del concepto
        conclusion = Text("Crucial para múltiples disciplinas científicas", font_size=28).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)

        # Despedida de la escena
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
