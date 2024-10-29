class Contact:
    def __init__(self, lastname, firstname,
                 surname='', organization='',
                 position='', phone='', email='', status=1):
        self.lastname = lastname
        self.firstname = firstname
        self.surname = surname
        self.organization = organization
        self.position = position
        self.phone = phone
        self.email = email
        self.status = status

    def __eq__(self, other):
        return self.lastname == other.lastname and self.firstname == other.firstname