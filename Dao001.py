class TDao():
    def __init__(self):
        self.vlresult: float = 0
        self.erro: str

    def somar(self, a: str, b: str):
        try:
            self.erro = ''
            self.vlresult = float(a.replace(',', '.')) + float(b.replace(',', '.'))
        except ValueError as e:
            self.erro = 'Informação invalida! '+ str(e)

    def subtrair(self, a: str, b: str):
        try:
            self.erro = ''
            self.vlresult = float(a.replace(',', '.')) - float(b.replace(',', '.'))
        except ValueError as e:
            self.erro = 'Informação invalida! ' + str(e)

    def multiplicar(self, a: str, b: str):
        try:
            self.erro = ''
            self.vlresult = float(a.replace(',', '.')) * float(b.replace(',', '.'))
        except ValueError as e:
            self.erro = 'Informação invalida! ' + str(e)

    def dividir(self, a: str, b: str):
        try:
            self.erro = ''
            self.vlresult = float(a.replace(',', '.')) / float(b.replace(',', '.'))
        except ValueError as e:
            self.erro = 'Informação invalida! ' + str(e)

