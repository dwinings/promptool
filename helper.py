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



def index_all(text, sub, start, finish):
    l = []
    #print text[start:finish], sub
    text = text[start:finish]
    i = text.find(sub)
    while i > -1:
        l.append(i)
        i = text.find(sub, i+1)
    #print l
    return l


def make_prompt(string):
    color_escapes = {
                ("(?bla)"  , "(?norm)") : r'\[\033[0;30m\]',
                ("(?red)"    , "(?norm)") : r'\[\033[0;31m\]',
                ("(?grn)"  , "(?norm)") : r'\[\033[0;32m\]',
                ("(?ylw)" , "(?norm)") : r'\[\033[0;33m\]',
                ("(?blu)"   , "(?norm)") : r'\[\033[0;34m\]',
                ("(?mgta)", "(?norm)") : r'\[\033[0;35m\]',
                ("(?cyn)"   , "(?norm)") : r'\[\033[0;36m\]',
                ("(?wht)"  , "(?norm)") : r'\[\033[0;37m\]',

                ("(?bla)"  , "(?bold)") : r'\[\033[1;30m\]',
                ("(?red)"    , "(?bold)") : r'\[\033[1;31m\]',
                ("(?grn)"  , "(?bold)") : r'\[\033[1;32m\]',
                ("(?ylw)" , "(?bold)") : r'\[\033[1;33m\]',
                ("(?blu)"   , "(?bold)") : r'\[\033[1;34m\]',
                ("(?mgta)", "(?bold)") : r'\[\033[1;35m\]',
                ("(?cyn)"   , "(?bold)") : r'\[\033[1;36m\]',
                ("(?wht)"  , "(?bold)") : r'\[\033[1;37m\]' }

    special_escapes = {
            '(?u)' : r'\u',
            '(?h)' : r'\h',
            '(?w)' : r'\w',
            '(?d)' : r'\d',
            '(?H)' : r'\H',
            '(?j)' : r'\j',
            '(?s)' : r'\s',
            '(?t)' : r'\t',
            '(?@)' : r'\@',
            '(?v)' : r'\v',
            '(?V)' : r'\V',
            '(?W)' : r'\W',
            '(?!)' : r'\!',
           r'(?#)' : r'\#',
            '(?$)' : r'\$',
	 '(?reset)': r'\[\e[0m'}

    colors = {'(?bla)', '(?red)', '(?grn)', '(?ylw)', '(?blu)', '(?mgta)', '(?cyn)', '(?wht)'}
    formats = {'(?bold)', '(?norm)'}
    specials = {'(?u)', '(?h)', '(?w)', '(?d)', '(?H)'}
    current_color = '(?bla)'
    current_style = '(?norm)'
    text_left = True
    itr = enumerate(list(string))
    output = ['PS1="']
    while text_left:
        char = itr.next()
        if char[1] == "(":
            if string[char[0]+1] == "?":
                symbol = ['(']
                while char[1] != ')':
                    try:
                        char = itr.next()
                        symbol.append(char[1])
                    except:
                        print "Unclosed paren, aborting... :("
                        return
                symbol = ''.join(symbol)
                if symbol in colors:
                    current_color = symbol
                    output.append(color_escapes[(current_color, current_style)])
                elif symbol in special_escapes:
                    output.append(special_escapes[symbol])
                elif symbol in formats:
                    current_style = symbol
                    output.append(color_escapes[(current_color, current_style)])

                else:
                    print "Valid symbol", symbol, " not defined, printing plaintext"
                    output.append(symbol)
        else:
            output.append(char[1])

        if len(string)-1 <= char[0]:
            text_left = False

    output.append('"')
    print "Here's your prompt command!\nJust put it into your ~/.*rc file!\n\n", ''.join(output)


