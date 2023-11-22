from database.db import get_connection
from .entities.Padre import Padre
from flask import request,render_template
from flask_paginate import Pagination

class PadreModel():
    
    @classmethod
    def get_page(self):
        zise_page = 5
        num_page = 0
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) FROM `padre`;")
            total_reg = cursor.fetchone()[0]
            num_page = request.args.get('page',1,type=int)
            
            zise_page = 3
            inicio = (num_page - 1) * zise_page + 1
            
            cursor.execute(f"SELECT * FROM `padre` WHERE id >= 1 ORDER BY id ASC LIMIT {zise_page} OFFSET {inicio - 1}")
            result = cursor.fetchall()
            padres = []
            for row in result:
                padre = Padre(row[0],row[1],row[2],row[3])
                padres.append(padre.to_JSON())

            fin = min(inicio + zise_page,total_reg)
            
            if (inicio > total_reg):
                fin = total_reg
            
            pagination = Pagination(page = num_page, per_page=zise_page, total = total_reg, display_msg = f"Mostrando registros {inicio} - {fin} de un total de {total_reg}")
            db.close()     
            return render_template('gestionpadre.html',data = padres, paginacion = pagination) 
        except Exception as ex:
            raise Exception(ex)

#Registro
    @classmethod
    def set_entidad(self,padre):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = """INSERT INTO `padre` (`strNombre`, `intEstado`, `strIcono` 
                ) VALUES (%s,%s,%s);"""
                dato = (padre.strNombre,padre.intEstado,padre.strIcono)
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
                sql = "DELETE FROM `padre` WHERE `Id`=%s"
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
    def up_Endidad(self,padre):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = """UPDATE `padre` SET `strNombre`=%s,
                     `intEstado`=%s,`strIcono`=%s WHERE `id` = %s"""                        
                dato = (padre.strNombre,padre.intEstado,padre.strIcono,padre.id)
                cursor.execute(sql,dato)
                fila_actualizada = cursor.rowcount
                db.commit()
            db.close()
            return fila_actualizada
        except Exception as ex:
            raise Exception(ex)
    
    
    