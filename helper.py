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


def make_prompt(string, shell):
    color_escapes = {
                ("(?bla)"  , "(?norm)") : r'\e[0;30m',
                ("(?red)"  , "(?norm)") : r'\e[0;31m',
                ("(?grn)"  , "(?norm)") : r'\e[0;32m',
                ("(?ylw)"  , "(?norm)") : r'\e[0;33m',
                ("(?blu)"  , "(?norm)") : r'\e[0;34m',
                ("(?mgta)" , "(?norm)") : r'\e[0;35m',
                ("(?cyn)"  , "(?norm)") : r'\e[0;36m',
                ("(?wht)"  , "(?norm)") : r'\e[0;37m',

                ("(?bla)"  , "(?bold)") : r'\e[1;30m',
                ("(?red)"  , "(?bold)") : r'\e[1;31m',
                ("(?grn)"  , "(?bold)") : r'\e[1;32m',
                ("(?ylw)"  , "(?bold)") : r'\e[1;33m',
                ("(?blu)"  , "(?bold)") : r'\e[1;34m',
                ("(?mgta)" , "(?bold)") : r'\e[1;35m',
                ("(?cyn)"  , "(?bold)") : r'\e[1;36m',
                ("(?wht)"  , "(?bold)") : r'\e[1;37m' }

    
    if shell == 'bash':
        prompt_header = 'PS1=\''
        special_escapes = {
                '(?u)' : r'\u', #Username
                '(?h)' : r'\h', #Hostname
                '(?w)' : r'\w', #pwd
                '(?d)' : r'\d', #date
                '(?H)' : r'\H', #full hostname
                '(?j)' : r'\j', #number of jobs managed by shell
                '(?s)' : r'\s', #the name of the shell.
                '(?t)' : r'\t', #current time (24h)
                '(?@)' : r'\@', # time 12h
                '(?v)' : r'\v', # bash version
                '(?V)' : r'\V', # release of bash
                '(?W)' : r'\W', # basename of pwd #POSSIBLY REMOVE
                '(?!)' : r'\!', # history number
               r'(?#)' : r'\#',# command number
                '(?$)' : r'\$', # magic $
                '(?reset)': r'\e[0m'}

    elif shell == 'zsh':
        prompt_header = 'PS1=$\''
        special_escapes = {
                '(?u)' : r'%n',
                '(?h)' : r'%m',
                '(?w)' : r'%~',
                '(?d)' : r'%T',
                '(?H)' : r'%M',
                '(?j)' : r'',
                '(?s)' : r'',
                '(?t)' : r'',
                '(?@)' : r'',
                '(?v)' : r'',
                '(?V)' : r'',
                '(?W)' : r'%d',
                '(?!)' : r'%!',
               r'(?#)' : r'', #Needs research
                '(?$)' : r'%#',
                '(?reset)': r'\e[0m'}

    colors = {'(?bla)', '(?red)', '(?grn)', '(?ylw)', '(?blu)', '(?mgta)', '(?cyn)', '(?wht)'}
    formats = {'(?bold)', '(?norm)'}
    specials = {'(?u)', '(?h)', '(?w)', '(?d)', '(?H)'}
    current_color = '(?bla)'
    current_style = '(?norm)'
    text_left = True
    itr = enumerate(list(string))
    output = [prompt_header]
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

    output.append(' \'')
    print "Here's your prompt command!\nJust put it into your ~/.*rc file!\n\n", ''.join(output)


