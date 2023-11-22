from database.db import get_connection
from .entities.AsignaPermiso import AsignaPermiso
from .entities.AsignaPermisoCompleto import AsignaPermisoCompleto
from .entities.Rol import Rol
from .entities.Permiso import Permiso
from flask import request,render_template
from flask_paginate import Pagination

class AsignaPermisoModel():
    
    @classmethod
    def get_page(self):
        
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor = db.cursor(buffered=True)
            cursor.execute("SELECT COUNT(*) FROM `rolpermiso`;")
            total_reg = cursor.fetchone()[0]
            num_page = request.args.get('page',1,type=int)
            
            zise_page = 5
            inicio = (num_page - 1) * zise_page + 1

            ###
            cursor.execute("SELECT idRol, idPermiso FROM `rolpermiso`;")
            result = cursor.fetchall()
            lista_asignaPermisos = []
            for row in result:                
                cursor.execute("""SELECT `rol`.`id` AS `idRol`,`permisos`.`id` AS `idPermiso`,`rol`.`strNombre` AS `strRol`,
                                    `permisos`.`strNombre` AS `strPermiso`,
                                    `rolpermiso`.`bitIngreso`,`rolpermiso`.`bitModificar`,`rolpermiso`.`bitEliminar`,`rolpermiso`.`intEstado`
                                    FROM `rol` INNER JOIN `permisos` ON `rol`.`id` = %s AND `permisos`.`id` = %s  
                                    INNER JOIN `rolpermiso` ON `rolpermiso`.`idRol` = %s AND `rolpermiso`.`IdPermiso`=%s; """ % (row[0], row[1],row[0],row[1]))
                               
                result = cursor.fetchone()
                asignaRolCompleto = AsignaPermisoCompleto(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
                lista_asignaPermisos.append(asignaRolCompleto)            
            ########
           
            cursor.execute(f"SELECT * FROM `rolpermiso` WHERE idRol >= 1 ORDER BY idRol ASC LIMIT {zise_page} OFFSET {inicio - 1}")
            result = cursor.fetchall()
            permisos = []
            for row in result:
                asignapermiso = AsignaPermiso(row[0],row[1],row[2],row[3],row[4],row[5])
                permisos.append(asignapermiso.__str__())

            fin = min(inicio + zise_page,total_reg)
            
            if (inicio > total_reg):
                fin = total_reg
            
            pagination = Pagination(page = num_page, per_page=zise_page, total = total_reg, display_msg = f"Mostrando registros {inicio} - {fin} de un total de {total_reg}")

            cursor.execute("SELECT `id`, `strNombre`, `strDescripcion`, `strUrl`, `strMetodo`, `intEstado`, `strIcono` FROM `permisos` WHERE `intEstado`>0;")
            result = cursor.fetchall()
            list_permisos = []
            for row in result:
                permiso = Permiso(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                list_permisos.append(permiso.to_JSON())

            cursor.execute("SELECT `id`, `strNombre`, `strDescripcion`, `intEstado`, `strIcono` FROM `rol` WHERE  `intEstado`>0;")
            result = cursor.fetchall()
            list_roles = []
            for row in result:
                rol = Rol(row[0],row[1],row[2],row[3],row[4])
                list_roles.append(rol.__str__())

            db.close()     
            return render_template('gestionasignarpermiso.html',data = lista_asignaPermisos,dataR = list_roles,dataP = list_permisos, paginacion = pagination) 
        except Exception as ex:
            raise Exception(ex)
   
#Registro
    @classmethod
    def set_entidad(self,asignarpermiso):
        try:
            db = get_connection()
            cursor = db.cursor(buffered=True)
            cursor.execute("SELECT * FROM `rolpermiso` WHERE `idRol`= %s AND `IdPermiso` = %s " % (asignarpermiso.idRol,asignarpermiso.idPermiso))
            result = cursor.fetchall()
            if (len(result) == 0):
                with db.cursor() as cursor:
                    sql = """ INSERT INTO `rolpermiso` (`idRol`, `IdPermiso`, `bitIngreso`, `bitModificar`, `bitEliminar`, `intEstado`) 
                            VALUES (%s, %s, %s, %s, %s, %s);"""
                    dato = (asignarpermiso.idRol,asignarpermiso.idPermiso,asignarpermiso.bitIngreso,asignarpermiso.bitModificar,asignarpermiso.bitEliminar,asignarpermiso.intEstado)
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
    def del_entidad(self,idRol,idPermiso):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = "DELETE FROM `rolpermiso` WHERE `idRol`=%s AND `IdPermiso`=%s"
                dato = (idRol,idPermiso)
                cursor.execute(sql,dato)
                fila_afectada = cursor.rowcount
                db.commit()
            db.close()
            return fila_afectada
        except Exception as ex:
            raise Exception(ex)

# actualizar
    @classmethod
    def up_Endidad(self,asignarpermiso):
        try:
            db = get_connection()
            cursor = db.cursor(buffered=True)
            with db.cursor() as cursor:
                sql = """UPDATE `rolpermiso` SET `bitIngreso`=%s,`bitModificar`=%s,`bitEliminar`=%s,`intEstado`=%s 
                     WHERE `idRol`=%s AND`IdPermiso`=%s;"""                     
                dato = (asignarpermiso.bitIngreso,asignarpermiso.bitModificar,asignarpermiso.bitEliminar,asignarpermiso.intEstado,asignarpermiso.idRol,asignarpermiso.idPermiso)
                cursor.execute(sql,dato)
                fila_actualizada = cursor.rowcount
                db.commit()
            db.close()
            return fila_actualizada
        except Exception as ex:
            raise Exception(ex)
    
    
    