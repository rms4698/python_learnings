from math import inf
from posixpath import pardir
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os
import json
import glob
from json import JSONDecodeError
import time
import random
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


dir = os.path.dirname(__file__)

Builder.load_file(os.path.join(dir, "design.kv"))


class LoginSuccessScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def enligten_me(self):
        feeling = self.ids.feeling.text.lower()
        feelings_list = ["happy", "sad", "unloved"]
        available_feelings = glob.glob('Quotes/*.txt')
        available_feelings = [Path(i).stem for i in available_feelings]
        if feeling not in feelings_list:
            self.ids.quote.text = "Try another feeling"
        else:
            with open(f'Quotes/{feeling}.txt', 'r', encoding='utf-8') as f:
                quotes = f.readlines()

            self.ids.quote.text = random.choice(quotes)


class SignupSuccessScreen(Screen):
    def go_to_login_page(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class SignupScreen(Screen):
    def add_user(self, username, password):
        # Create a file if it is not there
        if not os.path.exists('UserDB.json'):
            f = open("UserDB.json", "w")
            f.close()

        # Read the content from JSON
        with open('UserDB.json', 'r') as f:
            try:
                info = json.load(f)
            except JSONDecodeError:
                info = {}

        # Add the current user content
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        info[username] = {"username": username,
                          "password": password, "created": time_string}

        # Write the content to json
        with open('UserDB.json', 'w') as f:
            json.dump(info, f)

        self.manager.current = 'signup_success_screen'


class ForgotPWScreen(Screen):
    def get_password(self, username):
        with open('UserDB.json', 'r') as f:
            try:
                info = json.load(f)
            except JSONDecodeError:
                info = {}

        if username in info:
            self.ids.password.text = f'Your Password is "{info[username]["password"]}"'
        else:
            self.ids.password.text = "User name doesn't exist"

    def go_to_login(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'login_screen'


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'signup_screen'

    def forgot_password(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "forgot_pw_screen"

    def log_in(self, username, password):
        # Read the content from JSON
        with open('UserDB.json', 'r') as f:
            try:
                info = json.load(f)
            except JSONDecodeError:
                info = {}
        if username in info and info[username]["password"] == password:
            self.manager.transition.direction = 'right'
            self.manager.current = "login_success_screen"
        else:
            self.ids.mismatch.text = "Wrong user name & Password"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass




class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
