from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def temas(tema="dark"):
    dark = ["dark", "#323232", "#535353", "#1F1F1F", "#DEDEDE", "#F2F2F2"]
    if tema.lower() == dark[0]:
        return dark


def fontes(tamanho="12pt", fonte="SanSerif"):
    retorno = ("{} {}".format(tamanho, fonte))
    return retorno


def janelas(janela, cores="dark", nivel=1, fonte=fontes()):
    cor = temas(cores)
    if nivel == 1:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[1], cor[4], fonte))
    elif nivel == 2:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[2], cor[4], fonte))
    else:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[3], cor[4], fonte))
    janela.setStyleSheet(estilo)


def layouts(lay, margem=0, espaco=0):
    """"""
    lay.setMargin(margem)
    lay.setSpacing(espaco)


def quadros(quadro, cores="dark", nivel=1, fonte=fontes(), mx=0, my=0, tx=16777215, ty=16777215):
    cor = temas(cores)
    if nivel == 1:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[1], cor[4], fonte))
    elif nivel == 2:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[2], cor[4], fonte))
    else:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[3], cor[4], fonte))
    quadro.setStyleSheet(estilo)
    quadro.setMinimumSize(mx, my)
    quadro.setMaximumSize(tx, ty)


def botoes(botao, cores="dark", nivel=1, fonte=fontes(), mx=0, my=0, tx=16777215, ty=16777215, ti=(0, 0),
           px=0, py=0, borda=("10px", "outset", "1px", "None")):
    """"""
    cor = temas(cores)
    estilo_borda = ("border-radius: {}; border-style: {}; border-width: {}; border: {}".format(borda[0], borda[1],
                                                                                               borda[2], borda[3]))
    if nivel == 1:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[1], cor[4], fonte))
    elif nivel == 2:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[2], cor[4], fonte))
    else:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[3], cor[4], fonte))
    botao.setStyleSheet('QPushButton {' + str(estilo) + ';' + str(estilo_borda) + '}'
                        'QPushButton:hover {background-color:' + str(cor[3]) + '}')
    botao.setMinimumSize(mx, my)
    botao.setMaximumSize(tx, ty)
    if ti[0] == 0 and ti[1] == 0:
        largura = botao.width()
        altura = botao.height()
    else:
        largura = ti[0]
        altura = ti[1]
    botao.setIconSize(QSize(largura, altura))
    botao.move(px, py)


def textos(texto, cores="dark", nivel=1, fonte=fontes(), alin=Qt.AlignVCenter, px=0, py=0,
           mx=0, my=0, tx=16777215, ty=16777215):
    """"""
    cor = temas(cores)
    if nivel == 1:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[1], cor[4], fonte))
    elif nivel == 2:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[2], cor[4], fonte))
    else:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[3], cor[4], fonte))
    texto.setStyleSheet('QLabel {' + str(estilo) + '}')
    texto.setAlignment(alin)
    texto.move(px, py)
    texto.setMinimumSize(mx, my)
    texto.setMaximumSize(tx, ty)


def editar_texto(texto, cores="dark", nivel=1, fonte=fontes(), px=0, py=0, mx=0, my=0, tx=16777215, ty=16777215):
    """"""
    cor = temas(cores)
    if nivel == 1:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[1], cor[4], fonte))
    elif nivel == 2:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[2], cor[4], fonte))
    else:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[3], cor[4], fonte))
    texto.setStyleSheet('QLineEdit {' + str(estilo) + '}')
    texto.move(px, py)
    texto.setMinimumSize(mx, my)
    texto.setMaximumSize(tx, ty)


def combinacao(comb, cores="dark", nivel=1, fonte=fontes(), px=0, py=0, mx=0, my=0, tx=16777215, ty=16777215):
    """"""
    cor = temas(cores)
    if nivel == 1:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[1], cor[4], fonte))
    elif nivel == 2:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[2], cor[4], fonte))
    else:
        estilo = ('background-color:{}; color:{}; font:{}'.format(cor[3], cor[4], fonte))
    comb.setStyleSheet('QComboBox {' + str(estilo) + '}')
    comb.move(px, py)
    comb.setMinimumSize(mx, my)
    comb.setMaximumSize(tx, ty)


def tabelas(tab, cabecalho=("Nº", ""), tc=(0, 0), cores="dark", borda=("10px", "5px", "1px solid"),
            preencher=("5px", "5px"), rolagem=("14px", "14px"), margem=("0px", "21px", "0px", "21px"),
            cab=(True, False), editar=QAbstractItemView.NoEditTriggers, selecionar=QAbstractItemView.SelectRows):
    colunas = len(tc)
    tab.setColumnCount(colunas)
    tab.horizontalHeader().setStretchLastSection(True)
    tab.setEditTriggers(editar)
    tab.setSelectionBehavior(selecionar)
    tab.horizontalHeader().setVisible(cab[0])
    tab.verticalHeader().setVisible(cab[1])
    if tc[0] != 0 and tc[1] != 0:
        for num, valor in enumerate(tc):
            tab.setColumnWidth(num, valor)
    tab.setHorizontalHeaderLabels(cabecalho)
    cor = temas(cores)
    est_geral = ('background-color:{}; padding:{}; border-radius:{}; gridline-color:{}; border-bottom:{} {}'
                 .format(cor[3], borda[0], borda[1], cor[1], borda[2], cor[3]))
    est_item = ('border-color: {}; padding-left: {}; padding-right: {}; gridline-color: {}'
                .format(cor[1], preencher[0], preencher[1], cor[1]))
    est_sele = ('background-color:{}'.format(cor[2]))
    est_rolagem_h = ('border:{}; background:{}; height:{}; margin: {} {} {} {}; border-radius: {};'
                     .format("None", cor[1], rolagem[1], margem[0], margem[1], margem[2], margem[3], "0px"))
    est_rolagem_v = ('border:{}; background:{}; height:{}; margin: {} {} {} {}; border-radius: {};'
                     .format("None", cor[1], rolagem[0], margem[0], margem[1], margem[2], margem[3], "0px"))
    est_cabe = ('Background-color:{};max-width:{};border:{} {};border-style:{};border-bottom:{} {};border-right:{} {}'
                .format(cor[3], "30px", borda[2], cor[3], "None", borda[2], cor[3], borda[2], cor[3]))
    est_cabe_h = ('background-color:{};'.format(cor[4]))
    est_cabe_h_sele = ('border:{} {};background-color:{};padding:{};border-top-left-radius:{};'
                       'border-top-right-radius:{};'.format(borda[2], cor[3], cor[1], "3px", "7px", "7px"))
    est_cabe_v_sele = ('border: {} {}'.format(borda[2], cor[3]))

    tab.setStyleSheet('QTableWidget {' + str(est_geral) + '} QTableWidget::item{' + str(est_item) + '}'
                      'QTableWidget::item:selected {' + str(est_sele) + '}'
                      'QScrollBar:horizontal {' + str(est_rolagem_h) + '}'
                      'QScrollBar:vertical {' + str(est_rolagem_v) + '}'
                      'QHeaderView::section{' + str(est_cabe) + '}'
                      'QTableWidget::horizontalHeader {' + str(est_cabe_h) + '}'
                      'QHeaderView::section:horizontal {' + str(est_cabe_h_sele) + '}'
                      'QHeaderView::section:vertical {' + str(est_cabe_v_sele) + '}')

dark = ["dark", "#323232", "#535353", "#1F1F1F", "#DEDEDE", "#F2F2F2"]
