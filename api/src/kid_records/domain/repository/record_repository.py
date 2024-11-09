from abc import ABC, abstractmethod


class Record_repository(ABC):
    
    @(abstractmethod)
    def create_kid_record(dto):
        pass
    @(abstractmethod)
    def find_one(id:str):
        pass
    
    @(abstractmethod)
    def search(dto,query:str):
        pass
    
    @(abstractmethod)
    def modify_record():
        pass


    @(abstractmethod)
    def delete_record(id: str):
        pass