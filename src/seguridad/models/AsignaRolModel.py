from database.db import get_connection
from .entities.AsignaRol import AsignaRol
from .entities.Persona import Persona
from .entities.Rol import Rol
from .entities.AsignaRolCompleto import AsignaRolCompleto
from flask import request,render_template
from flask_paginate import Pagination

class AsignaRolModel():
    
    @classmethod
    def get_page(self):        
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor = db.cursor(buffered=True)
            cursor.execute("SELECT COUNT(*) FROM `personarol`;")
            total_reg = cursor.fetchone()[0]
            num_page = request.args.get('page',1,type=int)
            
            zise_page = 3
            inicio = (num_page - 1) * zise_page + 1

            ###
            cursor.execute("SELECT idPersona, idRol FROM `personarol`;")
            result = cursor.fetchall()
            lista_asignaRoles = []
            for row in result:                
                cursor.execute("""SELECT DISTINCT `persona`.`id`,`rol`.`id`,`persona`.`strNombres`, `persona`.`strApellidos`, `rol`.`strNombre`, `personarol`.`intEstado`
                                    FROM `persona` INNER JOIN `rol` ON `persona`.`id` = %s AND `rol`.`id` = %s 
                                    INNER JOIN `personarol` ON `idPersona` = %s AND `idRol` = %s; """ % (row[0], row[1],row[0], row[1]))
                               
                result = cursor.fetchone()
                asignaRolCompleto = AsignaRolCompleto(result[0],result[1],result[2],result[3],result[4],result[5])
                lista_asignaRoles.append(asignaRolCompleto)            
            ########
            cursor.execute(f"""SELECT * FROM `personarol` 
                               WHERE `idPersona`>= 1 ORDER BY `idPersona` ASC LIMIT {zise_page} OFFSET {inicio - 1}""")
            #cursor.execute(f"""SELECT `persona`.`strNombres`, `persona`.`strApellidos`, `rol`.`strNombre` FROM `persona` 
            #                   INNER JOIN `rol` ON `persona`.`id` >= 1 AND `rol`.`id` >= 1 ORDER BY `persona`.id ASC LIMIT {zise_page} OFFSET {inicio - 1}""")
            

            result = cursor.fetchall()
            asignaRoles = []
            for row in result:
                asignaRol = AsignaRol(row[0],row[1],row[2])
                asignaRoles.append(asignaRol.to_JSON())

            fin = min(inicio + zise_page,total_reg)
            
            if (inicio > total_reg):
                fin = total_reg
            
            pagination = Pagination(page = num_page, per_page=zise_page, total = total_reg, display_msg = f"Mostrando registros {inicio} - {fin} de un total de {total_reg}")

            cursor.execute("SELECT `id`, `strCedula`, `strNombres`, `strApellidos`, `strCorreo`, `strTelefono`, `strDependencia`, `intEstado`, `strCargo` FROM `persona` WHERE `intEstado` > 0;")
            result = cursor.fetchall()
            list_usuarios = []
            for row in result:
                usuario = Persona(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                list_usuarios.append(usuario.to_JSON())

            cursor.execute("SELECT `id`, `strNombre`, `strDescripcion`, `intEstado`, `strIcono` FROM `rol` WHERE  `intEstado`>0;")
            result = cursor.fetchall()
            list_roles = []
            for row in result:
                rol = Rol(row[0],row[1],row[2],row[3],row[4])
                list_roles.append(rol.to_JSON())

            
            db.close()     

            return render_template('gestionasignarrol.html',data = lista_asignaRoles,dataU = list_usuarios,dataR = list_roles,paginacion = pagination) 
        except Exception as ex:
            raise Exception(ex)


#Registro
    @classmethod
    def set_entidad(self,asignaRol):
        try:
            db = get_connection()
            cursor = db.cursor()
            #cursor = db.cursor(buffered=True)
            cursor.execute("SELECT idPersona, idRol FROM `personarol` WHERE idPersona= %s and idRol = %s;" % (asignaRol.idPersona,asignaRol.idRol))
            result = cursor.fetchall()
            if (len(result) == 0):
                with db.cursor() as cursor:
                    sql = "INSERT INTO `personarol` (`idPersona`, `idRol`,`intEstado`) VALUES (%s,%s,%s);"
                    dato = (asignaRol.idPersona,asignaRol.idRol,asignaRol.intEstado)
                    cursor.execute(sql,dato)
                    filas_ingresadas = cursor.rowcount
                    db.commit()    
            else:  
                filas_ingresadas = cursor.rowcount
            db.close()
            return filas_ingresadas
        except Exception as ex:
            raise Exception(ex)
# eliminar    
    @classmethod
    def del_entidad(self,idPersona,idRol):
        try:
            db = get_connection()

            with db.cursor() as cursor:
                sql = "DELETE FROM `personarol` WHERE `idPersona`=%s AND `idRol`=%s"
                dato = (idPersona,idRol,)
                cursor.execute(sql,dato)
                fila_afectada = cursor.rowcount
                db.commit()
            db.close()
            return fila_afectada
        except Exception as ex:
            raise Exception(ex)

# actualizar
    @classmethod
    def up_Endidad(self,asignarol):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = "UPDATE `personarol` SET `intEstado`=%s WHERE `idPersona` = %s AND idRol = %s"                        
                dato = (asignarol.intEstado,asignarol.idPersona,asignarol.idRol)
                cursor.execute(sql,dato)
                fila_actualizada = cursor.rowcount
                db.commit()
            db.close()
            return fila_actualizada
        except Exception as ex:
            raise Exception(ex)
    
    
    