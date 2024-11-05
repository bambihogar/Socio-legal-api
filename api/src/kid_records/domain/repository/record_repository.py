from abc import ABC, abstractmethod


class Record_repository(ABC):
    
    @(abstractmethod)
    def create_kid_record(dto):
        pass
    @(abstractmethod)
    def find_one(id:str):
        pass
    
    @(abstractmethod)
    def search(query:str):
        pass
    
    @(abstractmethod)
    def modify_record(
        kid_id:str,
        kid_name: str,
        kid_last_name: str,
        kid_internal_record_id: str,
        kid_identification: str,
        record_id:str,
        record__court_id:str, 
        record_entry_date:str, 
        record_entry_motivo:str, 
        record_exit_date:str, 
        record_exit_motivo:str,
        record_organization:str,
        responsible_id: str,
        responsible_name: str,
        responsible_id_doc: str,
        responsible_phone_number:str
    ):
        pass


    @(abstractmethod)
    def delete_record(id: str):
        pass