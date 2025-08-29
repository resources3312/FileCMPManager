from os import listdir
from os.path import isfile, isdir
from xxhash import xxh64


class FileCMPManager:

    @staticmethod
    def getFileCheckSum(path: str, chunk_size=4096) -> bin:
        try:
            with open(path, "rb") as f:
                func = xxh64()
                for chunk in iter(lambda: f.read(chunk_size), b""): func.update(chunk)
                return func.digest()

        except FileNotFoundError: False 
    
    @staticmethod
    def cmpFilePair(path_1: str, path_2: str) -> bool:
        return FileCMPManager.getFileCheckSum(path_1) == FileCMPManager.getFileCheckSum(path_2) if isfile(path_1) and isfile(path_2) else False
    
    @staticmethod
    def getFilesCount(dir_path: str) -> int:
        try: return len(listdir(dir_path))
        except: return -1
    
    def getFilenamesOfDirectory(dirPath: str) -> tuple:
        return tuple([f"{dirPath}/{filename}" for filename in listdir(dirPath)])

    @staticmethod
    def getLowDirectory(dirPath1: str, dirPath2: str) -> int:
        try:
            len1 = FileCMPManager.getFilesCount(dirPath1)
            len2 = FileCMPManager.getFilesCount(dirPath2)
            return len1 if len1 < len2 else len2

        except: return -1

    @staticmethod
    def cmpDirectoryContent(dirPath1, dirPath2) -> list:
        dirNames1 = FileCMPManager.getFilenamesOfDirectory(dirPath1)
        dirNames2 = FileCMPManager.getFilenamesOfDirectory(dirPath2)
        return any(FileCMPManager.cmpFilePair(dirNames1[i], dirNames2[i]) for i in range(FileCMPManager.getLowDirectory(dirPath1, dirPath2))) if isdir(dirPath1) and isdir(dirPath2) else False

    
