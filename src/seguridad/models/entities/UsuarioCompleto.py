class UsuarioCompleto():
    def __init__(self,id,idPersona,strNombres,strApellidos,username,password) -> None:
        self.id = id
        self.idPersona = idPersona
        self.strNombres = strNombres
        self.strApellidos = strApellidos
        self.username = username
        self.password = password
    
    def __str__(self) -> str:
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'strNombres': self.strNombres, 
            'strApellidos': self.strApellidos, 
            'username': self.username, 
            'password': self.password 
        }
    
    def to_JSON(self) -> str:
        return {
            'id': self.id, 
            'idPersona': self.idPersona,            
            'strNombres': self.strNombres, 
            'strApellidos': self.strApellidos, 
            'username': self.username, 
            'password': self.password 
        }