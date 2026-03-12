import math
import random
import datetime
import statistics as st
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#entradas
capital = float(input('capital inicial:'))
aporte = float(input('aporte mensal:'))
meses = int(input('prazo (meses):'))
cdi_anual = float(input('cdi anual(%):'))/100
perc_cdb = float(input('percentual do cdi(%):')) /100
perc_lci = float(input('percentual do lci(%):')) /100
taxa_fii = float(input('rentabilidade mensal FII(%):')) /100
meta = float(input('meta fiananceira(R$):'))

#conversão cdi
cdi_mensal = math.pow((1+cdi_anual), 1/12) -1

#total investido
total_investido = capital + (aporte * meses)

#cdb
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses) + (aporte * meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)
                                                     
#lci
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci),meses)+(aporte * meses))

#poupança
taxa_poupança = 0.005
montante_poupança = (capital * math.pow((1+taxa_poupança), meses)+(aporte * meses))

#fii - simulaçãoes
montante_fii = (capital*math.pow((1 + taxa_fii), meses) + ( aporte * meses))

vari1= random.uniform(-0.03, 0.03)
vari2= random.uniform(-0.03, 0.03)
vari3= random.uniform(-0.03, 0.03)
vari4= random.uniform(-0.03, 0.03)
vari5= random.uniform(-0.03, 0.03)

simu1= montante_fii +(montante_fii * vari1)
simu2= montante_fii +(montante_fii * vari2)
simu3= montante_fii +(montante_fii * vari3)
simu4= montante_fii +(montante_fii * vari4)
simu5= montante_fii +(montante_fii * vari5)

media_fii = st.mean((simu1, simu2, simu3, simu4, simu5))
mediana_fii = st.median((simu1, simu2, simu3, simu4, simu5))
dp_fii = st.stdev((simu1, simu2, simu3, simu4, simu5))

#FORMATAÇÃO MONETÁRIA
data_simulacao = datetime.date.today()
data_resgate = data_simulacao + datetime.timedelta(days = meses * 30)

# META
meta_atingida = media_fii >= meta
#blocos
bloco_cdb = int(montante_cdb_liquido / 1000)
bloco_lci = int(montante_lci / 1000)
bloco_poupança = int(montante_poupança / 1000)
bloco_fii = int(montante_fii / 1000)

#saidas
print('=' * 40)
print(" PyInvest - Simulador de Inestimentos")
print('=' * 40)
print(f'Data da simulação: {data_simulacao.strftime('%d/%m/%Y')}')
print(f'Data de resgate: {data_resgate.strftime('%d/%m/%Y')} ')
print('=' * 40)
print('           ')
print(f'Total investido: {locale.currency(total_investido, grouping=True)}')
print('           ')
print("--- RESULTADOS FINANCEIROS ---")
print(f'CDB: {locale.currency(montante_cdb_liquido, grouping=True)}')
print(f"{'█' * bloco_cdb}")
print('          ')
print(f'LCI: {locale.currency(montante_lci, grouping=True)}')
print(f"{'█' * bloco_lci}")
print("     ")
print(f'Poupança: {locale.currency(montante_poupança, grouping=True)}')
print(f'{'█' * bloco_poupança}')
print('       ')
print(f'FII (Média): {locale.currency(media_fii, grouping=True)}')
print(f'{'█' * bloco_fii}')
print('         ')
print('--- ESTATISTICAS FII ---')
print(f'Mediana: {locale.currency(mediana_fii, grouping=True)}')
print(f'Desvio padrão: {locale.currency(dp_fii, grouping=True)}')
print('           ')
print(f'Meta atingida? {media_fii >= meta}')
print('=' * 40)