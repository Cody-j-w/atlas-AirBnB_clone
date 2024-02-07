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

![create command example](https://github.com/Cody-j-w/atlas-AirBnB_clone/blob/main/example_images/User_create.PNG)

`show <class name> <instance id>` shows the details of the specified instance

`all <class name (optional)>` shows all instances of the specified class
or all instances of any class, if no class name is provided

![all command example, with User specification provided](https://github.com/Cody-j-w/atlas-AirBnB_clone/blob/main/example_images/all_example.PNG)

`destroy <class name> <instance id>` removes the specified instance
![destroy command example](https://github.com/Cody-j-w/atlas-AirBnB_clone/blob/main/example_images/example_destroy.PNG)

`update <class name> <instance id> <attribute> <value>` updates the specified
attribute of the specified instance with the value provided
![update command example](https://github.com/Cody-j-w/atlas-AirBnB_clone/blob/main/example_images/update_example.PNG)

`quit` quits the console. ctrl+D will also work.

These commands can also be viewed in the console by running `help <cmd name>`
and `help` with no arguments will provide a list of all usable commands

![console behavior flowchart](https://github.com/Cody-j-w/atlas-AirBnB_clone/blob/main/console_diagram.png)
