from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

class TebakApp(App):
    def build(self):
        self.angka = random.randint(1, 10)
        self.kesempatan = 3

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Tebak angka dari 1-10 (3 kesempatan)")
        self.input = TextInput(hint_text="Masukkan angka", multiline=False, input_filter='int')
        self.button = Button(text="Tebak", on_press=self.cek_tebakan)
        self.result = Label(text="")

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.result)
        return self.layout

    def cek_tebakan(self, instance):
        try:
            tebakan = int(self.input.text)
            if tebakan == self.angka:
                self.result.text = f"🎉 Benar! Angkanya {self.angka}"
            else:
                self.kesempatan -= 1
                if self.kesempatan == 0:
                    self.result.text = f"😢 Habis! Angkanya {self.angka}"
                else:
                    self.result.text = f"❌ Salah! Sisa: {self.kesempatan}"
        except:
            self.result.text = "⚠️ Masukkan angka valid"
        self.input.text = ""

TebakApp().run()
