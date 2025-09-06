from os import listdir, stat
from time import perf_counter
from os.path import isfile, isdir
from xxhash import xxh64
from datetime import datetime


def timer(func):
    def wrapper():
        start = perf_counter()
        func()
        print(f"Executed: {perf_counter() - start} sec")

    return wrapper

class BytesCMPManager:
    
    @staticmethod
    def getRawBytesCheckSum(buffer: bytes, formatHex=False, chunkSize=4096) -> bin:
        func = xxh64()
        for chunk in (buffer[i:i+chunkSize] for i in range(0, len(buffer), chunkSize)): func.update(chunk)
        #func.update(buffer)
        return func.digest() if not formatHex else func.hexdigest()
    
    @staticmethod
    def cmpByteArrayPair(buffer_1: bytes, buffer_2: bytes) -> bool:
        return BytesCMPManager.getRawBytesCheckSum(buffer_1) == BytesCMPManager.getRawBytesCheckSum(buffer_2)


class FileCMPManager:

    @staticmethod
    def getFileCheckSum(path: str, formatHex=False) -> bin:
        try:
            with open(path, "rb") as f:
                return BytesCMPManager.getRawBytesCheckSum(f.read(), formatHex)

        except FileNotFoundError: return False 

    @staticmethod
    def cmpFilePair(path_1: str, path_2: str) -> bool:
        return FileCMPManager.getFileCheckSum(path_1) == FileCMPManager.getFileCheckSum(path_2) if isfile(path_1) and isfile(path_2) else False
    
    @staticmethod
    def getFilesCount(dirPath: str) -> int:
        try: return len(listdir(dirPath))
        except: return -1
    
    @staticmethod
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
    def cmpDirectoryContent(dirPath1, dirPath2) -> bool:
        dirNames1 = FileCMPManager.getFilenamesOfDirectory(dirPath1)
        dirNames2 = FileCMPManager.getFilenamesOfDirectory(dirPath2)
        return any(FileCMPManager.cmpFilePair(dirNames1[i], dirNames2[i]) for i in range(FileCMPManager.getLowDirectory(dirPath1, dirPath2))) if isdir(dirPath1) and isdir(dirPath2) else False

@timer
def test():
    print("Copy" if FileCMPManager.cmpFilePair("./testFiles/im_1.jpg", "./testFiles/im_2.jpg") else "No copy")

def main() -> None:
    test()

if __name__ == '__main__': main()
