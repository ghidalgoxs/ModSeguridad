from database.db import get_connection
from .entities.Usuario import Usuario
from .entities.UsuarioCompleto import UsuarioCompleto
from .entities.Persona import Persona
from flask import request,render_template
from flask_paginate import Pagination

from flask import Blueprint,redirect,render_template,jsonify,request,url_for
from werkzeug.security import generate_password_hash


class UsuarioModel():
    
    @classmethod
    def get_page(self):
        zise_page = 5
        num_page = 0
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor = db.cursor(buffered=True)
            cursor.execute("SELECT COUNT(*) FROM `usuario`;")
            total_reg = cursor.fetchone()[0]
            num_page = request.args.get('page',1,type=int)
            
            zise_page = 3
            inicio = (num_page - 1) * zise_page + 1

            cursor.execute("SELECT id,idPersona FROM `usuario`;")
            result = cursor.fetchall()
            List_usuarios = []
            for row in result:      
                cursor.execute("""SELECT `usuario`.`id`,`persona`.`id` AS idPersona,`persona`.`strNombres`, `persona`.`strApellidos`, 
                                    `usuario`.`username`, `usuario`.`password`
                                    FROM `persona` INNER JOIN `usuario` ON `persona`.`id` = %s AND `usuario`.`id` = %s; """%(row[1], row[0]))
                res = cursor.fetchone()
                usuarioCompleto = UsuarioCompleto(res[0],res[1],res[2],res[3],res[4],res[5])
                List_usuarios.append(usuarioCompleto.to_JSON())
            
            cursor.execute(f"SELECT * FROM `usuario` WHERE id >= 1 ORDER BY id ASC LIMIT {zise_page} OFFSET {inicio - 1}")
            result = cursor.fetchall()
            usuarios = []
            for row in result:
                usuario = Usuario(row[0],row[1],row[2],row[3])
                usuarios.append(usuario.to_JSON())

            fin = min(inicio + zise_page,total_reg)
            
            if (inicio > total_reg):
                fin = total_reg
            
            cursor.execute("SELECT * FROM `persona` WHERE `id`>0")
            result = cursor.fetchall()
            list_personas = []
            for row in result:
                persona = Persona(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                list_personas.append(persona.__str__())


            pagination = Pagination(page = num_page, per_page=zise_page, total = total_reg, display_msg = f"Mostrando registros {inicio} - {fin} de un total de {total_reg}")
            db.close()     
            return render_template('gestionusuario.html',dataU = List_usuarios,dataP = list_personas, paginacion = pagination) 
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_all(self):
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor = db.cursor(buffered=True)
            cursor.execute("SELECT * FROM `usuario`; ")
            result = cursor.fetchall()
            usuarios = []
            for row in result:
                usuario = Usuario(row[0],row[1],row[2],row[3])
                usuarios.append(usuario.to_JSON())
            db.close()     
            return usuarios 
        except Exception as ex:
            raise Exception(ex)

#Registro
    @classmethod
    def set_entidad(self,usuarioCompleto):
        try:
            filas_ingresadas=0
            db = get_connection()
            cursor = db.cursor(buffered=True)
            cursor.execute("SELECT id FROM `usuario` WHERE idPersona = %s;"%(usuarioCompleto.idPersona))
            result = cursor.fetchone()
            
            if result is not None :
                return filas_ingresadas
            else:                
                with db.cursor() as cursor:
                    sql = """INSERT INTO `usuario` (`idPersona`, `username`, `password`)
                    VALUES (%s,%s,%s);"""
                    dato = (usuarioCompleto.idPersona,usuarioCompleto.username,generate_password_hash(usuarioCompleto.password))
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
                sql = "DELETE FROM `usuario` WHERE `id`=%s"
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
    def up_Endidad(self,usuario):
        try:
            db = get_connection()
            with db.cursor() as cursor:
                sql = """UPDATE `usuario` SET `password`=%s 
                    WHERE `idPersona`=%s"""                        
                dato = (generate_password_hash(usuario.password),usuario.idPersona)
                cursor.execute(sql,dato)
                fila_actualizada = cursor.rowcount
                db.commit()
            db.close()
            return fila_actualizada
        except Exception as ex:
            raise Exception(ex)

   