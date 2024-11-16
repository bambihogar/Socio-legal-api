import json
import csv, re
import os
from pymongo import MongoClient
from api.src.core.infrastructure.config.config import get_settings
from dotenv import load_dotenv


array = []
load_dotenv()

# This script was used as an ETL for cleaning and transforming the data taken from 
# the excel which contained the kid's records and then loaded into a mongodb database.
# this script is needed no more because the data is already allocated into the db, 
# it was left here so that the people which continue to work in this project know how the database was populated
def organizing_identification(kid_identification):
    if ( 
            'C. I.' in kid_identification[0].upper() or 
            'C.I.' in kid_identification[0].upper() or
            'V-' in kid_identification[0].upper()
            ):
                ci = kid_identification[0]
                if(len(kid_identification)>1):
                    birth_certificate = kid_identification[1]
                else:
                    birth_certificate = 'No se tiene información'         
    elif(
             'SE DESCONOCE' in kid_identification[0].upper() or 
             'NO APARECE' in kid_identification[0].upper() or  
             'EN ESPERA DEL FINIQUITO DEL TRIBUNAL' in kid_identification[0].upper()
             ):
                ci = 'NO SE TIENE INFO'
                birth_certificate = 'NO SE TIENE INFO'
    else:
            birth_certificate = kid_identification[0]
            ci = None
    
    return birth_certificate, ci      
     
def organizing_responsible(responsible):
    responsible = re.split(' y | e |-|/',responsible )
    if(responsible[0] == ''):
        responsible[0] = 'NO SE TIENE INFO'
    return responsible

def organizing_entry_date(bambi_entry_dates):
        bambi_entry_dates = re.split(' / |Reing. ',bambi_entry_dates )
        bambi_entry_date = bambi_entry_dates[0]
        return bambi_entry_dates

def organizing_entry_reason(entry_reasons):
      reasons = re.split(', | y |-| / ',entry_reasons)
      if len(reasons) == 1 and reasons[0] =='':
            reasons[0] = 'NO SE TIENE INFO'
      return reasons
       
def organizing_justice(organization):
        if( organization == ''):
              justice_organization = 'NO SE TIENE INFO' 
        else: 
            justice_organization =  organization#line[7] 
        return justice_organization 
      
def organizing_responsible_id(responsible_id):
      if(responsible_id[0] == ''):
               responsible_id[0] = 'NO SE TIENE INFO'
      return responsible_id

def organizing_names(complete_names):
        names = complete_names[-1]
        last_names = complete_names[0]
        return names, last_names

      
 
with open('/home/alfonsoski15/Escritorio/dataBambi.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    i = 1
    for line in csv_reader:
        general_id = line[-1]
        internal_id = line[0]
        complete_names=line[1].split(',') 
        names, last_names = organizing_names(complete_names)
        kid_identification = line[2].split('/')
        birth_certificate, ci = organizing_identification(kid_identification)
        responsible = organizing_responsible(line[9])
        responsible_identification = organizing_responsible_id(line[10].split('/'))
        responsible_contact = re.split(' 7 |/', line[11])
        if(responsible_contact[0] ==''):
               responsible_contact[0] = None
        
        if (line[8] == ''):
            court_id = None
        else:
            court_id = line[8]

        bambi_entry_dates = organizing_entry_date(line[3])
        entry_reasons = organizing_entry_reason(line[4])
        bambi_departure_date = organizing_entry_date(line[5])
        bambi_departure_reason = line[6]
        justice_organization = organizing_justice(line[7])
        
        row = {
            'id':general_id,
            'kid':{
                'internal_id': internal_id,
                'last_names': last_names,
                'names': names,
                'identification':{
                    'personal_id':ci,
                    'birth_certificate':birth_certificate
                },
            },    
            'responsibles':{
                'names':responsible,
                'identifications':responsible_identification,
                'contacts':responsible_contact
            },
            'record':{
                'court_id':court_id,
                'bambi_entry_dates':bambi_entry_dates,
                'bambi_entry_reasons':entry_reasons,
                'bambi_departure_date':bambi_departure_date,
                'bambi_departure_reason':bambi_departure_reason,
                'justice_organization':justice_organization,
            }
        }
        array.append(row)

array.pop(0)


try:
    uri = os.getenv("DB_CONNECTION")
    uri_remote  = os.getenv('DB_CONNECTION_REMOTE')
    uri_compose = os.getenv("DB_CONNECTION_COMPOSE")#os.getenv("DB_CONNECTION_COMPOSE_LOCAL")
    
    client = MongoClient(uri_remote)
    if client.admin.command("ping")["ok"] == 1:
        print("Connected to the database successfully")
        database = client['bambi_socio_legal']
        kid_record_collection = database['kid_information']
        Auditing_collection = database['auditing']
        massive_insert_response = kid_record_collection.insert_many(array)

        kid_record_collection.create_index(
        [
            ('kid.internal_id', 'text'),
            ('kid.last_names', 'text'),
            ('kid.names', 'text'),
            ('record.court_id', 'text'),
            ('record.bambi_entry_dates', 'text'),
            ('record.bambi_departure_dates', 'text')
        ],
        name='search_kids_index'
        )
    else:
        print("Failed to connect to the database")
    print('yasta')
except Exception as ex:
    print("Failed to connect to the database")
    print('conectadose a DB: {}'.format(ex))
finally:
    print('Conexion finalizada')


