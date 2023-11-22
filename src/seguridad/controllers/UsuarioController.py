from flask import Blueprint,redirect,jsonify,request,url_for,session

# importar los models
from models.UsuarioModel import UsuarioModel
from models.entities.Usuario import Usuario
main = Blueprint('Usuario_blueprint',__name__)

@main.route('/')
def home():
    try:
        if "username" in session:
            return UsuarioModel.get_page()
        else:
            return redirect(url_for('Login_blueprint.home'))
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

#Ruta para ingreso   
@main.route('/add', methods=['POST'])
def add():

    try:
        id = None
        idPersona = request.form['idPersona']
        username = request.form['username']     
        password = request.form['password'] 
        usuario = Usuario(id,idPersona,username,password)
        ingresos = UsuarioModel.set_entidad(usuario)
        
        if ingresos >= 1:
            return redirect(url_for('Usuario_blueprint.home'))
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
            fila_afectada = UsuarioModel.del_entidad(id)
            if fila_afectada == 1:
                return redirect(url_for('Usuario_blueprint.home'))
            else:
                return jsonify({'menssage':"Ninguna persona ha sido eliminada"}),404
    except Exception as ex:
        return jsonify({'mesage':str(ex)}),500

@main.route('/edit/<int:id>/<int:idPersona>', methods=['POST'])
def edit(id,idPersona):
    try:
        
        username = request.form.get('username')
        password = request.form.get('password')
        if password is None:
            return jsonify({'menssage':"password vacio"}),404
        else:
            usuario = Usuario(id,idPersona,username,password)
            ingresos = UsuarioModel.up_Endidad(usuario)

        if ingresos == 1:
            return redirect(url_for('Usuario_blueprint.home'))
        else:
            return jsonify({'menssage':"Error al actualizar"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500