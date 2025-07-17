# main.py de ejemplo
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text="¡Hola desde APK de PZSM!")

if __name__ == '__main__':
    MainApp().run()
