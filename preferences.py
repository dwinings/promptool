import pygtk
pygtk.require('2.0')
import gtk

class Preferences:
    def __init__(self):
        self.text_reset = True
        self.shell = "bash"
        self.textview_bg = gtk.gdk.Color(65535, 65535, 65535)

class PrefWindow:

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", (lambda widget, data=None: gtk.main_quit()))
        self.window.set_title("PyPrompt: Preferences")
        self.window.add(self._init_main_vbox())
        self.window.show()

    def _init_main_vbox(self):
       self.main_vbox = gtk.VBox(homogeneous=True, spacing=5)
       self.main_vbox.pack_start(self._init_textview_color_selector(), padding=5)
       self.main_vbox.pack_start(self._init_text_reset_toggle(), padding=5)
       self.main_vbox.pack_start(self._init_shell_combox(), padding=5)
       self.main_vbox.show()
       return self.main_vbox

    def _init_textview_color_selector(self):
        self.textview_color_selector = gtk.ColorSelection()
        self.textview_color_selector.show()
        return self.textview_color_selector

    def _init_text_reset_toggle(self):   
        self.fg_reset_toggle = gtk.CheckButton(label="Reset text color after prompt")
        self.fg_reset_toggle.show()
        return self.fg_reset_toggle

    def _init_shell_combox(self):
        self.shell_combox = gtk.combo_box_new_text()
        self.shell_combox.append_text("Bash Only :(")
        self.shell_combox.set_active(0)
        self.shell_combox.show()
        return self.shell_combox


