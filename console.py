#!/usr/bin/python3

"""Module console.py
The program starts here. Run this script to interact with the program"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.engine.file_storage import FileStorage

"""this will be responsible for consule part 

    Returns:
        nth: nth
    """


class HBNBCommand(cmd.Cmd):
    inrto = "well come to my shell"
    prompt = '(hbnb)'

    def checker(self, arg, number):
        """this will check the validity of argument 

        Args:
            arg (line from concule): string 
            number (which checker number): which type of check to check 

        Returns:
            _type_: _description_
        """
        classes = ["BaseModel", "User", "State", "Place", "City", "Amenity"]
        msg = ['** class name missing **',
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **", ]

        if not arg:
            print(msg[0])
            return 1
        args = arg.split(" ")
        if number == 1:
            if args[0] not in classes:
                print(msg[1])
                return 1
        if number == 2:
            if args[0] not in classes:
                print(msg[1])
                return 1
            if len(args) < 2:
                print(msg[2])
                return 1
        if number == 3:
            if args[0] not in classes:
                print(msg[1])
                return 1
        if number == 4:
            if args[0] not in classes:
                print(msg[1])
                return 1
            if len(args) < 2:
                print(msg[2])
                return 1
            x = FileStorage.all(self)
            clsandid = args[0] + "." + args[1]
            if clsandid not in x.keys():
                print("** no instance found **")
                return 1
            if len(args) < 3:
                print("** attribute name missing **")
                return 1
            if len(args) < 4:
                print("** value missing **")
                return 1

    def do_quit(self, arg):
        """Exit the HBNB console:  quit"""
        return True

    def do_EOF(self, arg):
        """Exit the HBNB console:  EOF"""
        return True

    def do_create(self, line):
        """this will creat instance of given things

        Args:
            line (this is argument of the command ): nothing 
        """
        if self.checker(line, 1) == 1:
            return
        arg = line.split(" ")
        obj = eval(arg[0])()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """this will show the single item 

        Args:
            line (string of the base and id ): nothing 
        """
        err = self.checker(line, 2)
        if err == 1 or err == 2:
            return
        x = FileStorage.all(self)
        args = line.split()
        clsandid = args[0] + "." + args[1]
        if clsandid in x.keys():
            print(x[clsandid].__dict__)
        else:
            print("** no instance found **")
        del x

    def do_all(self, line):
        """this will show all objects or speific objects 

        Args:
            line (string ): classes
        """
        y = []
        if not line:
            x = FileStorage.all(self)
            for obj in x.values():
                y.append(obj.to_dict())
            print(y)
            return
        err = self.checker(line, 1)
        if err == 1:
            return
        x = FileStorage.all(self)
        args = line.split()
        for obj in x.values():
            if args[0] == obj.__class__.__name__:
                y.append(obj.to_dict())
        print(y)
        del y
        return

    def do_update(self, line):
        """this will updatte instance 

        Args:
            line (str): informations to update
        """
        err = self.checker(line, 4)
        if err == 1:
            return
        x = FileStorage.all(self)
        args = line.split()
        clsandid = args[0] + "." + args[1]
        if clsandid in x.keys():
            x[clsandid].__dict__[args[2]] = eval(args[3])

    def do_destroy(self, line):
        """this will distroy instance 

        Args:
            line (str): model and id to distroy
        """
        err = self.checker(line, 2)
        if err == 1 or err == 2:
            return
        x = FileStorage.all(self)
        args = line.split()
        clsandid = args[0] + "." + args[1]
        if clsandid in x.keys():
            del x[clsandid]
        else:
            print("** no instance found **")
        del x


if __name__ == '__main__':
    HBNBCommand().cmdloop()
