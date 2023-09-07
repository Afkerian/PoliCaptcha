import configparser
import os



def cargar_configuracion():
    # Obtener la ruta del directorio actual donde se encuentra este archivo (cargar_configuracion.py)
    conf_dir = os.path.dirname(os.path.abspath(__file__))


    # Obtener la ruta completa del archivo de configuración (config.properties)
    config_file = os.path.join(conf_dir, 'config.properties')

    config = configparser.ConfigParser()
    config.read(config_file)

    #print('\n\n\n CONFIGURACION: \n\n', config, conf_dir, config_file, sep='\n')

    return config