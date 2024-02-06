#!/usr/bin/python3

"""
Module containing the console shell for HBNB project
"""
import cmd
import models
import sys
classes = {'BaseModel': models.base_model.BaseModel, 'User': models.user.User,
            'State': models.state.State, 'city': models.city.City,
            'Amenity': models.amenity.Amenity, 'Place': models.place.Place,
            'Review': models.review.Review}
storage = models.storage



class HBNBCommand(cmd.Cmd):
    """
    HBNB console

    Attributes:
        intro: string - introductory message displayed when console starts
        prompt: string - string prompting new input
    """
    intro = "Welcome to HBNB admin console, enter help or ? to view commands"
    prompt = "(hbnb)" if sys.__stdin__.isatty() else ""

    def preloop(self):
        """
        preloop handler override
        """
        if not sys.__stdin__.isatty():
            print("(hbnb)")

    # def postcmd(self, stop, line):
    #     """
    #     post-command override
    #     """
    #     if not sys.__stdin__.isatty():
    #         print("(hbnb)", end = '')

    def default(self, arg):
        """
        fallback command handler
        """
        args = arg.split(" ")
        print(args)
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
        if args == "" or args == " " or args is None:
            print("** class name missing **")
        else:
            args_list = args.split(" ")
            if args_list[0] not in classes:
                print("** class doesn't exist **")
            else:
                new_inst = classes[args_list[0]]()
                storage.save()
                print(new_inst.id)

    def do_show(self, args):
        """
        command input: show <class name> <instance id>
        Shows the information pertaining to the specified instance
        """
        if args == "" or args == " " or args is None:
            print("** class name missing **")
        else:
            args_list = args.split(" ")
            if args_list[0] not in classes:
                print("** class doesn't exist **")
            if len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_all(self, args):
        """
        command input: all <class name (optional)>
        Shows all instances of the specified class, or all instances of any
        class if the class name argument is not provided
        """
        flag = "all"
        if args != "" and args != " " and args is not None:
            flag = args.split(" ")[0]
            if flag not in classes:
                print("** class doesn't exist **")
            else:
                for key in storage.all():
                    if flag != "all":
                        if key.split(".")[0] != flag:
                            continue
                    print(storage.all()[key].to_dict())
        else:
            for key in storage.all():
                print(storage.all()[key].to_dict())

    def do_destroy(self, args):
        """
        command input: destroy <class name> <instance id>
        Delete the specified instance
        """
        if args == "" or args == " " or args is None:
            print("** class name missing **")
        else:
            args_list = args.split(" ")
            if args_list[0] not in classes:
                print("** class doesn't exist **")
            if len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_update(self, args):
        """
        command input: update <class name> <inst id> <attr name> <attr value>
        Update the value of the specified attribute with the provided value
        """
        if args == "" or args == " " or args is None:
            print("** class name missing **")
        else:
            args_list = args.split(" ")
            if args_list[0] not in classes:
                print("** class doesn't exist **")
            if len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all()[key]
                    if len(args_list) < 3:
                        print("** attribute name missing **")
                    else:
                        attr_name = args_list[2]
                        if len(args_list) < 4:
                            print("** value missing **")
                        else:
                            attr_val = args_list[3]
                            if hasattr(storage.all()[key], attr_name):
                                attrtype = type(getattr(obj, attr_name))
                                value = attrtype(attr_val)
                                setattr(obj, attr_name, value)
                                obj.save()
                            else:
                                print("** attribute not found")


    def do_quit(self, arg):
        """
        command input: quit
        terminates the current session and closes the HBNB console
        """
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()