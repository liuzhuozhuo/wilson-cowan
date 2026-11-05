from manim import *

class ExcInhCircuit(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Colors
        exc_color = RED_E
        inh_color = BLUE_E

        # Create E and I circles
        E = Circle(radius=1.0, color=exc_color, fill_opacity=0.5)
        I = Circle(radius=1.0, color=inh_color, fill_opacity=0.5)
        
        # Position them
        E.shift(LEFT * 3)
        I.shift(RIGHT * 3)
        E_label = Tex("E", color=BLACK).move_to(E.get_center())
        I_label = Tex("I", color=BLACK).move_to(I.get_center())

        # Input arrows
        iE = Arrow(UP * 3 + LEFT * 3, E.get_top()+UP*0.3, buff=0.1, color=exc_color)
        iE_label = Tex("$P_E$", color=exc_color).next_to(iE.get_start(), UP)
        iI = Arrow(UP * 3 + RIGHT * 3, I.get_top()+UP*0.3, buff=0.1, color=inh_color)
        iI_label = Tex("$P_I$", color=inh_color).next_to(iI.get_start(), UP)

        # # Recurrent loops
        # loop_E = Arc(
        #     radius=1.3, start_angle=PI / 4, angle=PI * 1.5, arc_center=E.get_center(),
        #     color=exc_color
        # )
        # arrow_E = Arrow(
        #     loop_E.point_from_proportion(0.02),
        #     loop_E.point_from_proportion(0.0),
        #     buff=0, color=exc_color
        # )
        # loop_I = Arc(
        #     radius=1.3, start_angle=-3 * PI / 4, angle=PI * 1.5, arc_center=I.get_center(),
        #     color=inh_color
        # )
        # arrow_I = Arrow(
        #     loop_I.point_from_proportion(0.02),
        #     loop_I.point_from_proportion(0.0),
        #     buff=0, color=inh_color
        # )

        # Cross connections
        W_EI = CurvedArrow(
            E.get_top()+UP*0.2, I.get_top()+UP*0.2, angle=-35 * DEGREES, color=exc_color
        )
        W_IE = CurvedArrow(
            I.get_bottom() +DOWN *0.2, E.get_bottom() +DOWN *0.2, angle=-35 * DEGREES, color=inh_color
        )
        W_EI_label = Tex(r"$W_{EI}$", color=exc_color).next_to(
            W_EI.get_center(), UP*1.5 + RIGHT * 0.2
        )
        W_IE_label = Tex(r"$W_{IE}$", color=inh_color).next_to(
            W_IE.get_center(), DOWN*1.5 + LEFT * 0.2
        )

        W_EE = CurvedArrow(
            E.get_top()+LEFT*0.5, E.get_bottom()+LEFT *0.5, angle=240 * DEGREES, color=exc_color
        )
        W_EE_label = Tex(r"$W_{EE}$", color=exc_color).next_to(
            W_EE.get_center(), UP*5 + LEFT * 3
        )

        W_II = CurvedArrow(
            I.get_bottom()+RIGHT *0.5, I.get_top()+RIGHT*0.5, angle=240 * DEGREES, color=inh_color
        )
        W_II_label = Tex(r"$W_{II}$", color=inh_color).next_to(
            W_II.get_center(), DOWN*5 + RIGHT * 3
        )

        # # Labels for loops
        # W_EE = Tex(r"$W_{EE}$", color=exc_color).next_to(
        #     loop_E.point_from_proportion(0.3), LEFT
        # )
        # W_II = Tex(r"$W_{II}$", color=inh_color).next_to(
        #     loop_I.point_from_proportion(0.3), RIGHT
        # )

        # Assemble
        self.add(E, I, E_label, I_label)
        # self.add(iE, iI, iE_label, iI_label)
        # self.add(W_EI, W_IE, W_EI_label, W_IE_label)
        # self.add(W_EE, W_II, W_EE_label, W_II_label)
        self.play(Create(iE), Write(iE_label), Create(iI), Write(iI_label))
        self.play(Create(W_EI), Write(W_EI_label), Create(W_IE), Write(W_IE_label),Create(W_EE), Write(W_EE_label), Create(W_II), Write(W_II_label), run_time = 1.5)
        self.wait(0.5)

        self.play(FadeOut(iE), FadeOut(iE_label),FadeOut(iI), FadeOut(iI_label),FadeOut(W_EI), FadeOut(W_EI_label),FadeOut(W_IE), FadeOut(W_IE_label)
                  ,FadeOut(W_EE), FadeOut(W_EE_label),FadeOut(W_II), FadeOut(W_II_label))
    
