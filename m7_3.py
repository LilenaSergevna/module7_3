import re

class WordsFinder:
    file_names=None
    def __init__(self, *file):
       self.file_names=file
    def get_all_words (self):
        all_words ={}
        punkt=[',', '.', '=', '!', '?', ';', ':', ' - ']
        for one_file in self.file_names:
            with open(one_file, encoding='utf-8') as file:
                all_words [one_file]=list()
                for stroka in file:           #тут получили только стринг
                    str_my=stroka.lower()
                    #str_my = re.sub('[.,=!?;:-]', '', str_my)
                    for znak in punkt:
                        if znak in str_my:
                            str_my= str_my.replace(znak,'')
                    tmp=str_my.split()
                    for i in tmp:
                        all_words [one_file].append(i)
        return all_words

    def find(self,word):
        rez_dict={}

        for p in dict(self.get_all_words()).items():  #перебор словаря
            x = 0
            #print(p[0])
            for i in p[1]:
                #print(i)
                x=x+1
                #print(x)
                if i==word.lower():
                    rez_dict[p[0]]=x
                    break;
        return rez_dict

    def count(self,word):
        rez_dict={}

        for p in dict(self.get_all_words()).items():  #перебор словаря
            x = 0
            #print(p[0])
            for i in p[1]:
                #print(i)
                if i==word.lower():
                    #print(i)
                    x=x+1
                rez_dict[p[0]]=x
        return rez_dict
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего