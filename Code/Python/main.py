# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:24:18 2019

@author: xingg
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

import os
import webbrowser
import numpy as np
import igraph

from rake_nltk import Rake
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

class RootWidget(BoxLayout):
    '''
    This is the a Box Layout class. We will then add CustomLayout on it.
    '''
    pass

class ShowLayout(GridLayout):
    '''
    This is a Grid Layout that contains graph figure and article text.
    '''
    
    def __init__(self, **kwargs):
        
        '''
        Initial the show layout with a default picture and an empty input box.
        '''
        
        super(ShowLayout, self).__init__(**kwargs)
        self.cols = 2
        self.col_force_default = True
        self.col_default_width = 500
        self.row_force_default=True
        self.row_default_height=500
        self.picture = AsyncImage(
                source="graphs.png",
                size_hint= (1, .8),
                pos_hint={'center_x':.5, 'center_y':.5})
        self.add_widget(self.picture)
        
        self.frequency_text = ''
        self.frequency = TextInput(text = self.frequency_text)
        
        self.add_widget(self.frequency)
        
class SearchLayout(GridLayout):
    
    '''
    Here's a custom layout. Contain a show layout and text layout
    '''
    
    def __init__(self, sg = None, **kwargs):
        super(SearchLayout, self).__init__(**kwargs)
        self.cols = 2
        self.sg_t = sg
        
        self.search_keyword = TextInput(multiline = False, size_hint_y=None, height = 50) 
        self.search_keyword.bind(text = self.name_get_text)
        
        self.idWithTitle = {}
        
        
        self.search_button = Button(text='Search Entity', size_hint_y=None, height = 50, size_hint_x=None, width=250)
        self.search_button.bind(on_press = self.search)
        
        self.dropdown = DropDown()
        
        #print("Hello")
        self.search_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.search_button, 'text', x))
        #runTouchApp(self.search_button)
        
        #self.search_button = Button(text = 'Search Entity') 
        #self.search_button.bind(on_press = self.search)
        self.add_widget(self.search_keyword) #row=9
        self.add_widget(self.search_button) #row=10 
        
    def name_get_text(self, instance, value):
        
        '''
        Get value from input box
        '''
        self.name_text = value
        
    def search(self, instance):
        
        '''
        search articles (as well as attributes) in the graph
        '''
        print("I'm here")
        if self.name_text == '':
            pass
        else:
            file = open('..\\IdWithTitle.csv','r',encoding = 'utf-8')
            lines = file.readlines()
            file.close()
            show_text = ''
            for line in lines:
                temp = line.split('\t')
                if self.name_text in temp[1].lower():
                    self.idWithTitle[temp[0]] = temp[1]
                    show_text += temp[1]
            for key,value in self.idWithTitle.items():
                btn = Button(text=value, size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
                btn.bind(on_press = self.graphSearch)
                self.dropdown.add_widget(btn)
            
            #self.sg_t.frequency.text = show_text
    def graphSearch(self, instance):
        pass


class CustomLayout(GridLayout):
    
    '''
    Here's a custom layout. Contain a show layout and text layout
    '''
    
    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)
        self.rows = 2
        self.row_force_default=True
        self.row_default_height=500
        #self.frequency_text = ''
        self.show_grid = ShowLayout()
        self.add_widget(self.show_grid)
        
        self.search_grid = SearchLayout(self.show_grid)
        self.add_widget(self.search_grid)
            
class MainApp(App):
    '''
    Start the application.
    :return: root
    '''
    def build(self):
        root = RootWidget()
        c = CustomLayout()
        root.add_widget(c)
        return root
    
if __name__ == '__main__':
    MainApp().run()