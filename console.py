#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.__init__ import storage

lists_of_class = {"BaseModel": BaseModel}

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
        exit the program
        """
        print("")
        return (True)

    def do_create(self, line):
        split_line = line.split()
        if (len(line) == 0):
            print("** class name missing **")
            return (False)
        elif split_line[0] in lists_of_class:
            obj = lists_of_class[split_line[0]]()
        else:
            print("** class doesn't exist **")
            return (False)
        print(obj.id)
        obj.save()

    def do_show(self, line):
        """
        class_id_line = f'{split_line[0]}.{split_line[1]}'
        if (len(line) == 0):
            print("** class name missing **")
            return (False)
        elif (len(split_line[1]) == 0):
            print("** instance id missing **")
        elif class_id_line not in storage.__objects:
            print("** instance id missing **")
        elif split_line[0] not in lists_of_class:
            print("** class doesn't exist **")
            return (False)"""

        split_line = line.split()
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()