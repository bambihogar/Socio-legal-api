def ensamble_kid_record(dto, id):
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

    
def kid_schema(kid_record)-> dict:
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

def kid_schemas(kid_records)-> list[dict]:
    kids=[ kid_schema(kid) for kid in kid_records ]
    return kids



def kid_record_schema(kid_record)-> dict:
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

