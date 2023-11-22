class AsignaRol():
    def __init__(self, idPersona,idRol,intEstado=None) -> None:
        self.idPersona = idPersona
        self.idRol = idRol
        self.intEstado = intEstado
    
    def __str__(self) -> str:
        return {
            'idPersona': self.idPersona,
            'idRol': self.idRol, 
            'intEstado': self.intEstado 
        }
    
    def to_JSON(self) -> str:
        return {
            'idPersona': self.idPersona,
            'idRol': self.idRol, 
            'intEstado': self.intEstado  
        }