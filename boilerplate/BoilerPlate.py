from gi.repository import Gtk
from gi.repository import Gio
import sys


class MyWindow(Gtk.ApplicationWindow):
	def __init__(self, app, appname, settings):
		Gtk.Window.__init__(self, title=appname, application=app)
		hb = Gtk.HeaderBar()
		hb.props.show_close_button = True
		hb.props.title = appname
		print settings.get_boolean("dark-theme")
		self.set_titlebar(hb)


class MyAboutDialog(Gtk.AboutDialog):
	def __init__(self, appname, parent):
		Gtk.AboutDialog.__init__(self)
		self.set_program_name(appname)
                self.set_transient_for(parent)
                self.set_modal(True)
		self.show()

class MyApplication(Gtk.Application):
	APPNAME = "boilerplate example"
	SETTINGS_KEY = "apps.boilerplate"
	def __init__(self):
		Gtk.Application.__init__(self)

	def do_activate(self):
		self.win = MyWindow(self, self.APPNAME, self.settings)
		self.win.show_all()

	def do_startup(self):
		# start the application
		Gtk.Application.do_startup(self)

		self.settings = Gio.Settings.new(self.SETTINGS_KEY)

		# create a menu
		menu = Gio.Menu()
		# append to the menu three options
		menu.append("New", "app.new")
		menu.append("About", "app.about")
		menu.append("Quit", "app.quit")
		# set the menu as menu of the application
		self.set_app_menu(menu)

		# create an action for the option "new" of the menu
		new_action = Gio.SimpleAction.new("new", None)
		# connect it to the callback function new_cb
		new_action.connect("activate", self.new_cb)
		# add the action to the application
		self.add_action(new_action)

		# option "about"
		about_action = Gio.SimpleAction.new("about", None)
		about_action.connect("activate", self.about_cb)
		self.add_action(about_action)

		# option "quit"
		quit_action = Gio.SimpleAction.new("quit", None)
		quit_action.connect("activate", self.quit_cb)
		self.add_action(quit_action)

	# callback function for "new"
	def new_cb(self, action, parameter):
		print "This does nothing. It is only a demonstration."

	# callback function for "about"
	def about_cb(self, action, parameter):
		about = MyAboutDialog(self.APPNAME, self.win)

	# callback function for "quit"
	def quit_cb(self, action, parameter):
		print "You have quit."
		self.quit()
