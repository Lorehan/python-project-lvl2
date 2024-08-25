import os
import json
import yaml


def load_file(file_path):
    file_extension = os.path.splitext(file_path)[1]
    match file_extension:
        case '.json':
            data = json.load(open(file_path))
        case '.yml' | '.yaml':
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)
    return data
