# No dia 25
loadPage1 = 13
loadPage2 = 17
exitPage = 20
# calcula hora max de carregamento
maxLoadPage = 0
if loadPage1 > loadPage2:
    maxLoadPage = loadPage1
# calcuma tempo da sessao no dia 25
tempSes25 = exitPage - maxLoadPage

# No dia 26
loadPage1 = 13
loadPage2 = 15
loadPage3 = 17
exitPage1 = 21
exitPage2 = 22
# calcula hora max de carregamento
maxLoadPage = 0
if loadPage1 > loadPage2:
    maxLoadPage = loadPage1
if maxLoadPage > loadPage3:
    pass
else:
    maxLoadPage = loadPage3
# calcula hora min de fechamento
minExitPage = 0
if exitPage1 > exitPage2:
    minExitPage = exitPage2
# calcuma tempo da sessao no dia 26
tempSes26 = minExitPage - maxLoadPage

# calcula tempo de sessão média
tempSesAvg = (tempSes25 + tempSes26) / 2
print('O tempo de sessão média nos dias 25 e 26 de março é de {} h.'.format(tempSesAvg))