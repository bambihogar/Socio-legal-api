from typing import List


class Responsibles:
    responsible_names: List[str]
    identity_documents: List[str]
    contacts: List[str]

    def __init__(
            self,
            responsible_name: List[str],
            identity_document: List[str],
            contacts: List[str],
        ):
        self.responsible_name = responsible_name
        self.identity_document = identity_document
        self.contacts = contacts
        