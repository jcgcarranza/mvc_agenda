from model.model import Model
from view.view import View

class Controller:

    #Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contacto controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if e:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
    
    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)
    
    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)

    #Cita controllers

    #General methods
    def insertar_contactos(self):
        self.agregar_contacto(1, 'Juan Perez', '464-123-1234','jp@gmail.com', 'Arteaga No. 5, Col. San Miguel, Salamanca')
        self.agregar_contacto(2, 'Ana Torres', '464-567-2342', 'at@ugto.mx', 'Sendero No. 17, Col. Revolución, Salamanca')
        self.agregar_contacto(3, 'Adriana Nuñez', '1234567890', 'an@gmail.com', 'Coco No. 11, Col. Linda Vista, Irapuato')

    def insertar_citas(self):
        pass

    def start(self):
        #Display a welcome message
        self.view.start()
        #Insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        #Show all contacts in DB
        self.leer_todos_contactos()
        self.leer_contactos_letra('a')

    def menu(self):
        #Display menu
        self.view.menu()
        o = input('Selecciona una opcion (1-9)')
        if o == '1':
            pass
        elif o == '2':
            pass
        elif o == '3':
            pass
        elif o == '9':
            self.view.end()
        else:
            self.view.opcion_no_valida()