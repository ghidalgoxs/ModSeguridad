from database.db import get_connection
from .entities.Rol import Rol
from flask import request,render_template,session
from flask_paginate import Pagination

class RolModel():
    
    @classmethod
    def get_page(self):
        
        try:
            num_page = 0
            db = get_connection()
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) FROM `rol`;")
            total_reg = cursor.fetchone()[0]
            num_page = request.args.get('page',1,type=int)
                
            zise_page = 3
            inicio = (num_page - 1) * zise_page + 1
                
            cursor.execute(f"SELECT * FROM `rol` WHERE id >= 1 ORDER BY id ASC LIMIT {zise_page} OFFSET {inicio - 1}")
            result = cursor.fetchall()
            roles = []
            for row in result:
                rol = Rol(row[0],row[1],row[2],row[3],row[4])
                roles.append(rol.to_JSON())

            fin = min(inicio + zise_page,total_reg)
                
            if (inicio > total_reg):
                fin = total_reg
                
            pagination = Pagination(page = num_page, per_page=zise_page, total = total_reg, display_msg = f"Mostrando registros {inicio} - {fin} de un total de {total_reg}")
            db.close()     
            return render_template('gestionrol.html',data = roles, paginacion = pagination) 
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_all(self):
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM `rol`; ")
            result = cursor.fetchall()
            roles = []
            for row in result:
                rol = Rol(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                roles.append(rol.to_JSON())
            db.close()     
            return roles 
        except Exception as ex:
            raise Exception(ex)

#Registro
    @classmethod
    def set_entidad(self,rol):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = """INSERT INTO `rol` (`strNombre`, `strDescripcion`, `intEstado`, `strIcono` 
                ) VALUES (%s,%s,%s,%s);"""
                dato = (rol.strNombre,rol.strDescripcion,rol.intEstado,rol.strIcono)
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
                sql = "DELETE FROM `rol` WHERE `Id`=%s"
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
    def up_Endidad(self,rol):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = """UPDATE `rol` SET `strNombre`=%s,`strDescripcion`=%s,
                     `intEstado`=%s,`strIcono`=%s WHERE `id` = %s"""                        
                dato = (rol.strNombre,rol.strDescripcion,rol.intEstado,rol.strIcono,rol.id)
                cursor.execute(sql,dato)
                fila_actualizada = cursor.rowcount
                db.commit()
            db.close()
            return fila_actualizada
        except Exception as ex:
            raise Exception(ex)
    
    
    