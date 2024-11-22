from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        self.label = Label(text="Hello, Kivy!")
        self.button = Button(text="Click Me")

        # When the button is pressed, change the label text
        self.button.bind(on_press=self.change_text)

        # Layout to hold the label and button
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(self.button)

        return layout

    def change_text(self, instance):
        # Change the label's text
        self.label.text = "Button Clicked!"

if __name__ == '__main__':
    MyApp().run()
