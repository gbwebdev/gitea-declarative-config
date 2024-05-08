import click
from functools import wraps

def options_group(option_defs, options_dict_name='options'):
    def decorator(f):
        @wraps(f)
        def wrapped(**kwargs):
            # Initialize an empty dictionary for the relevant options
            relevant_options = {}

            # Separate relevant options from other kwargs
            for opt_def in option_defs:
                option_key = opt_def['name'].strip('--').replace('-', '_')
                if option_key in kwargs:
                    relevant_options[option_key] = kwargs.pop(option_key)

            # Call the original function with the packaged options and any remaining kwargs
            return f(**{options_dict_name: relevant_options}, **kwargs)

        # Apply click.option decorators without modifying option_defs
        for opt_def in reversed(option_defs):
            option_name = opt_def['name']
            opt_def_copy = {k: v for k, v in opt_def.items() if k != 'name'}
            wrapped = click.option(option_name, **opt_def_copy)(wrapped)

        return wrapped
    return decorator
