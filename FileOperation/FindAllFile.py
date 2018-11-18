import os


def scanDir(path=os.curdir):
    path = os.path.realpath(path)
    __list = []
    for item in os.listdir(path):
        item = os.path.join(path, item)
        # @todo 查找、过滤等
        if os.path.isdir(item):
            __list += scanDir(item)
        else:
            __list.append(item)
    return __list


path_list = scanDir()
print(path_list)
