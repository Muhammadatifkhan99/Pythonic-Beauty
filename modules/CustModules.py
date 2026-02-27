

# to install custom module we need to install them using pip-> which stands for pip install package which is a recursive definition in its own.
# python3 -m pip install NAME_PACKAGE

import termcolor
import pyfiglet

help(termcolor)
ttAscii = input("Enter you desired text to convert to ASCII: ")
col = input("Enter the color: ")
text = termcolor.colored(ttAscii,color=col)
text1 = pyfiglet.figlet_format(text)
print(text1)