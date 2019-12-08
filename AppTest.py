from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.uix.camera import Camera
from kivy.uix.effectwidget import EffectWidget, InvertEffect, HorizontalBlurEffect
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout

class LabelKv(Label):
	pass

class BoxLayoutKv(BoxLayout):
	pass

class Button1(Button):
	def on_press(self):
		#self.text = '3333'
		MyApp2().run()
		MyApp().stop()

class Button2(Button):
	def on_press(self):
		MyApp().run()
		MyApp2().stop()

class MyApp(App):
	def build(self):
		b = BoxLayout()
		b.add_widget(Button())
		return BoxLayoutKv()
		b = BoxLayout(orientation = 'vertical')
		b.add_widget(AnchorLagout(Button(size_hint = (.9, .2), pos_hint = {'right':1})))
		b.add_widget(Button())
		return b
		return Button1()
		return Popup(title='Test popup',
		    content=Label(text='Hello world'),
		    size_hint=(None, None), size=(400, 400))
		return FileChooserListView()
		w = EffectWidget()
		w.add_widget(Button(text='Hello!'))
		w.effects = [InvertEffect(), HorizontalBlurEffect(size=2.0)]
		#return w
		#return Camera(resolution=(320, 240))

class MyApp2(App):
	def build(self):
		return Popup(title='Test popup',
		    content=Label(text='Hello world'),
		    size_hint=(None, None), size=(400, 400))

if __name__ == '__main__':
	#print(str(dir(Button())))
	#Button1().text = '111111'
	#print(Button1().text)
	MyApp().run()
