import sys
import clipboard
from os.path import exists
import json

args = sys.argv[1:]

if len(args) != 1:
    raise ValueError('provide a correct argument')

count = 0
for i in ['save', 'list', 'load', 'delete']:
    if i not in args:
        count += 1
if count == 4:
    raise ValueError('provide a correct argument')


def file_creator(path: str, content: dict) -> None:
    """
    this function creates a json file using the provided content
    :rtype: None
    """

    with open(path, 'w') as f:
        json.dump(content, f)


def file_loader(path: str) -> dict:
    """
    this function reads a json file and then returns a dict of
    {keys: values}
    :param path: string
    :return: dict{keys:values}
    """
    if exists(path):

        with open(path, 'r') as f:
            content = json.load(f)
            return content
    return {}


data = file_loader('clipboard.json')

if args[0] == 'save':
    key = input("enter a key: ")
    data[key] = clipboard.paste()
    file_creator('clipboard.json', data)

elif args[0] == 'load':
    key = input('enter a key :')
    if key in data:
        clipboard.copy(data[key])
        print('the content is copied to your clipboard')
    else:
        print(r'the key doesn\'t exist')
elif args[0] == 'list':
    print(data)

elif args[0] == 'delete':
    key = input('enter the key: ')
    if key in data.keys():
        del(data[key])
        file_creator('clipboard.json',data)
    else:
        raise ValueError('enter a valid key')





