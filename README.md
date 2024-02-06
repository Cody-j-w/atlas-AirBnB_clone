# HBNB Console

## Description and installation

A compact CRUD console for managing users, locations, and reviews
on an AirBnB-like platform

To install the console, simply clone it into your preferred directory
    `git clone https://github.com/Cody-j-w/atlas-AirBnB_clone`
and run it using a Python interpreter
    `python console.py`

## Console usage

Once you have the console installed and running, you have access to a number
of commands:
`create <class name>` creates a new instance of the specified class

`show <class name> <instance id>` shows the details of the specified instance

`all <class name (optional)>` shows all instances of the specified class
or all instances of any class, if no class name is provided

`destroy <class name> <instance id>` removes the specified instance

`update <class name> <instance id> <attribute> <value>` updates the specified
attribute of the specified instance with the value provided

`quit` quits the console. ctrl+D will also work.

These commands can also be viewed in the console by running `help <cmd name>`
and `help` with no arguments will provide a list of all usable commands
