import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        if ('.git' not in root and 'projectfiles' not in root):
            level = root.replace(startpath, '').count(os.sep) - 1
            indent = ('|' if (level + 1 < 0) else '')  + (' ' * (level-1 if level-1<0 else level+1))
            with open("tree.txt", "a+") as f:
                f.write('{}{}/\n'.format(indent, os.path.basename(root)))
                subindent = ' ' * (level+2 if level+1 != 0 else level+1) + ('|' if (level+1) != 0 else '') + (('-' * 2) if level+1 != 0 else '')
                for file in files:
                    f.write('{}{}\n'.format(subindent, file))

list_files(".")