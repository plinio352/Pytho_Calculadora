import tkinter as formulario


class TFrm:

    def ev001_click(self):
        self.lb001['text'] = 'Plinio Pereira'
        self.lb001['background'] = 'orange'

    def ev002_click(self):
        pass

    def ev003_click(self):
        pass

    def ev004_click(self):
        pass

    def __init__(self):
        self.tela = formulario.Tk()
        self.tela.title('Tela 001')
        self.tela.geometry("300x230+050+150")
        self.tela['background'] = 'gray'

        self.lb001 = formulario.Label(self.tela, text='Resultado de operação!')
        self.lb001.place(x=50, y=20, width=200)

        self.edt001 = formulario.Entry(self.tela)
        self.edt001.place(x=50, y=60, width=50)

        self.edt002 = formulario.Entry(self.tela)
        self.edt002.place(x=110, y=60, width=50)

        self.edterro = formulario.Entry(self.tela, textvariable='erro')
        self.edterro.place(x=1, y=210, width=300)

        self.btn001 = formulario.Button(self.tela, width="10", text="Somar", command=self.ev001_click)
        self.btn001.place(x=50, y=90)

        self.btn002 = formulario.Button(self.tela, width="10", text="Subtrair", command=self.ev002_click)
        self.btn002.place(x=50, y=120)

        self.btn003 = formulario.Button(self.tela, width="10", text="Multiplicar", command=self.ev003_click)
        self.btn003.place(x=50, y=150)

        self.btn004 = formulario.Button(self.tela, width="10", text="Dividir", command=self.ev004_click)
        self.btn004.place(x=50, y=180)

