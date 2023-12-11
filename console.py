#!/usr/bin/python3
""" Handle console class with it's commands """
import cmd
from models import base_model, user, city, place, review, state
from models import amenity, storage


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand to handle commmands """
    prompt = '(hbnb) '
    classes = {
        'BaseModel': base_model.BaseModel,
        'User': user.User,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'Amenity': amenity.Amenity
    }

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
            print('** class name missing **')
        else:
            new_instance = self.return_class(line.split()[0].strip('"'))
            if new_instance is not None:
                new_instance = new_instance()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """ Show the object """
        key = self.validate_line(line)
        if key is not None:
            print(storage.all()[key])

    def do_destroy(self, line):
        """ destory the object with it's id """
        key = self.validate_line(line)
        if key is not None:
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """ return all object as list of strings """
        if line.strip() == '':
            all_models = [obj.__str__() for obj in storage.all().values()]
            if all_models != []:
                print(all_models)
        else:
            if self.return_class(line.strip()) is not None:
                all_specific_models = [
                    obj.__str__()
                    for obj in storage.all().values()
                    if obj.__class__.__name__ == line.strip()
                    ]
                if all_specific_models != []:
                    print(all_specific_models)

    def return_class(self, classname):
        """ check if class exists and return it """
        try:
            return HBNBCommand.classes[classname]
        except KeyError:
            print("** class doesn't exist **")

    def validate_line(self, line):
        """ validate arguments """
        from models.base_model import BaseModel
        if line.strip() == '':
            print("** class name missing **")
            return
        arguments = line.split()
        instance = self.return_class(arguments[0].strip('"'))
        if len(arguments) == 1:
            (print("** instance id missing **")
                if instance is not None
                else '')
        elif len(arguments) >= 2:
            try:
                if instance is not None:
                    self.have_instances(arguments[0], arguments[1].strip('"'))
                    return '{}.{}'.format(arguments[0],
                                          arguments[1].strip('"'))
            except KeyError:
                print("** no instance found **")

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        key = self.validate_line(line)
        if key is not None:
            arguments = line.split()
            arguments_len = len(line.split()[2:])
            if arguments_len == 0:
                print("** attribute name missing **")
            elif arguments_len == 1:
                print("** value missing **")
            elif arguments_len >= 2:
                setattr(storage.all()[key], arguments[2].strip('"'),
                        arguments[2].__class__(arguments[3].strip('"')))
                storage.save()

    def have_instances(self, classname, obj_id):
        """ test if class have instances """
        storage.all()[classname+'.'+obj_id]

    def count_instances(self, classname):
        """ count instances of certain class """
        return len([obj for obj in storage.all().values()
                    if obj.__class__.__name__ == classname])

    def parseline(self, line):
        from re import match, search
        ret = cmd.Cmd.parseline(self, line)
        regex = match(r'\w+\.\w+\(\)', ret[2])
        if regex and ret[0] in HBNBCommand.classes:
            if ret[1] == '.all()':
                self.do_all(ret[0])
            if ret[1] == '.count()':
                print(self.count_instances(ret[0]))
            return (None, None, '')
        if match(r'\w+\.\w+\([0-9a-z-]+\)', ret[2]) and ret[0] in HBNBCommand.classes:
            self.do_show(ret[0]+' '+search(r"[0-9a-z]+\-([0-9a-z]+(\-)?)+", ret[2]).group())
            return (None, None, '')
        return ret


if __name__ == '__main__':
    HBNBCommand().cmdloop()
