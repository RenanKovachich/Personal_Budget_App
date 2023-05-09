# Valor total
Renda_mensal_apos_impostos = float(input("Renda mensal após impostos? : "))

# Porcentagens 50 | 30 | 20
obter_50_porcento = (50/100) * Renda_mensal_apos_impostos
obter_30_porcento = (30/100) * Renda_mensal_apos_impostos
obter_20_porcento = (20/100) * Renda_mensal_apos_impostos

print("============================================\nSeus números de 50% 30% 20% \n============================================\n")
print('Necessidades: R${:,.2f}'.format(obter_50_porcento))
print('Vontade: R${:,.2f}'.format(obter_30_porcento))
print('Economias e Planejamento: R${:,.2f}'.format(obter_20_porcento))
