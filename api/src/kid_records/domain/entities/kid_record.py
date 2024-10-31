from record import Record
from responsible import Responsibles

class kid_record:
    general_id: str
    kid:dict = {
        'id':str,
        'internal_record_id':str,
        'names':str,
        'last_names':str,
        'identification':{
              'personal_id': str, 
          'birth_certificate': str
        }
    }
    record: Record
    responsible: Responsibles

    def __init__(self, id, kid, record, responsibles):
        self.general_id = id
        self.kid = kid
        self.record = record
        self.responsible = responsibles        