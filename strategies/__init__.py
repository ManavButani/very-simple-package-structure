# strategies/__init__.py

import os
import importlib

# Automatically import all strategy modules in the current directory
for filename in os.listdir(os.path.dirname(__file__)):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = filename[:-3]  # Remove the .py extension
        module = importlib.import_module(f".{module_name}", package=__name__)
        
        # Get all functions from the module and import them into the current namespace
        for attr in dir(module):
            if callable(getattr(module, attr)) and not attr.startswith("__"):
                globals()[attr] = getattr(module, attr)
