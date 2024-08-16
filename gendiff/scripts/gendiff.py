import argparse
import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys = file1.keys() | file2.keys()
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
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
