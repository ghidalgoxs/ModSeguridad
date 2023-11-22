from flask import Blueprint,redirect,render_template,jsonify,request,url_for,session

# importar los models
from models.RolModel import RolModel
from models.entities.Rol import Rol
main = Blueprint('Rol_blueprint',__name__)

@main.route('/')
def home():
    try:
        if "username" in session:
            print(session['lista_roles'])
            return RolModel.get_page()
        else:
            return redirect(url_for('Login_blueprint.home'))
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

#Ruta para ingreso   
@main.route('/add', methods=['POST'])
def add():

    try:
        id = None
        strNombre = request.form['strNombre']
        strDescripcion = request.form['strDescripcion']
        intEstado = request.form['intEstado']
        strIcono = request.form['strIcono']
        rol = Rol(id,strNombre,strDescripcion,intEstado,strIcono)
        ingresos = RolModel.set_entidad(rol)
        
        if ingresos >= 1:
            return redirect(url_for('Rol_blueprint.home'))
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
            fila_afectada = RolModel.del_entidad(id)
            if fila_afectada == 1:
                return redirect(url_for('Rol_blueprint.home'))
            else:
                return jsonify({'menssage':"Ninguna persona ha sido eliminada"}),404
    except Exception as ex:
        return jsonify({'mesage':str(ex)}),500

@main.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    try:
        strNombre = request.form['strNombre']
        strDescripcion = request.form['strDescripcion']
        intEstado = request.form['intEstado']
        strIcono = request.form['strIcono']
        rol = Rol(id,strNombre,strDescripcion,intEstado,strIcono)
        ingresos = RolModel.up_Endidad(rol)
        if ingresos == 1:
            return redirect(url_for('Rol_blueprint.home'))
        else:
            return jsonify({'menssage':"Error al actualizar"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    