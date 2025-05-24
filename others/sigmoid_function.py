from manim import *

# Square format settings
config.pixel_width = 1080
config.pixel_height = 1080
config.frame_width = 10      # Scene units (adjust to your preference)
config.frame_height = 10

class SigmoidFunction(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-1.2, 1.2, 0.2],
            x_length=8,
            y_length=8,
            axis_config={"include_tip": True,
                         "include_numbers": True,
                         "color": BLACK,
                         }
        )
        axes.add_coordinates()
        self.add(axes)
        #self.play(Create(axes))

        sigmoid = lambda x: 1 / (1 + np.exp(-x))
        sigmoid_graph = axes.plot(sigmoid, color=RED_D, stroke_width=4)

        # Create label and move to left of x=0
        sigmoid_label = MathTex(r"f(x) = \frac{1}{1 + e^{-x}}").set_color(RED_D).set_stroke(width=2)
        sigmoid_label.move_to(axes.c2p(-4, 0.6))

        #self.add(sigmoid_graph, sigmoid_label)
        self.play(Create(sigmoid_graph), Write(sigmoid_label))
        self.wait(0.5)

        tanh = lambda x: np.tanh(x)
        tanh_graph = axes.plot(tanh, color=BLUE, stroke_width=4)

        # Create label and move to left of x=0
        tanh_label = MathTex(r"f(x) = \tanh x").set_color(BLUE).set_stroke(width=2)
        tanh_label.move_to(axes.c2p(-4, -0.6))

        #self.add(tanh_graph, tanh_label)
        self.play(Create(tanh_graph), Write(tanh_label))
        self.wait(2)