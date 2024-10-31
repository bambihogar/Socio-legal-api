class Kid:
    id: str
    internal_record_id:str
    names: str
    last_names: str 
    identification: dict = {
        'personal_id': str, 
        'birth_certificate': str,
        }
    
    def __init__(self, internal_record_id:str, names:str, last_names:str, identification:dict):
        self.internal_record_id = internal_record_id
        self.names = names
        self.last_names = last_names
        self.identification = identification

