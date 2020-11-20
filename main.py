from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Emma(App):
    def build(self):
        root_widget = BoxLayout(orientation='vertical')

        output_label = Label(size_hint_y=1)

        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')

        #button_grid = GridLayout(cols=4, size_hint_y=2)
        # for symbol in button_symbols:
        #     button_grid.add_widget(Button(text=symbol))

        textinput = TextInput(text='Hello world', size_hint_y = None, height = 30, multiline=False)

        clear_button = Button(text='Listen', size_hint_y=None,
                              height=50)

        root_widget.add_widget(output_label)
        root_widget.add_widget(textinput)
        root_widget.add_widget(clear_button)

        return root_widget

Emma().run()