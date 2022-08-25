import sys
import clipboard
import json

args = sys.argv[1:]

if len(args) != 1:
    raise ValueError('provide a correct argument')

count = 0
for i in ['save', 'list', 'load']:
    if i not in args:
        count += 1
if count == 3:
    raise ValueError('provide a correct argument')


def file_creator(path: str, content: str) -> None:
    """
    this function creates a json file using the provided content
    :rtype: None
    """

    with open(path, 'w') as f:
        json.dump(content, f)


def file_loader(path: str) -> str:
    """
    this function reads a json file and then returns a dict of
    {keys: values}
    :param path: string
    :return: dict{keys:values}
    """

    with open(path, 'r') as f:
        content = json.load(f)
        return content


if args[0] == 'save':
    file_creator('test.json', {'hello': 'world', 'this': 'is'})
    print(file_loader('test.json'))
elif args[0] == 'load':
    pass
elif args[0] == 'list':
    pass
else:
    pass



