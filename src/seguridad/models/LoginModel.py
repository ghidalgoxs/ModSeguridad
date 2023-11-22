from database.db import get_connection
from flask import render_template,session
#Entidades
from models.entities.Usuario import Usuario
#from models.entities.ListaRoles import ListaRoles
#from models.entities.ListaPermisos import ListaPermisos
#import json


class LoginModel():
    
    @classmethod
    def login_page(self,usuario):
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor = db.cursor(buffered=True)
            cursor.execute("SELECT `id`, `idPersona`, `username`, `password` FROM `usuario` WHERE `username`= '%s';" %(usuario.username))
            result = cursor.fetchone()
            if result is not None:
                usuario_db = Usuario(result[0],result[1],result[2],result[3]) 
                db.close()
                return usuario_db
            else:
                return None    
        except Exception as ex:
            raise Exception(ex)
     
    @classmethod     
    def get_roles(self):
        try:
            if "username" in session:
                username = session['username']
                session['lista_roles'] = []
                db = get_connection()
                cursor = db.cursor()
                cursor = db.cursor(buffered=True)
                lista_roles = session['lista_roles']
                #### seleccionar el o los roles
                cursor.execute("SELECT `idRol` FROM `personarol` WHERE `idPersona`='%s';" %(session["idPersona"]))
                rRoles = cursor.fetchall()
                for row_rol in rRoles:
                    cursor.execute("SELECT `id`, `strNombre` FROM `rol` WHERE `id` = '%s';" %(row_rol[0]))
                    rRolNombre = cursor.fetchall()
                    columnas_roles = [column[0] for column in cursor.description]
                    for row_Nombre in rRolNombre:
                        lista_roles.append(dict(zip(columnas_roles,row_Nombre)))
                session['lista_roles'] = lista_roles
                return render_template('header.html',_roles = lista_roles,user = username) 
            else:
                return render_template('login.html')
        except Exception as ex:
            raise Exception(ex)

    @classmethod     
    def get_permisos(self,rol):
        try:
            if "username" in session:
                username = session['username']
                session['lista_permisos'] = []
                db = get_connection()
                cursor = db.cursor()
                cursor = db.cursor(buffered=True)
                lista_permisos = session['lista_permisos']
                #### seleccionar el o los permisos
                cursor.execute("SELECT `IdPermiso` FROM `rolpermiso` WHERE `idRol` = '%s';" %(rol))
                rPemisos = cursor.fetchall()
                for row_Permiso in rPemisos:
                    cursor.execute("""SELECT `strNombre`, `strUrl` FROM `permisos` WHERE `id` = '%s'; """ % (row_Permiso[0]))         
                    rPermiso = cursor.fetchone()
                    columnas_permisos = [column[0] for column in cursor.description]
                    lista_permisos.append(dict(zip(columnas_permisos,rPermiso)))
                session['lista_permisos'] = lista_permisos
                return render_template('header.html',_permisos = session['lista_permisos'], _roles =  session['lista_roles'],user = username) 
            else:
                return render_template('login.html')
        except Exception as ex:
            raise Exception(ex)
   