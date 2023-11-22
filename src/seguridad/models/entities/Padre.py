class Padre():
    def __init__(self,id,strNombre=None,intEstado=None,strIcono=None) -> None:
        self.id = id
        self.strNombre = strNombre
        self.intEstado = intEstado
        self.strIcono = strIcono
    
    def __str__(self) -> str:
        return {
            'id': self.id, 
            'strNombre': self.strNombre, 
            'intEstado': self.intEstado, 
            'strIcono': self.strIcono 
        }
    
    def to_JSON(self) -> str:
        return {
            'id': self.id, 
            'strNombre': self.strNombre,  
            'intEstado': self.intEstado, 
            'strIcono': self.strIcono 
        }