import gtk.gdk
import pango

color_dict = { 'black' : gtk.gdk.Color(0, 0, 0),
                'red'     : gtk.gdk.Color(65535,     0,     0),
                'green'   : gtk.gdk.Color(    0, 35553,     0),
                'blue'    : gtk.gdk.Color(    0,     0, 65535),
                'white'   : gtk.gdk.Color(65535, 65535, 65535),
                'yellow'  : gtk.gdk.Color(65535, 65535,     0),
                'magenta' : gtk.gdk.Color(65535,     0, 65535),
                'cyan'    : gtk.gdk.Color(    0, 65535, 65535) }

format_dict = { 
                (pango.WEIGHT_NORMAL, 'black'  ) : '(?bla)',
                (pango.WEIGHT_NORMAL, 'red'    ) : '(?red)',
                (pango.WEIGHT_NORMAL, 'green'  ) : '(?grn)',
                (pango.WEIGHT_NORMAL, 'blue'   ) : '(?blu)',
                (pango.WEIGHT_NORMAL, 'white'  ) : '(?wht)',
                (pango.WEIGHT_NORMAL, 'yellow' ) : '(?ylw)',
                (pango.WEIGHT_NORMAL, 'magenta') : '(?mgta)',
                (pango.WEIGHT_NORMAL, 'cyan'   ) : '(?cyn)',
                (pango.WEIGHT_NORMAL, 'reset'  ) : '(?reset)',

                (pango.WEIGHT_BOLD, 'black'  ) : '(?bla_b)',
                (pango.WEIGHT_BOLD, 'red'    ) : '(?red_b)',
                (pango.WEIGHT_BOLD, 'green'  ) : '(?grn_b)',
                (pango.WEIGHT_BOLD, 'blue'   ) : '(?blu_b)',
                (pango.WEIGHT_BOLD, 'white'  ) : '(?wht_b)',
                (pango.WEIGHT_BOLD, 'yellow' ) : '(?ylw_b)',
                (pango.WEIGHT_BOLD, 'magenta') : '(?mgta_b)',
                (pango.WEIGHT_BOLD, 'cyan'   ) : '(?cyn_b)',
                (pango.WEIGHT_BOLD, 'reset'  ) : '(?reset)'}

symbol_dict = { 'Pick a variable to insert!': '',
                'Username': '(?u)',
                'Hostname': '(?h)',
                'Current Directory (short)': '(?W)',
                'Date'    :'(?d)',
                'Hostname (Long)' : '(?H)',
                'Number of Jobs in the Shell' :'(?j)',
                'Current Shell' : '(?s)',
                'Time (24-hr)' : '(?t)',
                'Time (12-hr)' : '(?@)',
                'Shell Version (short)' : '(?v)',
                'Shell Version (long)' : '(?V)',
                'Current Directory (long)' : '(?w)',
                'History Number' : '(?!)',
                'Command Number (in terminal)' : r'(?#)'}
