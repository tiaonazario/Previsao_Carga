from math import ceil


class Comodo:
    def __init__(self, comprimento, largura, tipo):
        self.comp = comprimento
        self.larg = largura
        self.tipo = tipo

    def area(self, mostrar=False):
        a = float(self.comp) * float(self.larg)
        if mostrar is True:
            print("Área:\t\t\t\t{}".format(a))
        return a

    def perimetro(self, mostrar=False):
        p = (2 * float(self.comp)) + (2 * float(self.larg))
        if mostrar is True:
            print("Perimetro:\t\t\t{}".format(p))
        return p

    def mtz_comodo(self, numero, descricao, mostar=False):
        mtz = [numero, self.tipo, descricao, self.comp, self.larg, self.area(), self.perimetro()]

        if mostar is True:
            titulo = ["Nº", "TIPO", "DESCRIÇÃO", "COMPRIMENTO", "LARGURA", "ÁREA", "PERIMETRO"]
            linha = 91 * "-"
            print(linha)
            print('|{:^89}|'.format("CARACTERISTICAS FÍSICAS"))
            print(linha)
            print('|{:^4}|{:^15}|{:^25}|{:^13}|{:^9}|{:^6}|{:^11}|'.format(*titulo))
            print(linha)
            print('|{:^4}|{:^15}|{:^25}|{:^13}|{:^9}|{:^6}|{:^11}|'.format(*mtz))
            print(linha)

        return mtz


class Iluminacao(Comodo):
    def __init__(self, comprimento, largura, tipo):
        super(Iluminacao, self).__init__(comprimento, largura, tipo)

    def potencia(self, mostrar=False):
        area = self.area()
        if area < 6:
            pot = 100
        else:
            pot = 100 + (((area - 6) // 4) * 60)
        if mostrar is True:
            print("Potência:\t\t\t{}".format(pot))
        return pot

    def quantidade(self, potencia_unitaria, mostrar=False):
        qtd = self.potencia() / potencia_unitaria
        qtd = ceil(qtd)
        if mostrar is True:
            print("Nº Pontos:\t{}".format(qtd))
        return qtd


class TUG(Comodo):
    def __init__(self, comprimento, largura, tipo):
        super(TUG, self).__init__(comprimento, largura, tipo)

    def quantidade(self, mostrar=False):
        tipo = self.tipo
        area = self.area()
        perimetro = self.perimetro()
        tipo = tipo.lower()
        if tipo == "comum":
            para = 5
        else:
            para = 3.5
        if area < 6:
            if tipo == "comum":
                qtd = [1, 0, 100]
            else:
                qtd = [0, 1, 650]
        else:
            q = ceil(perimetro / para)
            if tipo == "comum":
                qtd = [q, 0, q * 100]
            else:
                if q > 3:
                    q1 = q - 3
                    pot = (q1 * 100) + (3 * 650)
                    qtd = [q1, 3, pot]
                else:
                    qtd = [0, q, q * 650]

        if mostrar is True:
            print("Nº 100 VA:\t{}\nNº 650 VA:\t{}\nP.T. (VA):\t{}".format(qtd[0], qtd[1], qtd[2]))
        return qtd


class Cargas(Comodo):
    def __init__(self, comprimento, largura, tipo):
        super(Cargas, self).__init__(comprimento, largura, tipo)

    def mtz_cargas(self, numero, descricao="", mostrar=False):
        ilum = Iluminacao(self.comp, self.larg, self.tipo)
        tom = TUG(self.comp, self.larg, self.tipo)
        pl = ilum.potencia()
        t = tom.quantidade()
        tab = [numero, descricao, "", "", pl, t[0], t[1], t[2], "", ""]
        if mostrar is True:
            titulo = ["Nº", "DESCRIÇÃO", "P.U. LAMP.", "Nº LAMP.", "P.T. LÂMP.", "TUG - 100 VA", "TUG - 600 VA",
                      "P.T. TUG", "TUE - APARELHO", "POT. TUE"]
            linha = 138 * "-"
            print(linha)
            print('|{:^136}|'.format("PREVISÃO DE CARGAS"))
            print(linha)
            print('|{:^4}|{:^25}|{:^12}|{:^10}|{:^12}|{:^14}|{:^14}|{:^10}|{:^16}|{:^10}|'.format(*titulo))
            print(linha)
            print('|{:^4}|{:^25}|{:^12}|{:^10}|{:^12}|{:^14}|{:^14}|{:^10}|{:^16}|{:^10}|'.format(*tab))
            print(linha)
        return tab
