from PySide2.QtWidgets import *
from biblioteca import *
import sys


class JCargas(QMainWindow):
    def __init__(self):
        super(JCargas, self).__init__()
        self.setMinimumSize(850, 430)
        ###############################################################################################################
        # PARTE PRINCIPAL
        # -------------------------------------------------------------------------------------------------------------
        self.wdg_cargas = QWidget(self)
        self.lay_cargas = QGridLayout(self)
        self.wdg_cargas.setLayout(self.lay_cargas)

        self.setCentralWidget(self.wdg_cargas)
        ###############################################################################################################
        # TABELA DE PREVISÃO DE CARGA INSTALADA
        # -------------------------------------------------------------------------------------------------------------
        self.tab_cargas = QTableWidget(self)
        self.bot_carregar = QPushButton("Carregar", self)

        self.lay_cargas.addWidget(self.tab_cargas, 0, 0, 1, 4)
        self.lay_cargas.addWidget(self.bot_carregar, 1, 2, 1, 1)

        self.formatar()
        ###############################################################################################################
        self.comandos()

        self.mtz_comodos = []

    def formatar(self):
        janelas(self.wdg_cargas)
        layouts(self.lay_cargas, 10, 10)

        lst_cabecalho = ("Nº", "DESCRIÇÃO", "P.U. LAMP.", "Nº LAMP.", "P.T. LÂMP.", "TUG - 100 VA", "TUG - 600 VA",
                         "P.T. TUG", "TUE - APARELHO", "POT. TUE")
        tam_cabecalho = (40, 200, 130, 120, 120, 120, 120, 120, 150, 120)
        tabelas(self.tab_cargas, cabecalho=lst_cabecalho, tc=tam_cabecalho, editar=QAbstractItemView.DoubleClicked)

        botoes(self.bot_carregar, nivel=2, mx=100, my=40, tx=100, ty=40)

    def carregar(self):
        try:
            self.tbl_cargas = []
            mtz = self.mtz_comodos
            for lin, i_l in enumerate(mtz):
                mtz_cg = Cargas(mtz[lin][3], mtz[lin][4], mtz[lin][1])
                lst_cargas = mtz_cg.mtz_cargas(mtz[lin][0], mtz[lin][2])

                self.tbl_cargas += [lst_cargas]

            self.colocar_tabela()

        except Exception:
            print("ERRO EM CARREGAR A MATRIZ DE DADOS DOS CÔMODOS")

    def colocar_tabela(self):
        try:
            self.tab_cargas.setRowCount(0)
            for linha, il in enumerate(self.tbl_cargas):
                self.tab_cargas.insertRow(linha)
                for c, ic in enumerate(il):
                    self.tab_cargas.setItem(linha, c, QTableWidgetItem(str(self.tbl_cargas[linha][c])))
        except Exception:
            print("ERRO EM CARREGAR A MATRIZ DE DADOS DOS CÔMODOS")

    def comandos(self):
        self.bot_carregar.clicked.connect(self.carregar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = JCargas()
    jan.show()
    sys.exit(app.exec_())
