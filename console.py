#!/usr/bin/python3

"""
Module containing the console shell for HBNB project
"""
import cmd
import models
import sys


class HBNBCommand(cmd.Cmd):
    """
    HBNB console

    Attributes:
        intro: string - introductory message displayed when console starts
        prompt: string - string prompting new input
    """
    intro = "Welcome to the HBNB console. Type help or ? to list commands.\n"
    prompt = "(hbnb)" if sys.__stdin__.isatty() else ""

    def preloop(self):
        """
        preloop handler override
        """
        if not sys.__stdin__.isatty():
            print("(hbnb)")


    def default(self, arg):
        """
        fallback command handler
        """
        if arg == "EOF":
            print('\r')
            return True
        pass

    def emptyline(self):
        """
        handle empty lines
        """
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