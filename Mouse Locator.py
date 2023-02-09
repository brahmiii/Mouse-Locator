from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
import pyautogui
Window.size = (250, 30)
class Mouse_Locator(App):
    def build(self):
        return Builder.load_string("""
BoxLayout:
    Button:
        background_color:"black"
        color:"white"
        id: mouse
""")
    
    def on_start(self):
        self.function_interval=Clock.schedule_interval(self.update_label, 0)
    def update_label(self, *args):
        self.root.ids.mouse.text="Mouse "+str(pyautogui.position())
if __name__ == "__main__":
    Mouse_Locator().run()

