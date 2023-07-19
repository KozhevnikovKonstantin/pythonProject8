per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
TKB = per_cent['ТКБ']*money/100
SKB = per_cent['СКБ']*money/100
VTB = per_cent['ВТБ']*money/100
SBER = per_cent['СБЕР']*money/100
per_list = [TKB,SKB,VTB,SBER]
print(per_list)
print("Максимальная сумма, которую вы можете заработать — "+str(max(per_list)))