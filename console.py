titulo = ["DESCRIÇÃO", "Nº LÂMPADAS", "P.U. LÂMPADAS", "P.T. LÂMPADAS", "TUG - 100 VA", "TUG - 650 VA", "P.T. TUG`S"]
linha = 120 * "-"
print(linha)
print('|{:^118}|'.format("PREVISÃO DE CARGAS"))
print(linha)
print('|{:^26}|{:^13}|{:^15}|{:^15}|{:^14}|{:^14}|{:^15}|'.format(*titulo))
print(linha)
