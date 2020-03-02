class View:
    #Contacto views
    def mostrar_contacto(self, contacto):
        print('****** Datos del contacto *****')
        print('Nombre:', contacto.nombre)
        print('Teléfono:', contacto.tel)
        print('Correo:', contacto.correo)
        print('Dirección:', contacto.dir)
        print('*******************************')

    def mostrar_contactos(self, contactos):
        print('********* Contactos ***********')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('********************************')

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'se ha agregado a la base de datos!')
    
    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'se ha borrado de la base de datos')
    
    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'se ha modificado correctamente!')
    
    def contacto_ya_existe(self, contacto):
        print('EL CONTACTO',contacto.id_contacto,'YA EXISTE EN LA BASE DE DATOS')
    
    def contacto_no_existe(self, id_contacto):
        print('EL CONTACTO',id_contacto,'NO EXISTE EN LA BASE DE DATOS')

    #Cita views
    def mostrar_cita(self, cita):
        print('****** Datos de la cita ******')
        print('ID:', cita.id_cita)
        print('Contacto:', cita.id_contacto)
        print('Lugar:', cita.lugar)
        print('Fecha:', cita.fecha)
        print('Hora:', cita.hora)
        print('Asunto:', cita.asunto)
        print('******************************')

    def mostrar_citas(self, citas):
        print('*********** Citas *************')
        for c in citas:
            print(c.id_cita, c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
        print('*******************************')

    def crear_cita(self, cita):
        print(cita.fecha,cita.asunto, 'se ha agregado a la base de datos!')
    
    def borrar_cita(self, cita):
        print(cita.fecha, cita.asunto, 'se ha borrado de la base de datos')
    
    def modificar_cita(self, cita_o, cita_n):
        print(cita_o.fecha, cita_o.asunto, 'se ha modificado correctamente!')
    
    def cita_ya_existe(self, cita):
        print(cita.id_cita,'YA EXISTE EN LA BASE DE DATOS')
    
    def cita_no_existe(self, id_cita):
        print(id_cita,'NO EXISTE EN LA BASE DE DATOS')

    #General views
    def start(self):
        print('Esto es un ejemplo sencillo de MVC')
    
    def end(self):
        print('Hasta la vista!')

    def menu(self):
        print('1. Agregar contacto')
        print('2. Buscar contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Agregar cita')
        print('9. Salir')
