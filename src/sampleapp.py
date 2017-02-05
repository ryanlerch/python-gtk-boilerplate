from gi.repository import Gtk
from gi.repository import Gio

import sys

class MyWindow(Gtk.ApplicationWindow):
	def __init__(self, app, appname):
		Gtk.Window.__init__(self, title=appname, application=app)
		self.icontheme = Gtk.IconTheme.get_default()
		self.logo = self.icontheme.load_icon("org.sampleapp.sampleapp", 24, Gtk.IconLookupFlags.NO_SVG)
		self.set_default_icon(self.logo)
		hb = Gtk.HeaderBar()
		hb.props.show_close_button = True
		hb.props.title = "BoilerPlate"
		self.set_titlebar(hb)

class MyAboutDialog(Gtk.AboutDialog):
	def __init__(self, appname, parent):
		Gtk.AboutDialog.__init__(self)
		self.set_program_name(appname)
		self.set_transient_for(parent)
		self.icontheme = Gtk.IconTheme.get_default()
		self.set_logo(self.icontheme.load_icon("org.sampleapp.sampleapp", 96, Gtk.IconLookupFlags.FORCE_SVG))
		self.set_modal(True)
		self.show()

class MyApplication(Gtk.Application):
	APPNAME = "boilerplate"
	def __init__(self, *args, **kwargs):
		Gtk.Application.__init__(self)

	def do_activate(self):
		self.win = MyWindow(self, self.APPNAME)
		self.win.show_all()

	def do_startup(self):
		Gtk.Application.do_startup(self)
		menu = Gio.Menu()
		menu.append("Preferences", "app.show-preferences")
		menu.append("About", "app.about")
		menu.append("Quit", "app.quit")
		self.set_app_menu(menu)
		prefs_action = Gio.SimpleAction.new("show-preferences", None)
		prefs_action.connect("activate", self.prefs_cb)
		self.add_action(prefs_action)
		about_action = Gio.SimpleAction.new("about", None)
		about_action.connect("activate", self.about_cb)
		self.add_action(about_action)
		quit_action = Gio.SimpleAction.new("quit", None)
		quit_action.connect("activate", self.quit_cb)
		self.add_action(quit_action)

	def prefs_cb(self, action, parameter):
		print("This does nothing. It is only a demonstration.")

	def about_cb(self, action, parameter):
		about = MyAboutDialog(self.APPNAME, self.win)

	def quit_cb(self, action, parameter):
		self.quit()
