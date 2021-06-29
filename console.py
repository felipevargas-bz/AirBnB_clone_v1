#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    console cmd class
    """

    prompt = "(hbnb)"

    def do_quit(self, line):
         """
         Quit command
         """
         print("La buena mi papa")
         return(True)
    def do_EOF(self, line):
        """
        ....
        """
        print("")
        return (True)

    def do_help(self, line):
        print("""
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb)""")

if __name__ == '__main__':
    HBNBCommand().cmdloop()