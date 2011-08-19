#!/usr/bin/python2 

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



from helper import * 
import pygtk
pygtk.require('2.0')
import gtk
import gobject
import pango


class MainWindow:
    
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def output_prompt(self, widget, data=None):
        pass
    def __init__(self):
        self.color_dict = {
                'black'   : gtk.gdk.Color(    0,     0,     0),
                'red'     : gtk.gdk.Color(65535,     0,     0),
                'green'   : gtk.gdk.Color(    0, 35553,     0),
                'blue'    : gtk.gdk.Color(    0,     0, 65535),
                'white'   : gtk.gdk.Color(65535, 65535, 65535),
                'yellow'  : gtk.gdk.Color(65535, 65535,     0),
                'magenta' : gtk.gdk.Color(65535,     0, 65535),
                'cyan'    : gtk.gdk.Color(    0, 65535, 65535) }
        self.format_dict = {
                'black'   : '(?bla)',
                'red'     : '(?red)',
                'green'   : '(?grn)',
                'blue'    : '(?blu)',
                'white'   : '(?wht)',
                'yellow'  : '(?ylw)',
                'magenta' : '(?mgta)',
                'cyan'    : '(?cyn)',
                'bold'    : '(?bold)'}
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_title("PyPrompt")
        self.window.add(self._init_main_hbox())
        self.window.show()


    # I made a tree of _init functions :D
    def _init_main_hbox(self):
        self.main_hbox = gtk.HBox()
        self.main_hbox.pack_start(self._init_main_left_alignment(), padding=5)
        self.main_hbox.pack_end(self._init_main_right_vbox(), padding=5)
        self.main_hbox.show()
        return self.main_hbox

    def _init_main_left_alignment(self):
        self.main_left_alignment = gtk.Alignment(xalign=0.0, yalign=0.0, xscale=0.8, yscale=1.0)
        self.main_left_alignment.add(self._init_main_left_vbox())
        self.main_left_alignment.show()
        return self.main_left_alignment

    def _init_main_left_vbox(self):
        self.main_left_vbox = gtk.VBox()
        self.main_left_vbox.pack_start(self._init_text_entry(), padding=5)
        self.main_left_vbox.pack_start(self._init_left_hbox_alignment(), padding=5)
        self.main_left_vbox.show()
        return self.main_left_vbox

    def _init_text_entry(self):
        self.text_entry = gtk.Entry()
        self.text_entry.set_alignment(0.0)
        #TODO: Use a Gtk.TextView instead of a Gtk.Entry 
        def insert_handler(widget, text, length, position, data=None):
            if len(text) == 1:
                if text in  ("?", "\\"):
                    widget.emit_stop_by_name("insert_text")

        #TODO: Burn the delete handler
        #This has to handle deletion of entire tokens, so as to prevent malformed prompts.
        def delete_handler(widget, start, end, data=None):
            start_origin = start
            end_origin = end
            text = widget.get_text()
            pos = widget.get_position()

            def find_token(text, index, flag):
                symbol_start = 0
                symbol_end = 0
                if flag != ")":
                    symbol_end = text.find(")", index-1) + 1
                    if symbol_end < 0:  return None
                else: symbol_end = index+1
                if flag != "(":
                    symbol_start = text.rfind("(", 0, index)
                    if symbol_start < 0: return None
                else: symbol_start = index
                if text[min(len(text)-1, symbol_start+1)] == "?":
                    return (symbol_start, symbol_end)
                else: return None

            tokens = []
            for i in index_all(text, '?', 0, len(text)):
                #print "Index: ", i, "Text: ", text[i]
                token = find_token(text, i+start, '?')
                if token:
                    #print token[0], start, start_origin, end_origin, end, token[1]
                    if start >= start_origin:
                        #print "Replacing start with", min(start, token[0])
                        start = min(start, token[0])
                    if end <= end_origin: 
                        #print "Replacing end with", max(end-1, token[1])
                        end = max(end, token[1])
                        

            widget.disconnect(self.delete_id)
            widget.delete_text(start, end+1)
            self.delete_id = widget.connect("delete_text", delete_handler)
            widget.emit_stop_by_name("delete_text")

        self.text_entry.connect("insert_text", insert_handler)
        self.delete_id = self.text_entry.connect("delete_text", delete_handler)
        self.text_entry.show()
        return self.text_entry

    def _init_left_hbox_alignment(self):
        self.left_hbox_alignment = gtk.Alignment(xalign=0.0, yalign=0.0, xscale=1.0, yscale=1.0)
        self.left_hbox_alignment.add(self._init_left_hbox())
        self.left_hbox_alignment.show()
        return self.left_hbox_alignment

    def _init_left_hbox(self):
        self.left_hbox = gtk.HBox()
        self.left_hbox.pack_start(self._init_color_align(), padding=5)
        self.left_hbox.pack_start(self._init_misc_vbox(), padding=5)
        self.left_hbox.show()
        return self.left_hbox
    
    def _init_color_align(self):
        self.color_align = gtk.Alignment(xalign=0.0, yalign=0.0, xscale=0.75, yscale=1.0)
        self.color_align.add(self._init_color_table())
        self.color_align.show()
        return self.color_align
    
    #TODO: Actually make the buttons the proper colors. Maybe organize them as well... 
    def _init_color_table(self):
        self.color_table = gtk.Table(rows=2, columns=4, homogeneous=True)  
        self.color_buttons = {}
        count = 0

        #Lets make some closure madness
        def create_color_callback(color):
            def color_callback(widget, data=color):
                self._return_to_text()
                self.text_entry.emit('insert_at_cursor', self.format_dict[data])
                
            return color_callback
        
        for color in self.color_dict:
            self.color_buttons[color] = gtk.Button()
            self.color_buttons[color].connect("clicked", create_color_callback(color))
            self.color_buttons[color].show()
            self.color_buttons[color].modify_bg(gtk.STATE_NORMAL, self.color_dict[color])
            self.color_buttons[color].modify_bg(gtk.STATE_PRELIGHT, self.color_dict[color])
            self.color_buttons[color].modify_bg(gtk.STATE_ACTIVE, self.color_dict[color]) 
            self.color_table.attach(
                child         = self.color_buttons[color],
                left_attach   = (count % 4),
                right_attach  = ((count % 4) + 1),
                top_attach    = (count / 4),
                bottom_attach = ((count / 4) + 1),
                xpadding      = 3,
                ypadding      = 3)
            count += 1
        self.color_table.show()
        return self.color_table

    def _init_misc_vbox(self):
        self.misc_vbox = gtk.VBox()
        self.misc_vbox.pack_start(self._init_bold_btn(), padding=3)
        self.misc_vbox.pack_start(self._init_clear_btn(), padding=3)
        self.misc_vbox.show()
        return self.misc_vbox

    def _init_bold_btn(self):
        self.bold_btn = gtk.ToggleButton("_Bold")
        def bold_callback(widget, data=self.bold_btn.get_active()):
            if data:
                self._return_to_text()
                self.text_entry.emit('insert_at_cursor', "(?bold)")
            else:
                self._return_to_text()
                self.text_entry.emit('insert_at_cursor',  '(?norm)')

        self.bold_btn.connect("toggled", bold_callback)
        self.bold_btn.show()
        return self.bold_btn


    def _init_clear_btn(self):
        self.clear_btn = gtk.Button("Clear")
        def clear_handler(widget, data=None):
            self.text_entry.delete_text(0, self.text_entry.get_text_length())
            self._return_to_text()
        self.clear_btn.connect("clicked", clear_handler) 
        self.clear_btn.show()
        return self.clear_btn

    def _init_main_right_vbox(self):
        self.main_right_vbox = gtk.VBox()
        self.main_right_vbox.pack_start(self._init_special_combox(), padding=5)
        self.main_right_vbox.pack_start(self._init_shell_combox(), padding=5)
        self.main_right_vbox.pack_start(self._init_go_btn(), padding=5)
        self.main_right_vbox.show()
        return self.main_right_vbox

    #TODO: Add more of the bash's variables 
    def _init_special_combox(self):
        self.special_combox = gtk.combo_box_new_text()       
        self.special_combox.append_text("Pick a variable to insert!")
        self.special_combox.append_text("Username")
        self.special_combox.append_text("Hostname")
        self.special_combox.append_text("Current Directory (Local)")
        self.special_combox.set_active(0)

        def symbol_combox_changed_handler(widget, data=None):
            symbol_dict = {
                'Pick a variable to insert!': '',
                'Username': '(?u)',
                'Hostname': '(?h)',
                'Current Directory (Local)': '(?ds)'}
            self._return_to_text()
            self.text_entry.emit('insert_at_cursor', symbol_dict[widget.get_active_text()])
            widget.disconnect(self.symbol_combox_changed_id)
            widget.set_active(0)
            self.symbol_combox_changed_id = widget.connect_after(
                    'changed', 
                    symbol_combox_changed_handler)
        self.symbol_combox_changed_id = self.special_combox.connect_after(
                "changed", 
                symbol_combox_changed_handler)
        self.special_combox.show()
        return self.special_combox
    
    #TODO: Add support for more shells.
    def _init_shell_combox(self):
        self.shell_combox = gtk.combo_box_new_text()
        self.shell_combox.append_text("Bash Only :(")
        self.shell_combox.set_active(0)
        self.shell_combox.show()
        return self.shell_combox

    def _init_go_btn(self):
        go_btn = gtk.Button("Make a Prompt!")
        def btn_handler(widget):
            make_prompt(self.text_entry.get_text())
        go_btn.connect("pressed", (lambda widget: make_prompt(self.text_entry.get_text())))
        go_btn.show()
        return go_btn

    def _return_to_text(self):
        self.text_entry.emit('focus', gtk.DIR_RIGHT)
        l = self.text_entry.get_text_length()
        self.text_entry.select_region(l, l)


    def main(self):
        gtk.main()

if __name__ == '__main__':
    window = MainWindow()
    window.main()
