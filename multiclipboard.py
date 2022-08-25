"""
This is a multiclipboard commandline application where you can save what would be on you clipboard
to a json file with a key you provide so whenever you need to retrieve it would be easy

Arguments
save : it stores what's on your clipboard while asking you a key to associate it with
list : prints all the stored keys and value
load : retrieve a value and copies it to your clipboard
delete : delete a stored value
"""


import sys
import clipboard
from os.path import exists
import json

args = sys.argv[1:]

# here provide a file name or path
file_name = 'clipboard.json'

if len(args) != 1:
    raise ValueError('provide a correct argument')

count = 0
for i in ['save', 'list', 'load', 'delete']:
    if i not in args:
        count += 1
if count == 4:
    raise ValueError(f'{args[0]} is not a correct argument')


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


data = file_loader(file_name)

if args[0] == 'save':
    key = input("enter a key: ")
    data[key] = clipboard.paste()
    file_creator(file_name, data)

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
        file_creator(file_name, data)
    else:
        raise ValueError('enter a valid key')





