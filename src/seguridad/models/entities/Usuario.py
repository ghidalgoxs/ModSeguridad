from werkzeug.security import check_password_hash

class Usuario():
    def __init__(self,id,idPersona,username,password) -> None:
        self.id = id
        self.idPersona = idPersona
        self.username = username
        self.password = password
    
    def __str__(self) -> str:
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'username': self.username, 
            'password': self.password 
        }
    
    def to_JSON(self) -> str:
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'username': self.username, 
            'password': self.password
        }
    
    def __hash__(self, pasword_hashed, password) -> int:
        return check_password_hash(pasword_hashed,password)

    
   