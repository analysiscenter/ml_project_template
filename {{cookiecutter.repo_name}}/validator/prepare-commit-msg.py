""" Script to run validation. """
import json

# Define list of tuples with Validator class and path to yaml configs, e.g.
# from validator import Model
# VALIDATORS = [(Model, 'validator/config.yaml')]

VALIDATORS = []

def start_validation(validators):
    """ Start validation scheme described by `VALIDATORS`. """
    data = []

    for val, config in validators:
        val = val(config)
        val.run()
        data.append({
            'name': val.__class__.__name__,
            'config': config,
            **val.metrics
        })
    with open('validator_results.json', 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    start_validation(VALIDATORS)
