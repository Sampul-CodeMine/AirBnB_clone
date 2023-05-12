#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
import cmd
import datetime as dt
from models.base_model import BaseModel
from models import storage


"""
This is a Python class that will act as an interface for the first phase
of the AirBnB Clone project.
"""

all_classes = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):
    """
    This is a class modelling the inteface (CLI) for AirBnB Clone project.
    """

    """Specify the prompt for the CLI"""
    prompt = "(hbnb) "

    def do_quit(self, arg: any) -> None:
        """Issues a quit command to the CLI"""
        exit(1)

    def help_quit(self) -> None:
        """Updates the help for quit"""
        print("")
        print("The `quit` command issues a command to quit the CLI.\n")
        print("Usage:\n(hbnb) quit\n")

    def do_EOF(self, arg: any) -> True:
        """Returns True and breaks the cmdloop"""
        print("")
        return True

    def help_EOF(self) -> None:
        """Updates the help for EOF"""
        print("")
        print("The `EOF` command returns True to break the cmdloop", end=" ")
        print("and exits the CLI.\n")
        print("Usage:\n(hbnb) EOF\nor\n(hbnb) <CTRL + C>")
        print("or\n(hbnb) <CTRL + Z>\n")

    def emptyline(self) -> None:
        ...

    def do_create(self, args) -> None:
        """Public instance method that creates new instance of a class, save
        it to a JSON file and print the `id` of the instance"""
        if len(args) == 0:
            print("** class name missing **")
            return
        arg_num = args.split(" ")
        if arg_num[0] in all_classes.keys():
            obj = eval(arg_num[0] + "()")
            id = getattr(obj, 'id')
            print(id)
            storage.save()
            return
        else:
            print("** class doesn't exist **")
            return

    def help_create(self) -> None:
        """Updates the help for create"""
        print("")
        print("The `create` command creates an instance of a class, ", end="")
        print("saves it to the storage and prints out the ID of the", end=" ")
        print("instance created.\n")
        print("Usage:\n(hbnb) create User\n")

    def do_show(self, args=None) -> None:
        """Public instance method that displays the string instance of a class,
        based on the instance id and classname specified"""
        if len(args) == 0:
            print("** class name missing **")
            return
        arg_num = args.split(" ")
        if arg_num[0] in all_classes.keys():
            if len(arg_num) >= 2:
                id = "{}.{}".format(arg_num[0], str(arg_num[1]))
                str_obj = storage.all()
                if id in str_obj.keys():
                    obj = str_obj[id]
                    print(obj)
                    return
                else:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")
            return

    def help_show(self) -> None:
        """Updates the help for show"""
        print("")
        print("The `show` command displays the details and string", end=" ")
        print("representation of an instance based on class name", end=" ")
        print("and instance id provided.\n")
        print("Usage:\n(hbnb) show User 51a155c1-214a-4923-8d53-523900fed722")
        print("")

    def do_destroy(self, args) -> None:
        """Public instance method that deletes the instance of a class,
        based on the instance id and classname specified"""
        if len(args) == 0:
            print("** class name missing **")
            return
        arg_num = args.split(" ")
        if arg_num[0] in all_classes.keys():
            if len(arg_num) == 2:
                id = "{}.{}".format(arg_num[0], str(arg_num[1]))
                str_obj = storage.all()
                if id in str_obj.keys():
                    del (str_obj[id])
                    storage.save()
                    return
                else:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")
            return

    def help_destroy(self) -> None:
        """Updates the help for destroy"""
        print("")
        print("The `destroy` command deletes the details of an ", end="")
        print("instance based on class name and instance id provided.\n")
        print("Usage:\n(hbnb) destroy User 51a155c1-214a-4923-8d53-52fed22\n")

    def do_all(self, args) -> None:
        """Public instance method that displays the string instance of all
        the instances of a class based on the classname specified or no
        classname specified"""
        list_all = []
        str_obj = storage.all()
        arg_num = args.split(" ")
        if len(args) == 0:
            for obj in str_obj.values():
                list_all.append(str(obj))
        elif arg_num[0] in all_classes.keys():
            for id in str_obj.keys():
                if id.split(".")[0] == arg_num[0]:
                    list_all.append(str(str_obj[id]))
        else:
            print("** class doesn't exist **")
            return
        print(list_all)

    def help_all(self) -> None:
        """Updates the help for all"""
        print("")
        print("The `all` command displays the string representation", end="")
        print(" of all class instances present in the storage.\n")
        print("Usage:\n(hbnb) all User\n")

    def do_update(self, args) -> None:
        """Public instance method that updates a specified instance of a class
        using the id and either adding more attributes or updating an
        attribute"""
        if len(args) == 0:
            print("** class name missing **")
            return
        str_obj = storage.all()
        arg_num = args.split(" ")
        if arg_num[0] in all_classes.keys():
            if len(arg_num) < 2:
                print("** no instance found **")
                return
            elif arg_num[1] in [id.split(".")[1] for id in str_obj.keys()]:
                id = "{}.{}".format(arg_num[0], arg_num[1])
                obj = str_obj[id]
                if len(arg_num) < 3:
                    print("** attribute name missing **")
                    return
                else:
                    if len(arg_num) < 4:
                        print("** value missing **")
                        return
                    else:
                        try:
                            setattr(obj, arg_num[2],
                                    eval(arg_num[3].strip('"')))
                        except Exception:
                            setattr(obj, arg_num[2], arg_num[3].strip('"'))
                        setattr(obj, 'updated_at', dt.datetime.now())
                        storage.save()
            else:
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")
            return

    def help_update(self) -> None:
        """Updates the help for update"""
        print("")
        print("The `update` command update a specified instance of a", end="")
        print(" using the class name and the ID of the instance, and", end="")
        print(" and the specifying the attribute to update or adding", end="")
        print(" a new attribute plus the value.\n")
        print("Usage:\n(hbnb) update User 1234-5678 email 'test@oop.com'\n")


if __name__ == "__main__":
    try:
        commnd = HBNBCommand()
        commnd.cmdloop()
    except (KeyboardInterrupt, EOFError):
        exit(1)
