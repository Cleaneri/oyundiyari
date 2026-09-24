from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class UygulamaApp(App):
    def build(self):
        # Pencere başlığını ayarlıyoruz
        self.title = "Uygulama"
        
        # Pencere boyutunu ayarlıyoruz (Android'de tam ekran olur)
        Window.size = (300, 150)
        
        # Elemanları üstten aşağıya doğru dizmek için dikey (vertical) bir düzen oluşturuyoruz
        duzen = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Ekrana yazılacak metin (Etiket)
        yazi = Label(
            text="Yakında birçok oyun olacak.", 
            font_name="Arial" if Window.platform == "win" else "Roboto", 
            font_size='16sp'
        )
        duzen.add_widget(yazi)
        
        # Kapatma butonu (command yerine on_press kullanılır)
        kapat_butonu = Button(
            text="Kapat", 
            background_normal='', 
            background_color=(1, 0, 0, 1),  # Kırmızı renk (RGBA formatında)
            color=(1, 1, 1, 1),            # Beyaz yazı
            font_size='14sp', 
            bold=True,
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': 0.5}      # Butonu ortalar
        )
        kapat_butonu.bind(on_press=self.kapat)
        duzen.add_widget(kapat_butonu)
        
        return duzen

    def kapat(self, instance):
        # Uygulamayı kapatır
        App.get_running_app().stop()

if __name__ == '__main__':
    UygulamaApp().run()
