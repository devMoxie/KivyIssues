from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.lang import Builder

kv = """
<Cell>:
    size_hint: (None, None)
    width: 400
    height: 60
    canvas.before:
        Color:
            rgba: [0.23, 0.23, 0.23, 1] if self.is_even else [0.2, 0.2, 0.2, 1]
        Rectangle:
            pos: self.pos
            size: self.size

<Table>:
    grid: grid
    bar_width: 25
    scroll_type: ['bars', 'content']
    bar_color: [0.4, 0.7, 0.9, 1]
    bar_inactive_color: [0.2, 0.7, 0.9, .5]
    do_scroll_x: True
    do_scroll_y: True
    GridLayout:
        id: grid
        cols: 15
        rows: 30
        size_hint: (None, None)
        width: self.minimum_width
        height: self.minimum_height
"""

Builder.load_string(kv)


class Cell(Label):
    is_even = BooleanProperty(None)


class Table(ScrollView):

    grid = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)

        for i in range(30):
            for j in range(15):
                text = "data row: {}, column: {}".format(i, j)
                self.grid.add_widget(Cell(text=text, is_even=i % 2 is 0))


class TestApp(App):
    def build(self):
        return Table()


if __name__ == '__main__':
    TestApp().run()
