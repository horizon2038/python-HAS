from typing import Protocol
import secrets

from application.userrepository import UserRepository
from domain.tokengenerator import TokenGenerator

class UserAuthentication(Protocol):
    def __init__(self):
        pass

    def authenticate(self, id: str, password: str):
        pass

class UserAuthenticationImpl():
    def __init__(self, userrepository: UserRepository, tokengenerator: TokenGenerator):
        #These are injected by the Factory, so there is no problem even if they are redundant.
        self.userrepository: UserRepository = userrepository
        self.tokengenerator: TokenGenerator = tokengenerator

    def authenticate(self, id: str, password: str): #already hashed
        if (self.userrepository.userexists(id) and password != None):
            correct_password: str = self.userrepository.searchpassword_byuserid(id)
            if(password == correct_password):
                return self.__generatetoken()

    def __generatetoken(self):
        return self.tokengenerator.generatetoken()

    
