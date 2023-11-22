from flask import Blueprint,redirect,render_template,jsonify,request,url_for,session

# importar los models
from models.AsignaPermisoModel import AsignaPermisoModel
from models.entities.AsignaPermiso import AsignaPermiso
#from models.entities.AsignaRolCompleto import AsignaRolCompleto
main = Blueprint('AsignarPermiso_blueprint',__name__)

@main.route('/')
def home():
    try:
        if "username" in session:
            return AsignaPermisoModel.get_page()
        else:
            return redirect(url_for('Login_blueprint.home'))
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

#Ruta para ingreso   
@main.route('/add', methods=['POST'])
def add():
    try:
        idRol = request.form.get('idRol')
        idPermiso = request.form.get('idPermiso')
        if (idRol is not None) and (idPermiso is not None) :
            bitIngreso = request.form.get('bitIngreso')
            bitModificar = request.form.get('bitModificar')
            bitEliminar = request.form.get('bitEliminar')
            if not bitIngreso:
                bitIngreso = 0
            if not bitModificar:
                bitModificar = 0
            if not bitEliminar:
                bitEliminar = 0
            intEstado = request.form['intEstado']
            asignaPermiso = AsignaPermiso(idRol,idPermiso,bitIngreso,bitModificar,bitEliminar,intEstado)
            ingresos = AsignaPermisoModel.set_entidad(asignaPermiso)
            
            if ingresos >= 1:
                return redirect(url_for('AsignarPermiso_blueprint.home'))
            else:
                return jsonify({'menssage':"Error al insertar"}),500
        else:
            return redirect(url_for('AsignarPermiso_blueprint.home'))
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

@main.route('/delete/<int:idRol>/<int:idPermiso>')
def delete(idRol,idPermiso):
    try:
        if idRol is None and idPermiso is None:
            return jsonify({'menssage':"Id vacio"}),404
        else:
            fila_afectada = AsignaPermisoModel.del_entidad(idRol,idPermiso)
            if fila_afectada == 1:
                return redirect(url_for('AsignarPermiso_blueprint.home'))
            else:
                return jsonify({'menssage':"Ninguna persona ha sido eliminada"}),404
    except Exception as ex:
        return jsonify({'mesage':str(ex)}),500

@main.route('/edit/<int:idRol>/<int:idPermiso>', methods=['POST'])
def edit(idRol,idPermiso):
    try:
        bitIngreso = request.form.get('bitIngreso')
        bitModificar = request.form.get('bitModificar')
        bitEliminar = request.form.get('bitEliminar')
        if not bitIngreso:
            bitIngreso = 0
        else:
            bitIngreso = 1
        if not bitModificar:
            bitModificar = 0
        else:
            bitModificar = 1
        if not bitEliminar:
            bitEliminar = 0
        else:
            bitEliminar = 1
        intEstado = request.form['intEstado']
        asignaPermiso = AsignaPermiso(idRol,idPermiso,bitIngreso,bitModificar,bitEliminar,intEstado)
        ingresos = AsignaPermisoModel.up_Endidad(asignaPermiso)
        
        if ingresos == 1:
            return redirect(url_for('AsignarPermiso_blueprint.home'))
        else:
            return jsonify({'menssage':"Error al actualizar"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    