#  promptool - A tool to create prompts for POSIX shells, written in python and GTK
#  Copyright (C) 2011 - David Winings
# 
#  promptool is free software: you can redistribute it and/or modify it under the terms
#  of the GNU General Public License as published by the Free Software Found-
#  ation, either version 3 of the License, or (at your option) any later version.
#
#  promptool is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#  PURPOSE.  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along with promptool.
#  If not, see <http://www.gnu.org/licenses/>.

import pygtk
pygtk.require('2.0')
import gtk

class Preferences(object):
    def __init__(self):
        self.text_reset = True
        self.shell = "bash"
        self.textview_bg = gtk.gdk.Color(65535, 65535, 65535)

    def set(self, pref):                       #def void set(self, Preferences pref)
        self.text_reset = pref.text_reset      #Python's lack of optional type specifications bothers me...
        self.shell = pref.shell
        self.textview_bg = pref.textview_bg

    def __eq__(self, pref):
        if self.text_rest == pref.text_reset   and \
           self.shell == pref.shell            and \
           self.textview_bg == pref.textview_bg:
            return True
        else:
            return False

class PrefWindow(gtk.Dialog):

    def __init__(self, pref_in, parent=None, flags=0, buttons=None):
        super(PrefWindow, self).__init__('Promptool: Preferences', parent, flags, buttons)
        self.pref_global = pref_in
        print id(self.pref_global)
        self.pref_local = Preferences()
        self.connect("destroy", self.destroy_handler)
        self.add_button('Ok', 1)
        self.add_button('Cancel', 2)
        self.connect('response', self._response_handler)
        self._pack_vbox()


    def destroy_handler(self, widget, data=None):
        return False

    def _pack_vbox(self):
       self.vbox.pack_start(self._init_textview_color_selector(), padding=5)
       self.vbox.pack_start(self._init_text_reset_toggle(), padding=5)
       self.vbox.pack_start(self._init_shell_combox(), padding=5)

    def _init_textview_color_selector(self):
        self.textview_color_selector = gtk.ColorSelection()
        self.textview_color_selector.show()
        return self.textview_color_selector

    def _init_text_reset_toggle(self):   
        self.fg_reset_toggle = gtk.CheckButton(label="Reset text color after prompt")
        self.fg_reset_toggle.active = self.pref_global.text_reset
        def toggle_handler(widget, data=None):
            self.pref_local.text_reset = self.fg_reset_toggle.get_active()
            print self.pref_local.text_reset
        self.fg_reset_toggle.connect('toggled', toggle_handler)
        self.fg_reset_toggle.show()
        return self.fg_reset_toggle

    def _init_shell_combox(self):
        self.shell_combox = gtk.combo_box_new_text()
        self.shell_combox.append_text("Bash Only :(")
        self.shell_combox.set_active(0)
        self.shell_combox.show()
        return self.shell_combox

    def _response_handler(self, widget, response_id):
        if response_id == 1:
            self.pref_global.set(self.pref_local)
            self.destroy()
        elif response_id == 2:
            self.destroy()

    def main(self):
        gtk.main()

if __name__ == '__main__':
    window = PrefWindow()
    window.main()
