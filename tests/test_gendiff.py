from gendiff.scripts.gendiff import generate_diff


with open('tests/fixtures/output/result.txt', "r") as test_file:
    result_from_file = test_file.read()


PATH1 = 'tests/fixtures/input/JSON/file1.json'
PATH2 = 'tests/fixtures/input/JSON/file2.json'


def test_gendiff():
    assert generate_diff(PATH1, PATH2) == result_from_file
