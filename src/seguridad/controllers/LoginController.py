from flask import Blueprint,redirect,jsonify,request,url_for,render_template,flash,session
# importar los models
from models.LoginModel import LoginModel
from models.entities.Usuario import Usuario

main = Blueprint('Login_blueprint',__name__)



@main.route('/')
def home():
    return render_template('login.html')

@main.route('/login',methods = ['GET','POST'])
def login():
    try:
        if request.method=='POST':
            usuario = Usuario(0,0,request.form['username'],request.form['password'])
            logeado = LoginModel.login_page(usuario)
            if logeado is not None:
                if logeado.__hash__(logeado.password,request.form['password']):
                    session["username"] = logeado.username
                    session["idPersona"] = logeado.idPersona
                    return LoginModel.get_roles()                    
                else:
                    flash("Password invalido .....")   
                    return redirect(url_for('Login_blueprint.home')) 
            else:
                flash("Usuario no encontrado .....")   
                return redirect(url_for('Login_blueprint.home')) 

        else:
            return redirect(url_for('Login_blueprint.home'))

    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500


@main.route('/permiso/<int:id>',methods = ['GET','POST'])
def permiso(id):
    try:
        if request.method=='GET':
            return LoginModel.get_permisos(id)                    
        else:
            return redirect(url_for('Login_blueprint.home')) 
        
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500


@main.route('/logout')
def logout():
    if "username" in session:
        session.pop("username")
        return redirect(url_for('Login_blueprint.home'))
