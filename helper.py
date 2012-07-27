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

from shell import *

def index_all(text, sub, start, finish):
    l = []
    text = text[start:finish]
    i = text.find(sub)
    while i > -1:
        l.append(i)
        i = text.find(sub, i+1)
    return l


def make_prompt(string, shell):
    
    if shell == 'bash':
        shell = bash.Bash() 
    elif shell == 'zsh':
        shell = zsh.Zsh()
    itr = iter(string)
    output = [shell.prompt_header]

    # Why does the python iterator not have a thing to check whether or not we have more elements...?
    # Anyway, this littler parser I wrote is just a simple state machine.
    try:
        while True:
            char = itr.next()
            if char == "(":
                symbol = []
                symbol.append(char)
                try:
                    char = itr.next()
                    if char == "?":
                        symbol.append(char)
                        while char != ')':
                            char = itr.next()
                            symbol.append(char)
                        symbol = ''.join(symbol)
                        output.append(shell.escapes[symbol])

                    else:
                        #discard invalid symbole
                        output.append(symbol)
                except:
                    output.append(symbol)
            else:
                #append non-symbol characters
                output.append(char)
    except:
      pass

    output.append(' \'')

    #TODO: Show this graphically
    print "Here's your prompt command!\nJust put it into your ~/.*rc file!\n\n", ''.join(output)


