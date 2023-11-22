from database.db import get_connection
from .entities.Permiso import Permiso
from flask import request,render_template
from flask_paginate import Pagination

class PermisoModel():
    
    @classmethod
    def get_page(self):
        zise_page = 5
        num_page = 0
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) FROM `permisos`;")
            total_reg = cursor.fetchone()[0]
            num_page = request.args.get('page',1,type=int)
            
            zise_page = 3
            inicio = (num_page - 1) * zise_page + 1
            
            cursor.execute(f"SELECT * FROM `permisos` WHERE id >= 1 ORDER BY id ASC LIMIT {zise_page} OFFSET {inicio - 1}")
            result = cursor.fetchall()
            permisos = []
            for row in result:
                permiso = Permiso(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                permisos.append(permiso.to_JSON())

            fin = min(inicio + zise_page,total_reg)
            
            if (inicio > total_reg):
                fin = total_reg
            
            pagination = Pagination(page = num_page, per_page=zise_page, total = total_reg, display_msg = f"Mostrando registros {inicio} - {fin} de un total de {total_reg}")
            db.close()     
            return render_template('gestionpermiso.html',data = permisos, paginacion = pagination) 
        except Exception as ex:
            raise Exception(ex)
   
#Registro
    @classmethod
    def set_entidad(self,permiso):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = """INSERT INTO `permisos` (`strNombre`, `strDescripcion`, `strUrl`, `strMetodo`, 
                `intEstado`, `strIcono`) VALUES (%s,%s,%s,%s,%s,%s);"""
                dato = (permiso.strNombre,permiso.strDescripcion,permiso.strUrl,permiso.strMetodo,permiso.intEstado,permiso.strIcono)
                cursor.execute(sql,dato)
                filas_ingresadas = cursor.rowcount
                db.commit()
            db.close()
            return filas_ingresadas
        except Exception as ex:
            raise Exception(ex)
# eliminar    
    @classmethod
    def del_entidad(self,id):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = "DELETE FROM `permisos` WHERE `Id`=%s"
                dato = (id,)
                cursor.execute(sql,dato)
                fila_afectada = cursor.rowcount
                db.commit()
            db.close()
            return fila_afectada
        except Exception as ex:
            raise Exception(ex)

# actualizar
    @classmethod
    def up_Endidad(self,permiso):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = """UPDATE `permisos` SET `strNombre`=%s,`strDescripcion`=%s,`strUrl`=%s,`strMetodo`=%s,
                     `intEstado`=%s,`strIcono`=%s WHERE `id` = %s"""                        
                dato = (permiso.strNombre,permiso.strDescripcion,permiso.strUrl,permiso.strMetodo,permiso.intEstado,permiso.strIcono,permiso.id)
                cursor.execute(sql,dato)
                fila_actualizada = cursor.rowcount
                db.commit()
            db.close()
            return fila_actualizada
        except Exception as ex:
            raise Exception(ex)
    
    
    