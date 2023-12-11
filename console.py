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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
