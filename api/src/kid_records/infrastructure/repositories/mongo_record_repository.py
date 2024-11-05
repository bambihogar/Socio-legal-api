import json
from uuid import UUID, uuid4
import uuid
from bson import Binary
from fastapi import Depends
from pymongo import ReturnDocument
from src.core.infrastructure.config.database import get_db
from src.kid_records.domain.repository.record_repository import Record_repository

DB = get_db()
class Mongo_record_repository(Record_repository):   

    async def create_kid_record(self, record):
        try:
            kid_record = self.ensamble_kid_record(record,uuid4())
            print(kid_record )
            kid_record2 = dict(kid_record)
            response = DB.insert_one(kid_record)
            print()
            return kid_record2
        
        except Exception as e:
            print('error', e)
            
    
    async def find_one(self, id:str):
        try:
            
            kid_record = DB.find_one({'id':id})
            if kid_record is None:
                return {'msg': f"The record with the if {id} doesn't exist"}
            print('find', id)
            kid_record = self.kid_record_schema(kid_record)
            
            return kid_record
        except Exception as e:
            print('find one has gotten an exception:',e)
    
    async def search(query:str):
        pass
    
    
    async def modify_record(self, record):
        try:
        
            kid_record = self.ensamble_kid_record(record,uuid4())
            kid_record['id']= record.id
            kid_record =  DB.find_one_and_replace({
                'id':record.id},
                kid_record,
                return_document = ReturnDocument.AFTER
            )  
            kid_record = self.kid_record_schema(kid_record)
            return kid_record
        
        except Exception as e:
            print('Update record has gotten an exception:',e)


    
    async def delete_record(id: str):
        pass
    
    
    def kid_schema(self,kid_record)-> dict:
        return {
            'id':kid_record['id'],
            'internal_id':kid_record['kid']['internal_id'],
            'names':kid_record['kid']['names'],
            'last_names':kid_record['kid']['last_names'],
            'identification':{
                  'personal_id': kid_record['kid']['identification']['personal_id'], 
                  'birth_certificate': kid_record['kid']['identification']['birth_certificate']
            },
        }

    def kid_schemas(self,kid_records)-> list[dict]:
        return [ self.kid_schema(kid) for kid in kid_records ]


    def kid_record_schema(self,kid_record)-> dict:
        return {
            'id':  kid_record['id'],
            'kid':{
                  'internal_id':kid_record['kid']['internal_id'],
                  'names':kid_record['kid']['names'],
                  'last_names':kid_record['kid']['last_names'],
                  'identification':{
                        'personal_id': kid_record['kid']['identification']['personal_id'], 
                        'birth_certificate': kid_record['kid']['identification']['birth_certificate']
                    },
                },
            'responsibles': {
                'names': kid_record['responsibles']['names'],
                'identifications': kid_record['responsibles']['identifications'],
            'contacts': kid_record['responsibles']['contacts']
                },

            'record': {
                 'court_id': kid_record['record']['court_id'],
                 'bambi_entry_dates':kid_record['record']['bambi_entry_dates'],
                 'bambi_entry_reasons': kid_record['record']['bambi_entry_reasons'],
                 'bambi_departure_date': kid_record['record']['bambi_departure_date'] ,
                 'bambi_departure_reason':  kid_record['record']['bambi_departure_reason'] ,
                 'justice_organization': kid_record['record']['justice_organization'] 
                }      
        }


    def ensamble_kid_record(self,dto, id):
            kid_record = {
                'id': id.hex,
                'kid':{
                    'internal_id': dto.kid_internal_id,
                    'last_names': dto.kid_last_names ,
                    'names': dto.kid_names,
                    'identification': {
                         'personal_id': dto.kid_personal_id,
                         'birth_certificate': dto.kid_birth_certificate
                    }       
                },
                'record':{
                    'court_id': dto.record_court_id,
                    'bambi_entry_dates': dto.record_bambi_entry_date,
                    'bambi_entry_reasons':dto.record_bambi_entry_reasons,
                    'bambi_departure_date': dto.record_bambi_departure_date,
                    'bambi_departure_reason': dto.record_bambi_departure_reason,
                    'justice_organization': dto.record_justice_organization             
                },
                'responsibles':{
                    'names':dto.responsible_names ,
                    'identifications': dto.responsible_identification,
                    'contacts': dto.responsible_contact
                    }, 
                }
                
            
            return kid_record

    