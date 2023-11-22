from flask import Blueprint,redirect,jsonify,request,url_for,session

# importar los models
from models.PersonaModel import PersonaModel
from models.entities.Persona import Persona
main = Blueprint('Persona_blueprint',__name__)

@main.route('/')
def home():
    try:
        if "username" in session:
            return PersonaModel.get_page()
        else:
            return redirect(url_for('Login_blueprint.home'))
        
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

#Ruta para ingreso   
@main.route('/add', methods=['POST'])
def add():

    try:
        id = None
        strCedula = request.form['strCedula']
        strNombres = request.form['strNombres']
        strApellidos = request.form['strApellidos']
        strCorreo = request.form['strCorreo']
        strTelefono = request.form['strTelefono']
        strDependencia = request.form['strDependencia']
        intEstado = request.form['intEstado']
        strCargo = request.form['strCargo']
        persona = Persona(id,strCedula,strNombres,strApellidos,strCorreo,strTelefono,strDependencia,intEstado,strCargo)
        ingresos = PersonaModel.set_entidad(persona)
        
        if ingresos >= 1:
            return redirect(url_for('Persona_blueprint.home'))
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
            fila_afectada = PersonaModel.del_entidad(id)
            if fila_afectada == 1:
                return redirect(url_for('Persona_blueprint.home'))
            else:
                return jsonify({'menssage':"Ninguna persona ha sido eliminada"}),404
    except Exception as ex:
        return jsonify({'mesage':str(ex)}),500

@main.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    try:
        strCedula = request.form['strCedula']
        strNombres = request.form['strNombres']
        strApellidos = request.form['strApellidos']
        strCorreo = request.form['strCorreo']
        strTelefono = request.form['strTelefono']
        strDependencia = request.form['strDependencia']
        intEstado = request.form['intEstado']
        strCargo = request.form['strCargo']
        persona = Persona( id,strCedula,strNombres,strApellidos,strCorreo,strTelefono,strDependencia,intEstado,strCargo)
        ingresos = PersonaModel.up_Endidad(persona)
        if ingresos == 1:
            return redirect(url_for('Persona_blueprint.home'))
        else:
            return jsonify({'menssage':"Error al actualizar"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    