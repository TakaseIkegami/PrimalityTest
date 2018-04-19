#__author__ = 'crolera'
#-*- coding: utf-8 -*-

from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

import random

class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):
        self.text =  self.ids["text_box"].text

"""Miller-Rabin Primality Test
    def primarity_test(q, k = 50):
        q = abs(q)

        if q == 2: return True
        if q < 2 or q & 1 == 0: return False

        d = (q - 1) >> 1
        while d & 1 == 0:
            d >>= 1

        for i in range(k):
            a = random.randint(1, q-1)
            t = d
            y = pow(a, t, q)
            while t != q-1 and y != 1 and y != q-1:
                y = pow(y, 2, q)
                t <<= 1
            if y != q-1 and t & 1 == 0:
                return False
        return True"""

class IsPrimeApp(App):
    def __init__(self, **kwargs):
        super(IsPrimeApp, self).__init__(**kwargs)

    def build(self):
        self.title = 'Miller-Rabin Primality Test'
        return TextWidget()

if __name__ == '__main__':
    IsPrimeApp().run()
