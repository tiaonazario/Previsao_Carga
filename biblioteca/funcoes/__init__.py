from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sqlite3


status_janela = 0


def maximilizar(parametro):
    """"""
    global status_janela
    if status_janela == 0:
        parametro.showMaximized()
        status_janela = 1
    else:
        status_janela = 0
        parametro.showNormal()


def status():
    return status_janela


def alternar(parametro, frame, max_largura):
    """"""
    # pegar a largura atual
    largura = frame.width()
    padrao = 50
    # setar a largura desejada
    if largura == 50:
        largura_estendida = max_largura
    else:
        largura_estendida = padrao
    # animação
    parametro.animacao = QPropertyAnimation(frame, b"minimumWidth")
    parametro.animacao.setDuration(400)
    parametro.animacao.setStartValue(largura)
    parametro.animacao.setEndValue(largura_estendida)
    parametro.animacao.setEasingCurve(QEasingCurve.InOutQuart)
    parametro.animacao.start()


def valor_tabela(tabela, linha=0, coluna=0):
    valor = tabela.item(linha, coluna).text()
    return valor


def lampadas(area=1):
    dividir_area = ((area - 6) // 4) * 60
    if dividir_area < 0:
        dividir_area = 0
    pot_lamp = 100 + dividir_area
    return pot_lamp


def carregar_dados(tabela):
    conexao = sqlite3.connect("dados/bd_comodos.db")
    query = "SELECT * FROM Comodos"
    resultado = conexao.execute(query)
    tabela.setRowCount(0)
    for linha, item in enumerate(resultado):
        tabela.insertRow(linha)
        for coluna, dados in enumerate(item):
            tabela.setItem(linha, coluna, QTableWidgetItem(str(dados)))
