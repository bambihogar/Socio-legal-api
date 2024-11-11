import json
import csv, re
from pymongo import MongoClient

array = []


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
        #if(len(bambi_entry_dates) > 1):
        #      bambi_reentry_date = bambi_entry_dates[1]
        
        #elif( len(bambi_entry_dates) == 1 and bambi_entry_dates[0] ==''):
        #      print('hola')
        #      bambi_entry_date = None
        #      bambi_reentry_date = None
        #else:
        #      bambi_reentry_date = None    
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

    MONGO_HOST = "localhost" 
    MONGO_PORT = "27018"
    MONGO_DB = "bambi_socio_legal"
    MONGO_USER = "root"
    MONGO_PASS = "secret"

    uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
    client = MongoClient(uri)
    database = client['bambi_socio_legal']
    kid_record_collection = database['kid_information']
    Auditing_collection = database['auditing']
    massive_insert_response = kid_record_collection.insert_many(array)
    print(massive_insert_response)
    print()
    kid_record_collection.create_index({
        'kid.internal_id':'text',
        'kid.last_names':'text',
        'kid.names':'text',
        'record.court_id':'text',
        'record.bambi_entry_dates':'text',
        'record.bambi_departure_dates':'text'
    }, 
    {
        'name':'search_kids_index'
    })
    print('yasta')
except Exception as ex:
    print('conectadose a DB: {}'.format(ex))
finally:
    print('Conexion finalizada')
#acomodar manualmente griselda; 039-2016-JULIO CARRASQUEL, José Isrrael; 372 DÁVALOS CONTRERAS, Santiago Isaac; 798 hasta 802; 013-2023 880;
# 005-2023 870y871; 022-2009 150y151; 026-2009 157 hasta 161; 
#Yoangel D'olio acomodar manual 006-2021


#db.blog.createIndex(
#   {
#     content: "text",
#     "users.comments": "text",
#     "users.profiles": "text"
#   },
#   {
#     name: "InteractionsTextIndex"
#   }
#)