import json
from evento import Evento
from review import Review
from ruta import Ruta
from ubicacion import Ubicación
from usuario import Usuario

#Eventos
ubi_FNE = Ubicación('Estadio 23 de Agosto','Av. El Exodo y Santa Barbara',[-24.198357356157036, -65.29088570436872])
fne = Evento('Eleccion Reina 2023','Maria Becerra','regueton',ubi_FNE,'2023/9/29 20:00','2023/9/29 23:00','La nena de Argentina es la artista elegida para brindar el espectaculo en la fiesta de los estudiantes','/Users/danaa.sosa/Downloads/Tour Musical/assets/imagenes/FNE_2023.png')

ubi_moura = Ubicación('El Teatrino','Aniceto Latorre 1211',[-24.772960840169283, -65.41788491968977])
moura = Evento('Fede Moura interpreta virus','Fede Moura','rock y pop argentino',ubi_moura,'2023/8/31 20:30','2023/8/31 22:00','El show que marca el camino de la carrera solista del cantante y compositor Fede Moura','/Users/danaa.sosa/Downloads/Tour Musical/assets/imagenes/moura-sla.png')

ubi_queen = Ubicación('Teatro Provincial Saravia','Zuviria 70',[-24.788836272584476, -65.40949706016616])
queen = Evento('Experiencia Queen','queen','rock',ubi_queen,'2023/7/23 21:00','2023/7/23 23:00','Vivi una verdadera experiencia queen en vivo','/Users/danaa.sosa/Downloads/Tour Musical/assets/imagenes/experienciaqueeen_juj.png')

ubi_portezuelo = Ubicación('Centro Cultural Martin Fierro','Av. Illia 450',[-24.1686587873673, -65.32013554669801])
portezuelo = Evento('Gira 2023','Los del Portezuelo','folclore',ubi_portezuelo,'2023/8/26 21:00','2023/8/26 23:00','Una noche con sorpresas y un espectaculo inolvidable','/Users/danaa.sosa/Downloads/Tour Musical/assets/imagenes/los del portezuelo.png')

ubi_charco = Ubicación('Galpones Recuperados MTK','Urquiza y Argañaraz',[-24.177067672583316, -65.31881440251816])
charco = Evento('Cruzando el Charco Jujuy','Cruzando el Charco','pop', ubi_charco,'2023/7/28 23:00','2023/7/29 01:00','La banda platense vuelve a nuestra provincia con un show imperdible', '/Users/danaa.sosa/Downloads/Tour Musical/assets/imagenes/cruzando el charco.png')

#Usuarios
user1 = Usuario('Dana','Sosa')
user2 = Usuario('David','Serapio')

#Agregar destinos a los usuarios
eventos_jujuy = [fne,portezuelo,charco]
for evento in eventos_jujuy:
    user1.agregar_evento_historial(evento)

eventos_salta = [moura,queen]
for evento in eventos_salta:
    user2.agregar_evento_historial(evento)

#Rutas
eventos_jujuyID = [fne.id_evento,portezuelo.id_evento,charco.id_evento]
ruta_jujuy = Ruta('San Salvador de Jujuy',eventos_jujuyID)

#Reviews
review1 = Review(4377307744,4377322416,4,'Un show imperdible','positiva')

#Archivos Json
data_ubi = {}
data_ubi['Ubicaciones'] = []
data_ubi['Ubicaciones'].append(ubi_charco.to_json())
data_ubi['Ubicaciones'].append(ubi_FNE.to_json())
data_ubi['Ubicaciones'].append(ubi_moura.to_json())
data_ubi['Ubicaciones'].append(ubi_portezuelo.to_json())
data_ubi['Ubicaciones'].append(ubi_queen.to_json())

with open('/Users/danaa.sosa/Downloads/Tour Musical/data/ubicacion.json','w') as file:
    json.dump(data_ubi, file, indent=4)


data_eventos = {}
data_eventos['Eventos'] = []
data_eventos['Eventos'].append(charco.to_json())
data_eventos['Eventos'].append(fne.to_json())
data_eventos['Eventos'].append(moura.to_json())
data_eventos['Eventos'].append(portezuelo.to_json())
data_eventos['Eventos'].append(queen.to_json())

with open('/Users/danaa.sosa/Downloads/Tour Musical/data/eventos.json','w') as file:
    json.dump(data_eventos, file, indent=4)

    
data_user = {}
data_user['Usuarios'] = []
data_user['Usuarios'].append(user1.to_json())
data_user['Usuarios'].append(user2.to_json())

with open('/Users/danaa.sosa/Downloads/Tour Musical/data/usuarios.json','w') as file:
    json.dump(data_user, file, indent=4)

data_rutas = {}
data_rutas['Rutas'] = []
data_rutas['Rutas'].append(ruta_jujuy.to_json())

with open('/Users/danaa.sosa/Downloads/Tour Musical/data/ruta.json','w') as file:
    json.dump(data_rutas, file, indent=4)


data_review = {}
data_review['Reviews'] = []
data_review['Reviews'].append(review1.to_json())

with open('/Users/danaa.sosa/Downloads/Tour Musical/data/reviews.json','w') as file:
    json.dump(data_review, file, indent=4)