#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "Review", "Place",
               "State", "City", "Amenity"}

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exit the program
        """
        print("")
        return True

    def emptyline(self):
        """shouldn’t execute anything
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_one = eval(line)()
            new_one.save()
            print(new_one.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        new_list = line.split()
        if not line:
            print("** class name missing **")
        elif new_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(new_list) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = new_list[0] + '.' + new_list[1]
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        new_list = line.split()
        if not line:
            print("** class name missing **")
        elif new_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(new_list) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = new_list[0] + '.' + new_list[1]
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        new_list = line.split()
        obj = storage.all()
        for key in obj.keys():
            if new_list:
                if new_list[0] not in self.classes:
                    print("** class doesn't exist **")
                    break
                if obj[key].__class__.__name__ == new_list[0]:
                    print(obj[key])
            else:
                print(obj[key])

    def do_update(self, line):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        new_list = line.split()
        if not line:
            print("** class name missing **")
        elif new_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(new_list) < 2:
            print("** instance id missing **")
        elif len(new_list) < 3:
            obj = storage.all()
            key = new_list[0] + "." + new_list[1]
            if key not in obj:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(new_list) < 4:
            print("** value missing **")
        else:
            obj = storage.all()
            key = new_list[0] + "." + new_list[1]
            if key in obj:
                setattr(obj[key], obj[2], new_list[3])
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
