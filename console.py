#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel
from models.__init__ import storage



class HBNBCommand(cmd.Cmd):
    """
    console cmd class
    """
    lists_of_class = {
        "BaseModel": BaseModel}

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
        split_line = line.split(" ")
        if (len(line) == 0):
            print("** class name missing **")
            return (False)
        elif split_line[0] in self.lists_of_class:
            obj = self.lists_of_class[split_line[0]]()
        else:
            print("** class doesn't exist **")
            return (False)
        print(obj.id)
        obj.save()

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        split_line = line.split(" ")
        if self.class_id_check(split_line, len(split_line)) != 1:

            instancia_id = split_line[0] + "." + split_line[1]
            instancia_existe = models.storage.all()

            if instancia_id in instancia_existe.keys():
                instancia_existe[instancia_id].to_dict()
                # print(instancia_existe[instancia_id])
            else:
                print ("** no instance found **")

    def do_destroy(self, line):
        split_line = line.split(" ")

        if self.class_id_check(split_line, len(split_line)) != 1:

            instancia_id = split_line[0] + "." + split_line[1]
            instancia_existe = models.storage.all()

            if instancia_id in instancia_existe.keys():
                del instancia_existe[instancia_id]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name """

        split_line = line.split()

        if split_line[0]  in self.lists_of_class:
            pass
            

    

    def class_id_check(self, split_line, len_line):
        """
            check if class name and id exist 
        """
        if len_line == 0:
            print("** class name missing **")
            return 1
        elif split_line[0] not in self.lists_of_class:
            print("** class doesn't exist **")
            return 1
        elif len(split_line[1]) == 0:
            print("** instance id missing **")
            return 1

if __name__ == '__main__':
    HBNBCommand().cmdloop()