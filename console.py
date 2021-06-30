#!/usr/bin/python3
"""
rsfagdkvb lkhnvbilo cualquier mierda
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review




class HBNBCommand(cmd.Cmd):
    """
    console cmd class
    """

    lists_of_class = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    prompt = "(hbnb) "

    def emptyline(self):
        """this is a empty line"""
        return 0

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits console"""
        return True

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
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        split_line = line.split()
        if self.class_id_check(split_line, len(split_line)) != 1:

            instancia_id = split_line[0] + "." + split_line[1]
            instancia_existe = models.storage.all()

            if instancia_id in instancia_existe.keys():
                instancia_existe[instancia_id].to_dict()
                # print(instancia_existe[instancia_id])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        split_line = line.split()

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

        if len(line) == 0:
            return 0

        split_line = line.split(" ")
        if len(split_line[0]) == 0:
            return 0

        all_objects = models.storage.all()

        if split_line[0] in self.lists_of_class:
            for key in all_objects:
                print(all_objects[key])
        else:
            print("** class doesn't exist **")

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
        elif len_line == 1:
            print("** instance id missing **")
            return 1

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""
        split_line = line.split()

        if self.class_id_check(split_line, len(split_line)) == 1:
            return 0
        elif len(split_line) == 2:
            print("** attribute name missing **")
            return 0
        elif len(split_line) == 3:
            print("** value missing **")
            return 0
        else:
            inst_id = split_line[0] + "." + split_line[1]
            dict_instances = models.storage.all()

        if inst_id in dict_instances.keys():
            if split_line[3]:
                split_line[3] = split_line[3].replace('"', "")
                try:
                    split_line[3] = int(split_line[3])
                except ValueError:
                    try:
                        split_line[3] = float(split_line[3])
                    except ValueError:
                        split_line[3] = split_line[3]
                dict_instances[inst_id].__dict__[split_line[2]] = split_line[3]
                dict_instances[inst_id].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
