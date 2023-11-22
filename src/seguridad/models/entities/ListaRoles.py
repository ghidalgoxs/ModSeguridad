

class ListaRoles():
    def __init__(self,id,strNombre) -> None:
        self.id = id
        self.strNombre = strNombre
        
    def __str__(self) -> str:
        return {
            'id':self.id,
            'strNombre': self.strNombre 
        }