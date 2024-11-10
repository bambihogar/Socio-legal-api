from src.kid_records.application.queries.search.types.dto import Search_kid_dto
from src.kid_records.domain.repository.record_repository import Record_repository
from src.kid_records.infrastructure.schemas import kid_records_mongo_schemas as ch
from src.core.infrastructure.config.database import get_db
from src.core.application.error import Error
from src.core.application.result_handlers.result import Result
from uuid import uuid4
from fastapi import Depends
from pymongo import ReturnDocument

DB = get_db()

class Mongo_record_repository(Record_repository):   

    async def create_kid_record(self, record):
        try:
            kid_record = ch.ensamble_kid_record(record,uuid4())
            original_kid_record = dict(kid_record)
            db_result = DB.insert_one(kid_record)
            return Result.success(original_kid_record)
        
        except Exception as e:
            print('e', e)
            return Result.failure('MongoDB Exception', type(e))
            
    
    async def find_one(self, id:str):
        try:
            kid_record = DB.find_one({'id':id})
            if kid_record is None:    
                return Result.failure(Error(f'Kid Record Not Found', f'Kid record with id {id} was not found'))
            kid_record = ch.kid_record_schema(kid_record)
            return Result.success(kid_record)
        except Exception as e:
            print(e)
            return Result.failure('MongoDB Exception', type(e))
    
    async def search(self, query:Search_kid_dto):
        try:
            kids = DB\
                .find({
                     '$text':{'$search': query.search}})\
                .skip(query.page*query.per_page)\
                .limit(query.per_page).to_list()
            if kids is None:
                return Result.failure(Error(f'Kid Records Not Found', f"There is no records matching {query.search} "))
            kids = ch.kid_schemas(kids)
            return Result.success(kids)
        except Exception as e:
                print(e.__cause__)
                r:Result =Result.failure(Error('MongoDB Exception', e.__cause__ ))
                print(e)
                return Result.failure(Error('MongoDB Exception', e.__cause__ ))


    
    
    async def modify_record(self, record):
        try:
            
            kid_record = ch.ensamble_kid_record(record,uuid4())
            kid_record['id']= record.id
            kid_record =  DB.find_one_and_replace({
                'id':record.id},
                kid_record,
                return_document = ReturnDocument.AFTER
            )
            if kid_record is None:    
                return Result.failure(Error(f'Kid Record Not Found', f'Kid record with id {record.id} was not found, so that it was not modified'))
            kid_record = ch.kid_record_schema(kid_record)
            print('kid record update',kid_record)
            return Result.success(kid_record)
        
        except Exception as e:  
            print('excepcion en modify record', e)
            return Result.failure(Error('MongoDB Exception', type(e)))


    
    async def delete_record(self, id: str):
        try:
            deleted = DB.find_one_and_delete({'id':id})
            if deleted is None:   
                return Result.failure(Error(f'Kid Record Not Found', f'Kid record with id {id} was not found, therefore it was not deleted'))
            deleted = ch.kid_record_schema(deleted)
            return Result.success(deleted)
        except Exception as e:
            return Result.failure(Error('MongoDB Exception', type(e)))
    
    
    
    