from flask import Flask
from config import config
from flask_cors import CORS

import os
from controllers import PersonaController, RolController, PermisoController, PadreController, AsignarRolController, AsignarPermisoController,UsuarioController,LoginController

# directorio donde esta nuestra aplicación para acceder a nuestro archivo
dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# rescribir el directorio y concatenarlo con las otras carpetas
dir = os.path.join(dir,'seguridad','views')

#inicializar flask para poder lanzar nuestra aplicación
app = Flask(__name__,template_folder=dir)

CORS(app)

#ejecutor
if __name__=='__main__':
    app.config.from_object(config['development'])
    #Blueprints
    app.register_blueprint(LoginController.main,url_prefix='/')
    app.register_blueprint(PersonaController.main,url_prefix='/seg/persona')
    app.register_blueprint(RolController.main,url_prefix='/seg/rol')
    app.register_blueprint(PermisoController.main,url_prefix='/seg/permiso')
    app.register_blueprint(PadreController.main,url_prefix='/seg/padre')
    app.register_blueprint(AsignarRolController.main,url_prefix='/seg/asignarrol')
    app.register_blueprint(AsignarPermisoController.main,url_prefix='/seg/asignarpermiso')
    app.register_blueprint(UsuarioController.main,url_prefix='/seg/usuario')
    
    app.run(port=4000)
    
