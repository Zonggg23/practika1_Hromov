//Этот пример используется для превращения каждой первой буквы символов строки в прописную букву. Он работает со строкой из одного или нескольких символов и будет полезен при анализе текста или записи данных в файл и т.п.//
def capitalize(String):
    return String.title()
capitalize("shop") # [Shop]
capitalize("python programming") # [Python Programming]
capitalize("how are you!") # [How Are You!]
