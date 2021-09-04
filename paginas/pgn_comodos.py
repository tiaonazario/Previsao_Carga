from PySide2.QtWidgets import *
from biblioteca import *
import sys


class JComodo(QMainWindow):
    def __init__(self):
        super(JComodo, self).__init__()
        self.setMinimumSize(850, 430)
        ###############################################################################################################
        # PARTE PRINCIPAL
        # -------------------------------------------------------------------------------------------------------------
        self.wdg_comodo = QWidget(self)
        self.lay_comodo = QGridLayout(self)
        self.wdg_comodo.setLayout(self.lay_comodo)

        self.setCentralWidget(self.wdg_comodo)
        self.formatar_principal()
        ###############################################################################################################
        # CONTROLES
        # -------------------------------------------------------------------------------------------------------------
        self.txt_titulo = QLabel("INSERIR CÔMODOS", self)
        self.txt_tipo = QLabel("Tipo de cômodo", self)
        self.cbn_tipo = QComboBox(self)
        self.txt_descricao = QLabel("Descrição", self)
        self.edt_descricao = QLineEdit(self)
        self.txt_comprimento = QLabel("Comprimento", self)
        self.edt_comprimento = QLineEdit(self)
        self.txt_largura = QLabel("Largura", self)
        self.edt_largura = QLineEdit(self)
        self.bot_adicionar = QPushButton("Adicionar", self)
        self.bot_limpar = QPushButton("Limpar", self)

        self.lay_comodo.addWidget(self.txt_titulo, 0, 0, 1, 2)
        self.lay_comodo.addWidget(self.txt_tipo, 1, 0, 1, 1)
        self.lay_comodo.addWidget(self.cbn_tipo, 1, 1, 1, 1)
        self.lay_comodo.addWidget(self.txt_descricao, 2, 0, 1, 1)
        self.lay_comodo.addWidget(self.edt_descricao, 2, 1, 1, 1)
        self.lay_comodo.addWidget(self.txt_comprimento, 3, 0, 1, 1)
        self.lay_comodo.addWidget(self.edt_comprimento, 3, 1, 1, 1)
        self.lay_comodo.addWidget(self.txt_largura, 4, 0, 1, 1)
        self.lay_comodo.addWidget(self.edt_largura, 4, 1, 1, 1)
        self.lay_comodo.addWidget(self.bot_adicionar, 5, 0, 1, 1)
        self.lay_comodo.addWidget(self.bot_limpar, 5, 1, 1, 1)

        self.formatar_controles()
        ###############################################################################################################
        # LISTA DE COMODOS
        # -------------------------------------------------------------------------------------------------------------
        self.txt_lista = QLabel("LISTA DE CÔMODOS", self)
        self.tab_comodos = QTableWidget(self)
        self.bot_calcular = QPushButton("Calcular", self)
        self.bot_excluir = QPushButton("Excluir", self)

        self.lay_comodo.addWidget(self.txt_lista, 0, 2, 1, 4)
        self.lay_comodo.addWidget(self.tab_comodos, 1, 2, 6, 4)
        self.lay_comodo.addWidget(self.bot_calcular, 7, 3, 1, 1)
        self.lay_comodo.addWidget(self.bot_excluir, 7, 4, 1, 1)

        self.formatar_lista()
        ###############################################################################################################
        self.mtz_comodos = []

        self.comandos()

    def formatar_principal(self):
        janelas(self.wdg_comodo)
        layouts(self.lay_comodo, 10, 10)

    def formatar_controles(self):
        textos(self.txt_titulo, alin=Qt.AlignCenter, mx=400, my=40, tx=400, ty=40)
        textos(self.txt_tipo, mx=150, my=30, tx=150, ty=30)
        combinacao(self.cbn_tipo, nivel=3, mx=250, my=30, tx=250, ty=30)
        self.cbn_tipo.addItems(tipos_comodos())
        textos(self.txt_descricao, mx=150, my=30, tx=150, ty=30)
        editar_texto(self.edt_descricao, nivel=3, mx=250, my=30, tx=250, ty=30)
        textos(self.txt_comprimento, mx=150, my=30, tx=150, ty=30)
        editar_texto(self.edt_comprimento, nivel=3, mx=250, my=30, tx=250, ty=30)
        textos(self.txt_largura, mx=150, my=30, tx=150, ty=30)
        editar_texto(self.edt_largura, nivel=3, mx=250, my=30, tx=250, ty=30)
        botoes(self.bot_adicionar, nivel=2, mx=100, my=40, tx=100, ty=40)
        botoes(self.bot_limpar, nivel=2, mx=100, my=40, tx=100, ty=40)

    def formatar_lista(self):
        textos(self.txt_lista, alin=Qt.AlignCenter, my=40, ty=40)

        lst_cabecalho = ("Nº", "TIPO", "DESCRIÇÃO", "COMPRIMENTO", "LARGURA", "ÁREA", "PERIMETRO")
        tam_cabecalho = (40, 150, 350, 150, 150, 100, 150)
        tabelas(self.tab_comodos, cabecalho=lst_cabecalho, tc=tam_cabecalho)

        botoes(self.bot_calcular, nivel=2, mx=100, my=40, tx=100, ty=40)
        botoes(self.bot_excluir, nivel=2, mx=100, my=40, tx=100, ty=40)

    def adicionar(self):
        try:
            var_linhas = self.tab_comodos.rowCount()
            var_tipo = self.cbn_tipo.itemText(self.cbn_tipo.currentIndex())
            var_descricao = self.edt_descricao.text()
            var_comprimento = self.edt_comprimento.text()
            var_largura = self.edt_largura.text()

            var_comodo = Comodo(var_comprimento, var_largura, var_tipo)
            lst_var = var_comodo.mtz_comodo(var_linhas + 1, var_descricao)

            self.tab_comodos.insertRow(var_linhas)
            for num, item in enumerate(lst_var):
                self.tab_comodos.setItem(var_linhas, num, QTableWidgetItem(str(item)))

            self.limpar()
        except Exception:
            print("ERRO")

    def limpar(self):
        self.cbn_tipo.setCurrentText("...")
        self.edt_descricao.setText("")
        self.edt_comprimento.setText("")
        self.edt_largura.setText("")

    def calcular(self):
        var_ql = self.tab_comodos.rowCount()  # quantidade de linhas
        var_qc = self.tab_comodos.columnCount()  # quantidade de colunas
        """| id | Tipo | descrição | comprimento | largura | área | perimetro |  |  |  |"""
        mtz_comodos = []
        for linha in range(0, var_ql):
            lst_linhas = []
            for coluna in range(0, var_qc):
                valor = valor_tabela(self.tab_comodos, linha, coluna)
                lst_linhas += [valor]
            mtz_comodos += [lst_linhas]
        self.mtz_comodos = mtz_comodos

    def matriz_comodos(self):
        return self.mtz_comodos

    def excluir(self):
        try:
            var_linha_selecionada = self.tab_comodos.currentRow()
            self.tab_comodos.removeRow(var_linha_selecionada)
            print(var_linha_selecionada)
        except Exception:
            print("Provavelmente você não selecionou uma linha")

    def comandos(self):
        self.bot_adicionar.clicked.connect(self.adicionar)
        self.bot_limpar.clicked.connect(self.limpar)
        self.bot_calcular.clicked.connect(self.calcular)
        self.bot_excluir.clicked.connect(self.excluir)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = JComodo()
    jan.show()
    sys.exit(app.exec_())
