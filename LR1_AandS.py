import datetime

def cleanString(incomingString): #Для чистки текста от лишних символов
	key = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
	for word in incomingString:
		for j in word:
			if (j.lower() not in key):
				incomingString = incomingString.replace(j, ' ')
	return incomingString

def sorting(words): #сортировка вставками
	for i in range(len(words)):
		j = i - 1 
		key = words[i].lower()
		while words[j][0].lower() > key[0] and j >= 0:
			words[j + 1] = words[j]
			j -= 1
		words[j + 1] = key
	return words

def cntBukv(words): #аналитика кол-ва букв
	for bukva in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
		cnt = 0
		for i in range(len(words)):
			if (words[i][0] == bukva):
				cnt += 1
		fAnalysis.write(bukva + " = " + str(cnt) + "\n")

def cntWords(words): #Подсчёт кол-ва слов, игнорируя числа
	cnt = len(words) 
	for i in range(len(words)):
		for j in '1234567890':
			if (words[i][0] == str(j)):
				cnt -= 1
	return str(cnt)
		
def result(words): #Запись результата в файл
	previous_letter = None
	for word in words:
		if previous_letter is None or word[0].lower() != previous_letter:
			fRes.write("\n")
		previous_letter = word[0].lower()
		fRes.write(word + " ") 


		#РАБОТА С ФАЙЛАМИ
#Открываем файлы
f = open('original20000.txt', 'r', encoding='utf-8') # Текст
fRes = open('result.txt', 'w+', encoding='utf-8') # Результат сортировки
fAnalysis = open('analysis.txt', 'w+', encoding='utf-8') # Анализ работы с текстом
	
textFromF = f.read() # Текст из файла f
textFromF = cleanString(textFromF) # Удаление лишних символов
words = textFromF.split() # Лист слов

#Запись в файл аналитики
fAnalysis.write("Введённый текст: \n" + textFromF + "\n")
fAnalysis.write("\nВариант 15: кириллица, по алфавиту, по возрастанию, игнорировать числа, сортировка вставками")
fAnalysis.write("\nКоличество слов: " + cntWords(words) + "\n")
fAnalysis.write("Статистика слов на каждую букву алфавита: \n")
cntBukv(words)

start = datetime.datetime.now()
print('Время старта: ' + str(start))
sorting(words) #Сортировка
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))

print('Время работы: ' + str(finish - start))

result(words)  #Запись результата в файл
	
fRes.close
f.close
fAnalysis.close