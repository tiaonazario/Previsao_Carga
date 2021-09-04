from PySide2.QtWidgets import *
from biblioteca import *
from paginas.pgn_comodos import *
from paginas.pgn_cargas import *
import sys


class Janela(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Janela, self).__init__(*args, **kwargs)
        ###############################################################################################################
        # JANELA PRINCIPAL
        # -------------------------------------------------------------------------------------------------------------
        self.setMinimumSize(900, 500)
        # Remover titulo e barra de menus minimizar, maximilizar e fechar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.wdg_janela = QWidget(self)
        self.setCentralWidget(self.wdg_janela)

        self.lay_janela = QVBoxLayout(self)
        self.wdg_janela.setLayout(self.lay_janela)

        self.formatar_janela()
        ###############################################################################################################
        # JANELA - PARTE SUPERIOR
        # -------------------------------------------------------------------------------------------------------------
        self.frm_superior = QFrame(self)
        self.lay_superior = QGridLayout(self)
        self.frm_superior.setLayout(self.lay_superior)

        self.bot_barra = QPushButton(QIcon("icones/barras.png"), "", self)
        self.txt_titulo_janela = QLabel("Previsão de Cargas", self)
        self.bot_minimizar = QPushButton(
            QIcon("icones/minimizar.png"), "", self)
        self.bot_maximilizar = QPushButton(
            QIcon("icones/maximilizar.png"), "", self)
        self.bot_fechar = QPushButton(QIcon("icones/fechar.png"), "", self)
        self.frm_status = QFrame(self)

        self.lay_superior.addWidget(self.bot_barra, 0, 0, 2, 1)
        self.lay_superior.addWidget(self.txt_titulo_janela, 0, 1)
        self.lay_superior.addWidget(self.bot_minimizar, 0, 2)
        self.lay_superior.addWidget(self.bot_maximilizar, 0, 3)
        self.lay_superior.addWidget(self.bot_fechar, 0, 4)
        self.lay_superior.addWidget(self.frm_status, 1, 1, 1, 4)

        self.formatar_superior()
        ###############################################################################################################
        # JANELA - CENTRO
        # -------------------------------------------------------------------------------------------------------------
        self.frm_centro = QFrame(self)
        self.lay_centro = QHBoxLayout(self)
        self.frm_centro.setLayout(self.lay_centro)

        self.frm_barra_lateral = QFrame(self)
        self.lay_barra_lateral = QVBoxLayout(self)
        self.frm_barra_lateral.setLayout(self.lay_barra_lateral)

        self.bot_comodos = QPushButton(QIcon("icones/comodo.png"), "", self)
        self.bot_cargas = QPushButton(QIcon("icones/cargas.png"), "", self)
        self.frm_oculto = QFrame(self)

        self.lay_barra_lateral.addWidget(self.bot_comodos)
        self.lay_barra_lateral.addWidget(self.bot_cargas)
        self.lay_barra_lateral.addWidget(self.frm_oculto)

        self.stw_paginas = QStackedWidget(self)
        self.pgn_comodo = JComodo()
        self.pgn_cargas = JCargas()

        self.stw_paginas.addWidget(self.pgn_comodo.wdg_comodo)
        self.stw_paginas.addWidget(self.pgn_cargas.wdg_cargas)

        self.lay_centro.addWidget(self.frm_barra_lateral)
        self.lay_centro.addWidget(self.stw_paginas)

        self.formatar_centro()
        ###############################################################################################################
        # JANELA - INFERIOR
        # -------------------------------------------------------------------------------------------------------------
        self.frm_inferior = QFrame(self)
        self.lay_inferior = QHBoxLayout(self)
        self.frm_inferior.setLayout(self.lay_inferior)

        self.formatar_inferior()
        ###############################################################################################################
        self.lay_janela.addWidget(self.frm_superior)
        self.lay_janela.addWidget(self.frm_centro)
        self.lay_janela.addWidget(self.frm_inferior)

        self.comandos()

    def formatar_janela(self):
        janelas(self.wdg_janela)
        layouts(self.lay_janela)

    def formatar_superior(self):
        quadros(self.frm_superior, nivel=2, my=50, ty=50)
        layouts(self.lay_superior)

        botoes(self.bot_barra, nivel=2, mx=50,
               my=50, tx=50, ty=50, ti=(30, 30))
        textos(self.txt_titulo_janela, nivel=2)
        botoes(self.bot_minimizar, nivel=2, mx=40,
               my=30, tx=40, ty=30, ti=(20, 20))
        botoes(self.bot_maximilizar, nivel=2, mx=40,
               my=30, tx=40, ty=30, ti=(20, 20))
        botoes(self.bot_fechar, nivel=2, mx=40,
               my=30, tx=40, ty=30, ti=(20, 20))
        quadros(self.frm_status, nivel=3, my=20, ty=20)

    def formatar_centro(self):
        quadros(self.frm_centro)
        layouts(self.lay_centro)

        quadros(self.frm_barra_lateral, nivel=2, mx=50, tx=50)
        layouts(self.lay_barra_lateral)

        botoes(self.bot_comodos, nivel=2, mx=50, my=50, ty=50, ti=(40, 40))
        botoes(self.bot_cargas, nivel=2, mx=50, my=50, ty=50, ti=(40, 40))

    def formatar_inferior(self):
        quadros(self.frm_inferior, nivel=2, my=20, ty=20)
        layouts(self.lay_inferior)

    def duplo_clique(self, event):
        if status() == 0:
            print('Janela MAXIMILIZADA')
        else:
            print('Janela DESMAXIMILIZADA')
        maximilizar(self)

    def mover_janela(self, event):
        if status() == 1:
            maximilizar(self)

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Clique do mouse: CLIQUE À ESQUERDA')
        if event.buttons() == Qt.RightButton:
            print('Clique do mouse: CLIQUE À DIREITA')
        if event.buttons() == Qt.MidButton:
            print('Clique do mouse: BOTÃO DO MEIO')

    def selecionar_paginas(self, indice):
        self.stw_paginas.setCurrentIndex(indice)

    def cargas(self):
        self.selecionar_paginas(1)
        try:
            mtz_comodos = self.pgn_comodo.matriz_comodos()
            self.pgn_cargas.mtz_comodos = mtz_comodos
            self.pgn_cargas.carregar()
        except Exception:
            print("ERRO ao carregar os dados da previsão de carga")

    def comandos(self):
        self.txt_titulo_janela.mouseMoveEvent = self.mover_janela
        self.txt_titulo_janela.mouseDoubleClickEvent = self.duplo_clique
        self.bot_barra.clicked.connect(
            lambda: alternar(self, self.frm_barra_lateral, 150))
        self.bot_minimizar.clicked.connect(self.showMinimized)
        self.bot_maximilizar.clicked.connect(lambda: maximilizar(self))
        self.bot_fechar.clicked.connect(self.close)
        self.bot_comodos.clicked.connect(lambda: self.selecionar_paginas(0))
        self.bot_cargas.clicked.connect(self.cargas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    car = Janela()
    car.show()
    sys.exit(app.exec_())
