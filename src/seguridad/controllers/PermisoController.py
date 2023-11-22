from flask import Blueprint,redirect,render_template,jsonify,request,url_for,session
import os
# importar los models
from models.PermisoModel import PermisoModel
from models.entities.Permiso import Permiso
main = Blueprint('Permiso_blueprint',__name__)

@main.route('/')
def home():
    try:
        if "username" in session:
            return PermisoModel.get_page()
        else:
            return redirect(url_for('Login_blueprint.home'))
        
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

#Ruta para ingreso   
@main.route('/add', methods=['POST'])
def add():
    try:
        ingresos = 0
        id = None
        strNombre = request.form['strNombre']
        strDescripcion = request.form['strDescripcion']
        strUrl = request.form['strUrl']
        strMetodo = request.form['strMetodo']
        intEstado = request.form['intEstado']
        strIcono = request.form['strIcono']
        
        template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        template_dir = os.path.join(template_dir,'seguridad','views')

        permiso = Permiso(id,strNombre,strDescripcion,strUrl,strMetodo,intEstado,strIcono)
        ingresos = PermisoModel.set_entidad(permiso)
        
        if ingresos >= 1:
            return redirect(url_for('Permiso_blueprint.home'))
        else:
            return jsonify({'menssage':"Error al insertar"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

@main.route('/delete/<int:id>')
@main.route('/delete', defaults={'id': None})
def delete(id):
    try:
        if id is None:
            return jsonify({'menssage':"Id vacio"}),404
        else:
            fila_afectada = PermisoModel.del_entidad(id)
            if fila_afectada == 1:
                return redirect(url_for('Permiso_blueprint.home'))
            else:
                return jsonify({'menssage':"Ninguna persona ha sido eliminada"}),404
    except Exception as ex:
        return jsonify({'mesage':str(ex)}),500

@main.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    try:
        strNombre = request.form['strNombre']
        strDescripcion = request.form['strDescripcion']
        strUrl = request.form['strUrl']
        strMetodo = request.form['strMetodo']
        intEstado = request.form['intEstado']
        strIcono = request.form['strIcono']
        permiso = Permiso(id,strNombre,strDescripcion,strUrl,strMetodo,intEstado,strIcono)
        ingresos = PermisoModel.up_Endidad(permiso)
        if ingresos == 1:
            return redirect(url_for('Permiso_blueprint.home'))
        else:
            return jsonify({'menssage':"Error al actualizar"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    