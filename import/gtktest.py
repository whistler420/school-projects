import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class testWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="funny joke")
		self.button = Gtk.Button(label="click me for a funny joke")
		self.button.connect("clicked",self.on_button_clicked)
		self.add(self.button)
	def on_button_clicked(self, widget):
		print("test")
test = testWindow()
test.connect("destroy",Gtk.main_quit)
test.show_all()
Gtk.main()
