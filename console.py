#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
