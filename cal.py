import calendar
cal=calendar.Calendar()

# 0-понедельник
# 1-вторник
# 2-среда
# 3-четверг
# 4-пятница
year=2016
days=[1,3]
kanikulu=[
[4,11,2016],
[29,12,2016],
[30,12,2016],
[31,12,2016],
[1,1,2017],
[2,1,2017],
[3,1,2017],
[4,1,2017],
[5,1,2017],
[6,1,2017],
[7,1,2017],
[8,1,2017],
[2,5,2017],
[9,5,2017],
[28,5,2017],
[29,5,2017],
[30,5,2017],
[31,5,2017],
]

themes=[[ 'Голоса синтезатора из банков клавишных,  хроматических ударных, деревянно-духовых инструментов',[1,2,3]],
		[ 'Паттерны  народной, современной и популярной музыки и их редактирование',[4,5,6]],
		[ 'Секвенсер синтезатора',[9,12,23]],
		[ 'Музыкальная грамота: интервалы в пределах октавы, аккорды и их обращения, тональности, хроматическая гамма и др.',[8,11,14,15,22,30,36,48,52,58]],
		[ 'Тональные функции гармонии',[24,37,59]],
		[ 'Строение музыкальной фактуры: мелодия и бас',[25,38,60]],
		[ 'Элементарная классификация тембров',[26,39,61]],
		[ 'Гармония, фактура и тембр в формообразовании',[27,40,62]],
		[ 'Простые формы, вариации и рондо',[28,41,63]],
		[ 'Освоение различных игровых приемов, связанных с артикуляцией, динамикой. применением двухголосия в одной руке',[7,10,13,13,17,29,42]],
		[ 'Чтение с листа',[18,31,43,53]],
		[ 'Игра в ансамбле',[19,32,44,54]],
		[ 'Подбор по слуху',[20,33,45,55]],
		[ 'Импровизация',[21,34,46,56]],
		[ 'Развитие навыков электронной аранжировки и исполнения музыки',[16,35,47,49,57,64,67,68,69,70]],
		[ 'Репетиции на сцене и выступления',[50,51,65,66,71,72]]]

day_themes=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

d=0
c=1
for month in [9,10,11,12]:
	for day in cal.itermonthdays2(year,month):
		if day[1] in days:
			if day[0]!=0:
				text=''
				if not ([day[0],month,year] in kanikulu):
					# text=' - каникулы'
					for th in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
						if c in themes[th][1]:
							# themes[th][0]=themes[th][0]+' '+str(day[0])+'.'+str(month)+'.'+str(year)+'('+str(c)+'), '
							day_themes[th].append(str(str(day[0])+'.'+str(month)+'.'+str(year)))#+'('+str(c)+')'))
							d=d+1
					# print(c,'-',day[0],'.',month,'.',year,text)
					c=c+1

year=2017

for month in [1,2,3,4,5]:
	for day in cal.itermonthdays2(year,month):
		if day[1] in days:
			if day[0]!=0:
				text=''
				if not ([day[0],month,year] in kanikulu):
					# text=' - каникулы'
					for th in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
						if c in themes[th][1]:
							# themes[th][0]=themes[th][0]+' '+str(day[0])+'.'+str(month)+'.'+str(year)+'('+str(c)+'), '
							day_themes[th].append(str(str(day[0])+'.'+str(month)+'.'+str(year)))#+'('+str(c)+')'))
							d=d+1
					# print(c,'-',day[0],'.',month,'.',year,text)
					c=c+1

for th in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
	# print(themes[th][0])
	# print(', '.join(day_themes[th]))
	print('{0:30}	{1:50}'.format(themes[th][0],(', '.join(day_themes[th])),str(th+1)))

# print(day_themes)


print('Всего часов: ',d)