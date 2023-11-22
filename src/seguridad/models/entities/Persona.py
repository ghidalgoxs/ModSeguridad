
class Persona():
    def __init__(self,id,strCedula=None,strNombres=None,strApellidos=None,strCorreo=None,strTelefono=None,strDependencia=None,intEstado=None,strCargo=None) -> None:
        self.id = id
        self.strCedula = strCedula
        self.strNombres = strNombres
        self.strApellidos = strApellidos
        self.strCorreo = strCorreo
        self.strTelefono =  strTelefono 
        self.strDependencia = strDependencia
        self.intEstado = intEstado
        self.strCargo = strCargo
    
    def __str__(self) -> str:
        return {
            'id': self.id, 
            'strCedula': self.strCedula, 
            'strNombres': self.strNombres, 
            'strApellidos': self.strApellidos, 
            'strCorreo': self.strCorreo, 
            'strTelefono': self.strTelefono,  
            'strDependencia': self.strDependencia, 
            'intEstado': self.intEstado, 
            'strCargo': self.strCargo 
        }
    
    def to_JSON(self) -> str:
        return {
            'id': self.id, 
            'strCedula': self.strCedula, 
            'strNombres': self.strNombres, 
            'strApellidos': self.strApellidos, 
            'strCorreo': self.strCorreo, 
            'strTelefono': self.strTelefono,  
            'strDependencia': self.strDependencia, 
            'intEstado': self.intEstado, 
            'strCargo': self.strCargo 
        }
