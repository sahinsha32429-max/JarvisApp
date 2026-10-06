from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.04, 0.10, 1)

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=25
        )

        title = Label(
            text="J.A.R.V.I.S",
            font_size=38,
            color=(0, 0.8, 1, 1)
        )

        status = Label(
            text="Hello Sahin!\nI am your Jarvis Assistant.",
            font_size=22,
            color=(1, 1, 1, 1)
        )

        button = Button(
            text="START JARVIS",
            font_size=22,
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 0.9, 1)
        )

        layout.add_widget(title)
        layout.add_widget(status)
        layout.add_widget(button)

        return layout

JarvisApp().run()

