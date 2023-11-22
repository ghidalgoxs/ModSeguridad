class ListaPermisos():
    def __init__(self,strNombre, strUrl) -> None:
        self.strNombre = strNombre
        self.strUrl = strUrl
    
    def __str__(self) -> str:
        return {
            'strNombre': self.strNombre, 
            'strUrl': self.strUrl 
        }
    