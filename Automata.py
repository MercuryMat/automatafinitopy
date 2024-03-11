import tkinter as tk
import time

class MaquinaExpendedora:
    def __init__(self):
        self.estado_actual = 'Esperando'
        self.cantidad_total = 0
        self.precio_snack = {
            500: 'Frutiño de aguila',
            1000: 'Pin pop Ferxxo',
            1500: 'Bianchi explosion caramelo',
            2000: 'Huevos no me olvides',
            2500: 'Doritos',
            25000: 'Bandeja paisa'
        }
        self.producto_seleccionado = None
    
    def recibir_moneda(self, moneda):
        if self.estado_actual == 'Esperando':
            if moneda in [0, 1]:
                self.cantidad_total += 500 if moneda == 0 else 1000
                self.estado_actual = 'Recibiendo'
                lbl_estado.config(text=self.estado_actual)
            else:
                print('Ingrese una moneda válida (0 para 500 y 1 para 1000).')

        elif self.estado_actual == 'Recibiendo':
            if moneda in [0, 1]:
                self.cantidad_total += 500 if moneda == 0 else 1000
            else:
                print('Ingrese una moneda válida (0 para 500 y 1 para 1000).')
        lbl_dinero.config(text='Ha ingresado: ' + str(self.cantidad_total))

    def vender_snack(self):
        precio = self.producto_seleccionado

        if precio <= self.cantidad_total:
            self.cantidad_total -= precio
            self.estado_actual = 'Vendiendo'
            lbl_estado.config(text=self.estado_actual)
            if self.cantidad_total > 0:
                self.devolver_cambio()
            root.update()
            time.sleep(1)
            self.estado_actual = 'Esperando'
            self.producto_seleccionado = None
            lbl_estado.config(text=self.estado_actual)
            lbl_dinero.config(text='Ingresa una moneda')

        else:
            lbl_estado.config(maquina.estado_actual)

    def devolver_cambio(self):
        lbl_dinero.config(text='Cambio devuelto: ' + str(self.cantidad_total))
        root.update()
        time.sleep(1)
        self.cantidad_total = 0

def reset():
    lbl_dinero.config(text='Ingresa una moneda')

maquina = MaquinaExpendedora()

def insertar_moneda(moneda):
    maquina.recibir_moneda(moneda)

def seleccionar_producto(precio):
    maquina.producto_seleccionado = precio
    if maquina.cantidad_total < maquina.producto_seleccionado:
        lbl_estado.config(text='Faltan ' + str(maquina.producto_seleccionado-maquina.cantidad_total) + ' para comprar ' + maquina.precio_snack[precio])
    else:
        maquina.vender_snack()

root = tk.Tk()
root.title('Maquina Expendedora')

title_container = tk.Frame(root)
title_container.pack()

lbl_titulo = tk.Label(title_container, text='Bienvenido a la Maquina Expendedora')
lbl_titulo.pack()

btn_container = tk.Frame(root)
btn_container.pack()

btn_a1 = tk.Button(btn_container, text='Frutiño de aguila', command=lambda: seleccionar_producto(500))
btn_a1.pack()

btn_a2 = tk.Button(btn_container, text='Pin pop Ferxxo', command=lambda: seleccionar_producto(1000))
btn_a2.pack()

btn_a3 = tk.Button(btn_container, text='Bianchi explosion caramelo', command=lambda: seleccionar_producto(1500))
btn_a3.pack()

btn_a4 = tk.Button(btn_container, text='Huevos no me olvides', command=lambda: seleccionar_producto(2000))
btn_a4.pack()

btn_a5 = tk.Button(btn_container, text='Doritos', command=lambda: seleccionar_producto(2500))
btn_a5.pack()

btn_a6 = tk.Button(btn_container, text='Bandeja paisa', command=lambda: seleccionar_producto(25000))
btn_a6.pack()

moneda_container =tk.Frame(root)
moneda_container.pack()

lbl_moneda = tk.Label(moneda_container, text='Inserte una moneda (500 o 1000):')
lbl_moneda.pack()

btn_moneda0 = tk.Button(moneda_container, text='500', command=lambda: insertar_moneda(0))
btn_moneda0.pack(side=tk.LEFT)

btn_moneda1 = tk.Button(moneda_container, text='1000', command=lambda: insertar_moneda(1))
btn_moneda1.pack(side=tk.RIGHT)

estado_container = tk.Frame()
estado_container.pack()

lbl_estado = tk.Label(estado_container, text=maquina.estado_actual)
lbl_estado.pack()

lbl_dinero = tk.Label(estado_container, text='Ingrese una moneda')
lbl_dinero.pack()

root.mainloop()
