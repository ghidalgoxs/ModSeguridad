from flask import Blueprint,redirect,jsonify,request,url_for,session

# importar los models
from models.AsignaRolModel import AsignaRolModel
from models.entities.AsignaRol import AsignaRol
#from models.entities.AsignaRolCompleto import AsignaRolCompleto
main = Blueprint('AsignarRol_blueprint',__name__)

@main.route('/')
def home():
    try:
        if "username" in session:
            return AsignaRolModel.get_page()
        else:
            return redirect(url_for('Login_blueprint.home'))
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

#Ruta para ingreso   
@main.route('/add', methods=['POST'])
def add():
    try:
        idPersona = request.form.get('idPersona')
        idRol = request.form.get('idRol')
        intEstado = request.form['intEstado']
        asignaRol = AsignaRol(idPersona,idRol,intEstado)
        ingresos = AsignaRolModel.set_entidad(asignaRol)
        
        if ingresos >= 1:
            return redirect(url_for('AsignarRol_blueprint.home'))
        else:
            return jsonify({'menssage':"Error al insertar"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

@main.route('/delete/<int:idPersona>/<int:idRol>')
#@main.route('/delete', defaults={'idPersona': None})
def delete(idPersona,idRol):
    try:
        if idPersona is None and idRol is None:
            return jsonify({'menssage':"Id vacio"}),404
        else:
            fila_afectada = AsignaRolModel.del_entidad(idPersona,idRol)
            if fila_afectada == 1:
                return redirect(url_for('AsignarRol_blueprint.home'))
            else:
                return jsonify({'menssage':"Ninguna persona ha sido eliminada"}),404
    except Exception as ex:
        return jsonify({'mesage':str(ex)}),500

@main.route('/edit/<int:idPersona>', methods=['POST'])
def edit(idPersona):
    try:
        #idPersona = request.form.get('idPersona')
        idRol = request.form.get('idRol')
        intEstado = request.form['intEstado']
        asignarol = AsignaRol(idPersona,idRol,intEstado)
        ingresos = AsignaRolModel.up_Endidad(asignarol)
        if ingresos == 1:
            return redirect(url_for('AsignarRol_blueprint.home'))
        else:
            return jsonify({'menssage':"Error al actualizar"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    