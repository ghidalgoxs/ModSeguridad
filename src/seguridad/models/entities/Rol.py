class Rol():
    def __init__(self,id,strNombre=None,strDescripcion=None,intEstado=None,strIcono=None) -> None:
        self.id = id
        self.strNombre = strNombre
        self.strDescripcion = strDescripcion
        self.intEstado = intEstado
        self.strIcono = strIcono
    
    def __str__(self) -> str:
        return {
            'id': self.id, 
            'strNombre': self.strNombre, 
            'strDescripcion': self.strDescripcion, 
            'intEstado': self.intEstado, 
            'strIcono': self.strIcono 
        }
    
    def to_JSON(self) -> str:
        return {
            'id': self.id, 
            'strNombre': self.strNombre, 
            'strDescripcion': self.strDescripcion, 
            'intEstado': self.intEstado, 
            'strIcono': self.strIcono 
        }
