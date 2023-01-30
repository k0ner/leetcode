import collections
from typing import List


class File:

    def __init__(self, name: str, is_dir=True, content=""):
        self.name = name
        self.files = {}
        self.is_dir = is_dir
        self.content = content

    def list(self, path: List[str]) -> List[str]:
        if not path:
            if self.is_dir:
                return sorted([c for c in self.files])
            return [self.name]
        else:
            return self.files[path[0]].list(path[1:])

    def mkdir(self, path: List[str]) -> None:
        if path:
            if path[0] not in self.files:
                self.files[path[0]] = File(name=path[0])
            self.files[path[0]].mkdir(path[1:])

    def append(self, path: List[str], content: str):
        p = path[0]
        if len(path) == 1:
            if p in self.files:
                self.files[p].content += content
            else:
                self.files[p] = File(name=path[0], is_dir=False, content=content)
        else:
            self.files[p].append(path[1:], content)

    def read(self, path: List[str]):
        if not path:
            return self.content
        else:
            return self.files[path[0]].read(path[1:])


class FileSystem:

    def __init__(self):
        self.root = File("")

    def ls(self, path: str) -> List[str]:
        p = [s for s in path.split("/") if s != '']
        return self.root.list(p)

    def mkdir(self, path: str) -> None:
        p = path.lstrip("/").split("/")
        self.root.mkdir(p)

    def addContentToFile(self, filePath: str, content: str) -> None:
        p = [s for s in filePath.split("/") if s != '']
        self.root.mkdir(p[:-1])

        self.root.append(p, content)

    def readContentFromFile(self, filePath: str) -> str:
        return self.root.read(filePath[1:].split("/"))

# Your FileSystem object will be instantiated and called as such:
if __name__ == '__main__':
    path = "/test"
    obj = FileSystem()
    # obj.mkdir(path)
    # param_1 = obj.ls(path)
    # print(param_1)
    obj.mkdir("/a/b/c")
    print(obj.ls("/a/b"))
    print(obj.ls("/"))
    obj.addContentToFile("/a/b/c/d", "hello")
    print(obj.readContentFromFile("/a/b/c/d"))
    filePath = "/test/directory/new/file"
    print(obj.ls("/a/b/c/d"))
    obj.addContentToFile(filePath, "hello_world")
    param_4 = obj.readContentFromFile(filePath)
    print(param_4)
