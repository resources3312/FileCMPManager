from os import listdir
from os.path import isfile, isdir
from xxhash import xxh64



class BytesCMPManager:
    
    @staticmethod
    def getRawBytesCheckSum(buffer: bytes) -> bin:
        func = xxh64()
        func.update(buffer)
        return func.digest()
    
    @staticmethod
    def cmpByteArrayPair(buffer_1: bytes, buffer_2: bytes) -> bool:
        return BytesCMPManager.getRawBytesCheckSum(buffer_1) == BytesCMPManager.getRawBytesCheckSum(buffer_2)


class FileCMPManager:

    @staticmethod
    def getFileCheckSum(path: str, chunk_size=4096) -> bin:
        try:
            with open(path, "rb") as f:
                return FileCMPManager.getRawBytesCheckSum(f.read())

        except FileNotFoundError: return False 

    @staticmethod
    def cmpFilePair(path_1: str, path_2: str) -> bool:
        return FileCMPManager.getFileCheckSum(path_1) == FileCMPManager.getFileCheckSum(path_2) if isfile(path_1) and isfile(path_2) else False
    
    @staticmethod
    def getFilesCount(dirPath: str) -> int:
        try: return len(listdir(dirPath))
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
    def cmpDirectoryContent(dirPath1, dirPath2) -> bool:
        dirNames1 = FileCMPManager.getFilenamesOfDirectory(dirPath1)
        dirNames2 = FileCMPManager.getFilenamesOfDirectory(dirPath2)
        return any(FileCMPManager.cmpFilePair(dirNames1[i], dirNames2[i]) for i in range(FileCMPManager.getLowDirectory(dirPath1, dirPath2))) if isdir(dirPath1) and isdir(dirPath2) else False



