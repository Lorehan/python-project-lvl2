import json
from gendiff.cli import parse_arguments


def generate_diff(file_path1, file_path2, format='PLAIN'):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys = sorted(file1.keys() | file2.keys())
    diff_list = []
    for key in keys:
        if key not in file1:
            diff_list.append(f'  + {key}: {file2[key]}')
        elif key not in file2:
            diff_list.append(f'  - {key}: {file1[key]}')
        elif file1[key] != file2[key]:
            diff_list.append(f'  - {key}: {file1[key]}')
            diff_list.append(f'  + {key}: {file2[key]}')
        else:
            diff_list.append(f'    {key}: {file1[key]}')
    intermediate_result = '\n'.join(diff_list)
    result = f'{{\n{intermediate_result}\n}}'
    return result


def main():
    first_file, second_file, format = parse_arguments()
    print(generate_diff(first_file, second_file, format=format))


__all__ = (
    'generate_diff'
)


if __name__ == '__main__':
    main()
