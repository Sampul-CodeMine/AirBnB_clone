#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
import cmd
import datetime as dt
import re
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


"""
This is a Python class that will act as an interface for the first phase
of the AirBnB Clone project.
"""

all_classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

attributes = {
    "BaseModel":{
        "id": str,
        "created_at": dt.datetime,
        "updated_at": dt.datetime
    }, "User":{
        "email": str,
        "password": str,
        "first_name": str,
        "last_name": str
    }, "State": {
        "name": str
    }, "City": {
        "state_id": str,
        "name": str
    }, "Amenity": {
        "name": str
    }, "Place": {
        "city_id": str,
        "user_id": str,
        "name": str,
        "description": str,
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
        "amenity_ids": list
    }, "Review": {
        "place_id": str,
        "user_id": str,
        "text": str
    }
}

class HBNBCommand(cmd.Cmd):
    """
    This is a class modelling the inteface (CLI) for AirBnB Clone project.
    """

    """Specify the prompt for the CLI"""
    prompt = "(hbnb) "

    def do_quit(self, arg: any) -> None:
        """Issues a quit command to the CLI by returning True"""
        return True

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
        """Method that does nothing when the ENTER key is pressed without a
        command."""
        pass

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
        print("Models available includes:\n")
        print("\tAmenity\n\tBaseModel\n\tCity\n\tPlace\n\tReview\n\t", end="")
        print("State\n\tUser\n")
        print("Usage:\n(hbnb) create User\n")

    def do_show(self, args=None) -> None:
        """Public instance method that displays the string instance of a
        class, based on the instance id and classname specified"""
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
        regx = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        is_match = re.search(regx, args)
        cls_name_match = is_match.group(1)
        uid_match = is_match.group(2)
        attr_match = is_match.group(3)
        val_match = is_match.group(4)
        if is_match:
            if cls_name_match in all_classes.keys():
                if uid_match:
                    id = "{}.{}".format(cls_name_match, uid_match)
                    if id in storage.all():
                        if attr_match:
                            if val_match:
                                datatype = None
                                if not re.search('^".*"$', val_match):
                                    if '.' in val_match:
                                        datatype = float
                                    else:
                                        datatype = int
                                else:
                                    val_match = val_match.replace('"', '')
                                attrs = attributes[cls_name_match]
                                if attr_match in attrs:
                                    val_match = attrs[attr_match](val_match)
                                elif datatype:
                                    try:
                                        val_match = datatype(val_match)
                                    except ValueError:
                                        ...
                                setattr(storage.all()[id], attr_match, val_match)
                                storage.all()[id].save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_update(self) -> None:
        """Updates the help for update"""
        print("")
        print("The `update` command update a specified instance of a", end="")
        print(" using the class name and the ID of the instance, and", end="")
        print(" and the specifying the attribute to update or adding", end="")
        print(" a new attribute plus the value.\n")
        print("Usage:\n(hbnb) update User 1234-5678 email 'test@oop.com'\n")


if __name__ == "__main__":
    commnd = HBNBCommand()
    commnd.cmdloop()
