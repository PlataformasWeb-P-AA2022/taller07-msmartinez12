from requests import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo from requests import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo2 = open("data/datos_jugadores.txt", "r")
registro2 = archivo2.readlines()
for r in registro2:
    club = r.split(";")[0]
    posicion = r.split(";")[1]
    dorsal = int(r.split(";")[2])
    nombre = r.split(";")[3].replace("\n", "")
    club1 = session.query(Club).filter_by(nombre=club).one()
    jugador = Jugador(nombre=nombre, dorsal=dorsal,posicion=posicion, club=club1)
    session.add(jugador)

session.commit()




