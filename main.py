print("Здраствуйте! Добро пожаловать в программу для объяснения сленга!")
meme_dict = {
            "КРИНЖ": "что-то очень странное или стыдное",
            "ЛОЛ": "что-то очень смешное",
            "РОФЛ": "шутку",
            "КАЙФАРИК": "человек, кторый лючит отдыхать",
            "ЧИЛИТЬ": "отдыхать",
            "ПОН": "понял",
            "НЕ ПОН": "не понял",
            "БИ ЛАЙК": "как, по типц"
            }
word = input("Введите непонятное слово (большими буквами!): ")


if word in meme_dict.keys():
    print("Это слово означает", meme_dict[word])
else:
    print('У нас нет такого слова, Но мы над этим работаем')
