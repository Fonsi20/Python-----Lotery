# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import gi
from random import randint

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class pantallaInicio:

    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('ventanaInicio.glade')


        # Objetos
        self.venprincipal = b.get_object('ventanaprincipal')
        self.venQuin = b.get_object('ventanaQuiniela')
        self.venPrim = b.get_object('ventanaPrimitiva')
        self.btnsalir = b.get_object('btnsalir')
        self.btnsalQuin = b.get_object('btnSalirQui')
        self.btnsalPrim = b.get_object('btnSalirPri')
        self.btncprimi = b.get_object('btnprimitiva')
        self.btnquini = b.get_object('btnquiniela')
        self.PrimiResu = b.get_object('lblResultadoPrimi')
        self.PrimiRein = b.get_object('lblReintegro')
        self.QuinResu = b.get_object('lblResultadosQuin')

        self.r1 = b.get_object('r1')
        self.r2 = b.get_object('r2')
        self.r3 = b.get_object('r3')
        self.r4 = b.get_object('r4')
        self.r5 = b.get_object('r5')
        self.r6 = b.get_object('r6')
        self.r7 = b.get_object('r7')
        self.r8 = b.get_object('r8')
        self.r9 = b.get_object('r9')
        self.r10 = b.get_object('r10')
        self.r11 = b.get_object('r11')
        self.r12 = b.get_object('r12')
        self.r13 = b.get_object('r13')
        self.r14 = b.get_object('r14')
        self.r15 = b.get_object('r15')

        self.listaQuin = {self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7,
                          self.r8, self.r9, self.r9, self.r10, self.r11, self.r12, self.r13,
                          self.r14, self.r15}


        # Diccionario
        # Eventos
        dic = {'on_ventanaprincipal_destroy': self.salir,
               'on_btnsalir_clicked': self.salir,
               'on_ventanaPrimitiva_destroy': self.salPrim,
               'on_btnSalirPri_clicked': self.salPrim,
               'on_ventanaQuiniela_destroy': self.salQuin,
               'on_btnSalirQui_clicked': self.salQuin,
               'on_btnprimitiva_clicked': self.primi,
               'on_btnquiniela_clicked': self.quini,
               }

        b.connect_signals(dic)
        self.venprincipal.show()


    def primi(self, widget, data=None):
        self.venPrim.show()
        lista = []
        reintegro = randint(0, 9)
        while len(lista) != 6:
            numero = randint(1, 49)
            if numero not in lista:
                lista.append(numero)
        lista.sort()
        self.PrimiResu.set_text(str(lista))
        self.PrimiRein.set_text(str(reintegro))



    def quini(self, widget, data=None):
        self.venQuin.show()
        for object in self.listaQuin:
            object.set_text(self.generaRandon())


    def generaRandon(null):
        randN = randint(1, 3)
        string = ''
        if randN == 1:
            string = '1 ---------------'
        elif randN == 2:
            string = '------- X -------'
        else:
            string = '--------------- 2'
        return string

    def salir(self, widget, data=None):
        Gtk.main_quit()


    def salQuin(self, widget, data=None):
        self.venQuin.hide()


    def salPrim(self, widget, data=None):
        self.venPrim.hide()


if __name__ == '__main__':
    main = pantallaInicio()
    Gtk.main()
