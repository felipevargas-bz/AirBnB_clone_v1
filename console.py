#!/usr/bin/python3
"""
Cobsole 
"""
import cmd
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand
    for command interpreter"""
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the cmd"""
        return True

    def do_quit(self, line):
        """quit command to exit the cmd"""
        return True

    def emptyline(self):
        """ Prints new line when press enter """
        pass

    def default(self, line):
        """ Method called when an empty line is entered in
        response to the prompt. We have .all() .count() .show()
        .destroy() included here """
        cmd_methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.__count,
            "update": self.do_update
            }
        line = line.split(".")
        class_name = line[0]
        line_finder = line[1].split("(")
        method = line_finder[0]
        attr_finder = line_finder[1].replace(')', "").replace('"', "")
        id_finder = attr_finder.split(", ")
        class_id = id_finder[0]

        if class_name in self.classes and method in cmd_methods:
            if method == "all" or method == "count":
                cmd_methods[method](class_name)
            elif method == "update":
                attr_finder = attr_finder.split(", ")
                attr_name = attr_finder[1]
                attr_value = attr_finder[2]
                cmd_methods[method]("{} {} {} {}".format(class_name,
                                                         class_id,
                                                         attr_name,
                                                         attr_value))
            else:
                cmd_methods[method]("{} {}".format(class_name, class_id))
        else:
            cmd.Cmd.default(self, line)

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id """
        line_list = line.split()

        if line == "":
            print("** class name missing **")
        elif line_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[line_list[0]]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id"""
        line_list = line.split()
        if len(line_list) < 2:
            print("** instance id missing **")
            return 0

        instance_id = line_list[0] + "." + line_list[1]
        existing_instances = storage.all()

        if instance_id not in existing_instances.keys():
            print("** no instance found **")
            return 0

        if self.__class_id_checker(line, len(line)) != 1:
            instance_id = line_list[0] + "." + line_list[1]
            existing_instances = storage.all()

            if instance_id in existing_instances.keys():
                print(existing_instances[instance_id])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        line_list = line.split()

        if self.__class_id_checker(line_list, len(line_list)) != 1:

            instance_id = line_list[0] + "." + line_list[1]
            existing_instances = storage.all()

            if instance_id in existing_instances.keys():
                del existing_instances[instance_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name """
        line_list = line.split()
        if line == "" or line_list[0] in self.classes:
            instances_id = storage.all()
            list_classes = []

            for key, value in instances_id.items():
                if line in key:
                    list_classes.append(value.__str__())

            print(list_classes)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""
        line_list = line.split()

        if self.__class_id_checker(line_list, len(line_list)) == 1:
            pass
        elif len(line_list) == 2:
            print("** attribute name missing **")
        elif len(line_list) == 3:
            print("** value missing **")
        else:
            inst_id = line_list[0] + "." + line_list[1]
            dict_instances = storage.all()

            if inst_id in dict_instances.keys():
                if line_list[3]:
                    line_list[3] = line_list[3].replace('"', "")
                try:
                    line_list[3] = int(line_list[3])
                except ValueError:
                    try:
                        line_list[3] = float(line_list[3])
                    except ValueError:
                        line_list[3] = line_list[3]
                dict_instances[inst_id].__dict__[line_list[2]] = line_list[3]
                dict_instances[inst_id].save()
            else:
                print("** no instance found **")

    def __class_id_checker(self, line_list, len_line):
        """ Checks if class name and id exist """
        if len_line == 0:
            print("** class name missing **")
            return 1
        elif line_list[0] not in self.classes:
            print("** class doesn't exist **")
            return 1
        elif len_line == 1:
            print("** instance id missing **")
            return 1

    def __count(self, line):
        """Retrieve the number of instances of a class """
        line_list = line.split()
        if line_list[0] in self.classes:
            instances_id = storage.all()
            number_instances = 0

            for key, value in instances_id.items():
                if line in key:
                    number_instances += 1

            print(number_instances)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
