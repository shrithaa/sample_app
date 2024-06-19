from kivymd.app import MDApp
import bluetooth
from kivymd.uix.screen import Screen
from kivy.lang import Builder

from kivymd.uix.button import *
from bluetooth import Protocols
bd_addr = "B8:27:EB:4D:30:73"
port = 1
username_helper="""
MDTextField:
    hint_text:"Enter Username"
    helper_text:"forgot username/password"
    helper_text_mode:"persistent"
    icon_right:"android" 
    icon_right_color:app.theme_cls.primary_color 
    pos_hint: {'center_x': 0.5,'center_y': 0.5}
    size_hint_x: None
    width: 300
"""
password_helper="""
MDTextField:
    hint_text:"Enter Password"
    icon_right:"android" 
    pos_hint: {'center_x': 0.5,'center_y': 0.4}
    size_hint_x: None
    width: 300
"""



class demo(MDApp):
    def build(self):
        screen=Screen()
        self.theme_cls.primary_palette="Teal"
        '''self.username=Builder.load_string(username_helper)
        self.password=Builder.load_string(password_helper)'''
        enter_button=MDFillRoundFlatButton(text="Enter",pos_hint= {'center_x': 0.5,'center_y': 0.3},on_release=self.enter_button_clicked)
        '''screen.add_widget(self.username)
        screen.add_widget(self.password)'''
        screen.add_widget(enter_button)
        return screen
    def enter_button_clicked(self,obj):
        sock = bluetooth.BluetoothSocket(Protocols.RFCOMM)
        sock.connect((bd_addr, port))

        sock.send("hello hi".encode('utf-8'))
        ethernet_connections = sock.recv(1024)
        print(ethernet_connections)
        sock.close()

demo().run()


