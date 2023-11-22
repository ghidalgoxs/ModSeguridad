class AsignaPermiso():
    def __init__(self,idRol, idPermiso,bitIngreso=None,bitModificar=None,bitEliminar=None,intEstado=None) -> None:
        self.idRol = idRol
        self.idPermiso = idPermiso
        self.bitIngreso = bitIngreso
        self.bitModificar = bitModificar
        self.bitEliminar = bitEliminar
        self.intEstado = intEstado
    
    def __str__(self) -> str:
        return {
            'idRol': self.idRol, 
            'idPermiso': self.idPermiso, 
            'bitIngreso': self.bitIngreso, 
            'bitModificar': self.bitModificar,
            'bitEliminar': self.bitEliminar, 
            'intEstado': self.intEstado 
        }
    