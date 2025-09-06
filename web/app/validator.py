from config import Config
from redis import Redis


class UserRequestAccept:
    def __init__(self, token: str):
        self.__token = token
        self.__redis = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=2, decode_responses=True)
    
    def __addUser(self) -> int:
        try:
            self.__redis.set(self.__token, 0)
            return 0
        
        except: return 0

    def __getUserRequestCount(self) -> int:
        try:
            count = self.__redis.get(self.__token)
            return int(count) if count else self.__addUser()
        except: return 0

    def __addUserRequestCount(self) -> None:
        self.__redis.set(self.__token, self.__getUserRequestCount() + 1)
    
    def getRequestAccept(self) -> bool:
        if self.__getUserRequestCount() <= Config.REQUEST_COUNT: 
            self.__addUserRequestCount()
            return True
        else: return False


