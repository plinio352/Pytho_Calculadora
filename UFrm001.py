from form001 import *
import Dao001 as Dao


class UFrm(TFrm):

    def __init__(self):
        super().__init__()
        self.dao =  Dao.TDao()

    def ev001_click(self):
        super().ev001_click()
        self.dao.somar(self.edt001.get(), self.edt002.get())
        if len(self.dao.erro) == 0:
            self.lb001['text'] = f'A soma é: {self.dao.vlresult:,.4f}'
        else:
            self.edterro.insert(index=0, string=self.dao.erro)

    def ev002_click(self):
        super().ev002_click()
        self.dao.subtrair(self.edt001.get(), self.edt002.get())
        if len(self.dao.erro) == 0:
            self.lb001['text'] = f'A subtração é: {self.dao.vlresult:,.4f}'
        else:
            self.edterro.insert(index=0, string=self.dao.erro)

    def ev003_click(self):
        super().ev003_click()
        self.dao.multiplicar(self.edt001.get(), self.edt002.get())
        if len(self.dao.erro) == 0:
            self.lb001['text'] = f'A multiplicação é: {self.dao.vlresult:,.4f}'
        else:
            self.edterro.insert(index=0, string=self.dao.erro)

    def ev004_click(self):
        super().ev004_click()
        self.dao.dividir(self.edt001.get(), self.edt002.get())
        if len(self.dao.erro) == 0:
            self.lb001['text'] = f'A divisão é: {self.dao.vlresult:,.4f}'
        else:
            self.edterro.insert(index=0, string=self.dao.erro)

    def load(self):
        self.tela.mainloop()
