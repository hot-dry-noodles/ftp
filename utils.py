import os
import stat
import sys
import time

# prefer official qt bindings
if 'PySide2' in sys.modules:
    from PySide2.QtGui import QStandardItem, QIcon
else:
    from PyQt5.QtGui import QStandardItem, QIcon

LOCAL_DEFAULT_PATH = os.getcwd()
REMOTE_DEFAULT_PATH = ''
FILE_DICT = {'py': u'python文件', 'md': u'markdown文件', 'txt': u'文本文件'}
PY_ICON = './ui/icon/py.svg'
TXT_ICON = './ui/icon/txt.svg'
DIR_ICON = './ui/icon/dir.svg'
MD_ICON = './ui/icon/md.svg'
OTHER_ICON = './ui/icon/other.svg'
ICON_DICT = {'py': PY_ICON, 'md': MD_ICON, 'txt': TXT_ICON}


def size2str(size: int) -> str:
    if size < 1024:
        return str(size) + 'B'
    elif size < 1024 * 1024:
        return str(round(float(size) / 1024, 1)) + 'MB'
    else:
        return str(round(float(size) / 1024 / 1024, 1)) + 'GB'


def getFileMode(file):
    st = os.stat(file)
    modes = [
        stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR,
        stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP,
        stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH,
    ]
    mode = st.st_mode
    fullMode = ''
    fullMode += os.path.isdir(file) and 'd' or '-'

    for i in range(9):
        fullMode += bool(mode & modes[i]) and 'rwxrwxrwx'[i] or '-'
    return fullMode


def ListFolder(path=LOCAL_DEFAULT_PATH):
    items = []
    files = os.listdir(path)
    for file in files:
        name, ext = os.path.splitext(file)
        postFix = ext[1:]
        absPath = os.path.join(os.getcwd(), file)
        mode = getFileMode(absPath)
        if postFix:
            name = name + '.' + postFix
        if mode.startswith('d'):
            fType = u'文件夹'
            fIcon = QIcon(DIR_ICON)
        elif FILE_DICT.get(postFix):
            fType = FILE_DICT[postFix]
            fIcon = QIcon(ICON_DICT[postFix])
        else:
            fType = u'未知文件'
            fIcon = QIcon(OTHER_ICON)
        size = os.path.getsize(file)
        tm = os.path.getmtime(file)
        item = []
        nameItem = QStandardItem(fIcon, name)
        item.append(nameItem)
        item.append(QStandardItem(size2str(size)))
        item.append(QStandardItem(fType))
        item.append(QStandardItem(mode))
        item.append(QStandardItem(time.strftime('%Y-%m-%d %H:%M', time.localtime(tm))))
        items.append(item)

    return items
