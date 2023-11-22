class AsignaRolCompleto():
    def __init__(self, idPersona, idRol, strNombres,strApellidos,strNombre,intEstado=None) -> None:
        self.idPersona = idPersona
        self.idRol = idRol
        self.strNombres = strNombres
        self.strApellidos = strApellidos
        self.strNombre = strNombre
        self.intEstado = intEstado
    
    def __str__(self) -> str:
        return {
            'idPersona': self.idPersona,
            'idRol': self.idRol,
            'strNombres': self.strNombres,
            'strApellidos': self.strApellidos, 
            'strNombre': self.strNombre, 
            'intEstado': self.intEstado 
        }
    
    def to_JSON(self) -> str:
        return {
            'idPersona': self.idPersona,
            'idRol': self.idRol,
            'strNombres': self.strNombres,
            'strApellidos': self.strApellidos, 
            'strNombre': self.strNombre, 
            'intEstado': self.intEstado 
        }