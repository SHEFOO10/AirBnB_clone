#!/usr/bin/python3
""" Handle console class with it's commands """
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand to handle commmands """
    prompt = '(hbnb) '

    def emptyline(self):
        """ prevent emtpy line function from make it's default behaviour """
        pass

    def do_EOF(self, line):
        """ Handle Ctrl + D or (EOF) """
        return True

    def do_quit(self, line):
        """ to exit the program """
        return True

    def do_create(self, line):
        """ create new object from classname inside the line """
        if line == '':
            print ('** class name missing **')
        else:
            new_instance = self.return_class(line.split()[0].strip('"'))
            new_instance.save()

    def do_show(self, line):
        """ Show the object """
        from models import storage
        from models.base_model import BaseModel
        if line == '':
            print("** class name missing **")
        arguments = line.split()
        instance = self.return_class(arguments[0].strip('"'))

        if len(arguments) == 1:
                (print("** instance id missing **")
                    if isinstance(instance, BaseModel)
                    else print("** class doesn't exist **"))
        elif len(arguments) >= 2:
            try:
                print(storage.all()[arguments[0]+'.'+arguments[1]])
            except KeyError:
                print("** no instance found **")

    def return_class(self, classname):
        """ check if class exists and return it """
        from models.base_model import BaseModel
        classes = {
        'BaseModel': BaseModel
        }
        try:
            return classes[classname]()
        except KeyError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
