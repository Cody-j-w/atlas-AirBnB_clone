#!/usr/bin/python3

"""
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to the HBNB console. Type help or ? to list commands.\n"
    prompt = "(hbnb)"

    def default(self, arg):
        """
        fallback command handler
        """
        if arg == "EOF":
            print('\r')
            return True
        pass

    def do_create(self, args):
        """
        command input: create <class name>
        Creates a new instance of the specified class
        """
        pass

    def do_quit(self, arg):
        """
        command input: quit
        terminates the current session and closes the HBNB console
        """
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()