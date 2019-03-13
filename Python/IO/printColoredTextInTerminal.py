from sys import platform # to check os
'''
sys.platform returns:
   OS                       RETURN
- Linux (2.x and 3.x)	  'linux2'
- Windows	              'win32'
- Windows/Cygwin	      'cygwin'
- Mac OS X	              'darwin'

'''

class ColorPrinter:
    '''
    This does only work on unix systems
    Class for coloring text for terminal print
    '''
    def __init__(self):
        self.reset_mac  = "\033[0m"  # reset (turn of color)
        self.reset_linux  = "\u001b[0m"  # reset (turn of color)
        self.black  = 30
        self.red    = 31
        self.green  = 32
        self.yellow = 33
        self.blue   = 34
        self.magenta = 35
        self.cyan   = 36
        self.defualt_os = "mac"



    def get_color(self, color, bright=True):
        clr = None

        if color == 'black':
            clr = self.black

        elif color == 'red':
            clr = self.red

        elif color == 'green':
            clr = self.green

        elif color == 'yellow':
            clr = self.yellow

        elif color == 'blue':
            clr = self.blue

        elif color == 'magenta':
            clr = self.magenta

        elif color == 'cyan':
            clr = self.cyan

        #################

        if not clr is None:
            if bright:
                clr += 60
            return "\033[{}m".format(str(clr))

        else:
            return ""

    def _getOS(self):
        '''
        Determins the operating system used to run code,
        and returns the terminal exit code to reset terminal features.
        :return: escape code for operating system that resets terminal print config.
        '''
        if platform.startswith("linux"): return self.reset_linux
        elif platform.startswith('darwin'): return self.reset_mac
        elif platform.startswith("win") or platform.startswith("cygwin"):
            return NotImplemented("Windows operating system does not support \
                color print nativly")
        elif platform.startswith("freebsd"): raise NotImplemented("Freebsd os \
                support is not implemented yet")
        else: raise NotImplemented("Could not find os type")


    def paintString(self, text, color=None, bright=True):
        # find reset code for os:
        reset_code = self._getOS()
        return self.get_color(color, bright) + text + reset_code

printer = ColorPrinter()
res = printer.paintString("Dette er en farget text", color="magenta")
print(res)
res = printer.paintString("Dette er en annen farget text", color="cyan", bright=False)
print(res)
