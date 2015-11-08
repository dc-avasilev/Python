Когда Антон прочитал «Войну и мир», ему стало интересно,
сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, 
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и 
выводить для каждого уникального слова в этой строке число его 
повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным.

 Sample Input 1:

a aa abC aa ac abc bcd a

Sample Output 1:

a 2
aa 2
ac 1
abc 2
bcd 1


Sample Input 2:

a A a

Sample Output 2:

a 3

# put your python code here
n='' #инициализация строки
n = str(input())
m = [] #инициализация списка
m.append([str(s.lower()) for s in n.split()]) 
d = {} #инициализация пустого словаря
li, lj = len(m), len(m[0])
for i in range(li):
    for j in range(lj):
        p = m[i][j]
        if p in d:
            d[p]+=1
        else:
            d[p] = 1
for key,value in d.items():
   print(key,value)
