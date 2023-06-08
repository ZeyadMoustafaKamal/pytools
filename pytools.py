import getopt
import sys
import importlib
import pkgutil
import os
from youtube import *
from utils import ARGUMENTS


def update_arguments(function_name, args):
    ARGUMENTS[function_name] = args

update_arguments('test', {'-u':'url', '-t':'time'})

def test(*args,**kwargs):
    # just if someone wants to test the tools
    print('Yes it works!!')
    print(kwargs.get('url'))
    print(kwargs.get('time'))

class FunctionProccessor:

    def __init__(self):
        self.opts = {}

    def run_function(self):
        opts, args = self.get_arguments_values()
        print(opts)
        func = self.get_function()
        kwargs = {}
        for key, opt in opts:
            kwargs[self.opts[key]] = opt
        try:
            eval(f'{func}(*{args},**{kwargs})')
        except NameError:
            print('and error accured please contanct a developer')

        
    def get_arguments_values(self):
        # Get the values of the arguments from the CMD in order to pass it to the function
        opts_keys = ''
        long_keys = []
        for opt in self.opts.keys():
            if not opt.startswith('--'):
                opt = opt.replace('-','')
                opts_keys += opt + ':'
            else:
                print(opt)
                opt = opt.replace('--','')
                long_keys.append(opt)
        try:
            opts, args = getopt.getopt(sys.argv[2:], opts_keys,long_keys)
        except getopt.GetoptError as e:
            print(e)
            print('Invalid argument')
            exit()
        
        opts = [(opt, True) if value == '' else (opt, value) for opt, value in opts]
        print(opts)
        return opts, args

    def add_argument(self, opt, arg):
        self.opts[opt] = arg

    def get_function(self):
        # get the function to run
        function_name = sys.argv[1]
        if function_name in ARGUMENTS:
            root_directory = os.path.dirname(os.path.abspath(__file__))
            for module_info in pkgutil.iter_modules([root_directory]):
                module_name = module_info.name
                module = importlib.import_module(module_name)
            # Add all the functions from the module to the current namespace
                function = getattr(module, function_name, None)
                print(function)
                if callable(function):
                    print('adding a function')
                    globals()[function_name] = function
                return function_name
        print('Invalid function name')
        exit()


if __name__ == '__main__':
    function = FunctionProccessor()
    func = function.get_function()
    
    args = ARGUMENTS.get(func)
    if args is not None:
        for arg in args:
            function.add_argument(arg, args.get(arg))
    function.run_function()
