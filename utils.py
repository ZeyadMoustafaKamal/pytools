""" from abc import ABCMeta
import getopt
import sys
import importlib

youtube = importlib.import_module('youtube')

class IFunctionProccessor(metaclass=ABCMeta):
    pass

class FunctionProccessor(IFunctionProccessor):
    __instance = None
    @staticmethod
    def get_instance():
        return FunctionProccessor.__instance

    def __init__(self):
        if FunctionProccessor.__instance:
            raise Exception('there is an instance before')
        self.opts = {}
        print('an object created')
        FunctionProccessor.__instance = self

    def run_function(self):
        opts, args = self.get_arguments_values()
        func = self.get_function()
        kwargs = {}
        for key, opt in opts:
            kwargs[self.opts[key]] = opt 
        self.import_functions()
        eval(f'{func}(*{args},**{kwargs})')

        
    def get_arguments_values(self):
        # get the values of the arguments from the CMD in order to pass it to the function
        opts_keys = ''
        for opt in self.opts.keys():
            opt = opt.replace('-','')
            opts_keys += opt + ':'
        try:
            opts, args = getopt.getopt(sys.argv[2:], opts_keys)
        except getopt.GetoptError:
            print('You added an invalid argument')
            exit()
        return opts, args

    def import_functions(self):
        for function_name in dir(youtube):
            function = getattr(youtube, function_name)
            if callable(function):
                globals()[function_name] = function

    def add_argument(self, opt, arg):
        self.opts[opt] = arg

    def get_function(self):
        # get the function to run
        function_name = sys.argv[1]
        return function_name
 """



ARGUMENTS = {
    'test':{'-u':'url', '-t':'time'}
}
