from gendiff.load_file import load_file


TEST_DICT = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False
}

JSON_PATH = 'tests/fixtures/input/JSON/file1.json'
YAML_PATH = 'tests/fixtures/input/yaml/file1.yaml'


def test_load_file():
    assert load_file(JSON_PATH) == TEST_DICT
    assert load_file(YAML_PATH) == TEST_DICT
