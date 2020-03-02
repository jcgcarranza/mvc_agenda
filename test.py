from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller

""" contactos = []
c1 = Contacto(1, 'Juan Perez', '464-123-1234','jp@gmail.com', 'Arteaga No. 5, Col. San Miguel, Salamanca')
c2 = Contacto(2, 'Ana Torres', '464-567-2342', 'at@ugto.mx', 'Sendero No. 17, Col. Revolución, Salamanca')

t1 = Cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase de Sistemas de Información')
 """""" print(c2.id_contacto)
print(c2.nombre)
print(c2.tel)
print(c2.correo)
print(c2.dir) """

""" contactos.append(c1)
contactos.append(c2)
 """
""" t = input('Dame un nombre: ')

for c in contactos:
    if t.lower() == c.nombre.lower():
        print('Si esta')
        break
else:
    print('No esta')
 """

""" m = Model()
m.agregar_contacto(1, 'Juan Perez', '464-123-1234','jp@gmail.com', 'Arteaga No. 5, Col. San Miguel, Salamanca')
m.agregar_contacto(2, 'Ana Torres', '464-567-2342', 'at@ugto.mx', 'Sendero No. 17, Col. Revolución, Salamanca')
m.agregar_contacto(3, 'Adriana Nuñez', '1234567890', 'an@gmail.com', 'Coco No. 11, Col. Linda Vista, Irapuato')
s = m.leer_todos_contactos()
for c in s:
    print(c.nombre, c.tel)
 """
""" s = m.leer_contacto(2)
print(s.nombre) """
""" 
#m.actualizar_contacto(1, 'Sara Juarez', '1234-12312', 'gh@gmail.com', 'Sin numero en colonia')
m.actualizar_contacto(1, n_nombre = 'Hugo Belman')
s = m.leer_todos_contactos()
for c in s:
    print(c.nombre, c.tel)

s = m.leer_contactos_letra('a')
for c in s:
    print(c.nombre, c.tel)
 """
""" s = m.leer_contacto(2)
print(s.nombre) """

""" s = m.borrar_contacto(1)
print(s)
s = m.borrar_contacto(1)
print(s) """

""" m.agregar_contacto(3, 'Adriana Nuñez', '1234567890', 'an@gmail.com', 'Coco No. 11, Col. Linda Vista, Irapuato')

l = m.leer_contactos_letra('a')
for c in l:
    print(c.nombre)

l = m.leer_todos_contactos()
for c in l:
    print(c.nombre) """


""" m.agregar_cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase de Sistemas de Información')
m.agregar_cita(2, 2, 'Aula 102', '21-02-2020', '12:00', 'Clase de NLP')
m.agregar_cita(3, 1, 'Aula 104', '21-02-2020', '14:00', 'Clase de Minería de Datos')

l = m.leer_todas_citas()
for c in l:
    print(c.asunto)

print('********')
l = m.leer_citas_fecha('21-02-2020')
for c in l:
    print(c.fecha, c.hora, c.asunto)
print('********')
#m.borrar_contacto(1)
l = m.leer_todas_citas()
for c in l:
    print(c.fecha, c.hora, c.asunto)

v = View()
s = m.leer_todos_contactos()
v.mostrar_contactos(s)
c = m.leer_contacto(1)
v.mostrar_contacto(c)

f, c = m.borrar_contacto(1)
if f:
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)

s = m.leer_todos_contactos()
v.mostrar_contactos(s)
 """
cont = Controller()
cont.start()