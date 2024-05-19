#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
         'User': User,
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a new line
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[arg]()
        obj.save()
        print(obj.id)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances
            based or not on the class name.
        """
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        objs = models.storage.all()
        obj_list = []
        for key, obj in objs.items():
            if not arg or key.startswith(arg):
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
            by adding or updating attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = models.storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name, attr_value = args[2], args[3].strip('"')
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            attr_value = attr_type(attr_value)
            setattr(obj, attr_name, attr_value)
            obj.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
            based on class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = models.storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        print(obj)


if __name__ == '__main__':
    models.storage.reload()
    HBNBCommand().cmdloop()
