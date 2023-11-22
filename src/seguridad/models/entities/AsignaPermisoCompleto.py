class AsignaPermisoCompleto():
    def __init__(self,idRol, idPermiso,strRol,strPermiso,bitIngreso=None,bitModificar=None,bitEliminar=None,intEstado=None) -> None:
        self.idRol = idRol
        self.idPermiso = idPermiso
        self.strRol = strRol
        self.strPermiso = strPermiso
        self.bitIngreso = bitIngreso
        self.bitModificar = bitModificar
        self.bitEliminar = bitEliminar
        self.intEstado = intEstado
    
    def __str__(self) -> str:
        return {
            'idRol': self.idRol, 
            'idPermiso': self.idPermiso,  
            'strRol': self.strRol, 
            'strPermiso': self.strPermiso, 
            'bitIngreso': self.bitIngreso, 
            'bitModificar': self.bitModificar,
            'bitEliminar': self.bitEliminar, 
            'intEstado': self.intEstado 
        }
    
    