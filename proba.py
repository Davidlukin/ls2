# # # # # # # # # # # # dict={'name1':'alexsei',
# # # # # # # # # # # #       'name2':'Misha',
# # # # # # # # # # # #       'name3':'Lionid'}
# # # # # # # # # # # # print(dict['name1'])
# # # # # # # # # # # # dict['Misha'] = 'name4'
# # # # # # # # # # # # del dict['name1']
# # # # # # # # # # # # if 'Misha' in dict:
# # # # # # # # # # # #     print(dict)
# # # # # # # # # # # # print('Всего в адресной книге {0} штук'.format(len(dict)))
# # # # # # # # # # # # for name, lastname in dict.items():
# # # # # # # # # # # #     print('имя {0} и фамилия {1}'.format(name, lastname))
# # # # # # # # # # # #     help(dict)
# # # # # # # # # # # spisok=['mango','banan','ogyrec']
# # # # # # # # # # # print(spisok[0::])
# # # # # # # # # aer='_$_$_'
# # # # # # # # # bric=['kanada', 'Russia','dfdfdf']
# # # # # # # # # # 'Russia' in bric
# # # # # # # # # # bri=bric.copy()
# # # # # # # # # # print(bri)
# # # # # # # # # # bri.add('franc')
# # # # # # # # # # print(bric.remove('Russia'))
# # # # # # # # #
# # # # # # # # # print(aer.join(bric))
# # # # # # # # class person:
# # # # # # # #     def neme (self):
# # # # # # # #         print("привет я игорь")
# # # # # # # #
# # # # # # # # p = person()
# # # # # # # # p.neme()
# # # # # # # class person:
# # # # # # #     def __init__(self,name):
# # # # # # #         self.name=name
# # # # # # #     def neme(self):
# # # # # # #         print("Привет меня зовут",self.name)
# # # # # # #
# # # # # # # p=person('Шыг')
# # # # # # # p.neme()
# # # # # # class robot:
# # # # # #     population = 0
# # # # # #     def __init__(self,name):
# # # # # #         self.name = name
# # # # # #         print("На данный момент у нас {0} роботов ".format(self.name))
# # # # # #         robot.population+=1
# # # # # #     def __del_ (self):
# # # # # #         print('Я уничтожился {0}'.format(self.name))
# # # # # #         robot.population-=1
# # # # # #         if robot.population == 0:
# # # # # #             print('Последний робот был {0}'.format(self.name))
# # # # # #     def her(self):
# # # # # #         ''' ПРиветствие роботов
# # # # # #         Да они это могут'''
# # # # # #         print('Мои хозяева называют меня {0}'.format(self.name))
# # # # # #     def howmany(self):
# # # # # #         print('Нас {0}'.format(robot.population))
# # # # # #
# # # # # # lastrob=robot('kiki')
# # # # # # lastr=robot('kikl')
# # # # # # lastrob.her()
# # # # # class Schoolmemeber:
# # # # #     def __init__(self,name,age):
# # # # #         self.name=name
# # # # #         self.age=age
# # # # #         print('Создан SchooklMember {0}'.format(self.name))
# # # # #     def tell (self):
# # # # #         print('Имя {0} возрост {1}'.format(self.name,self.age),end=" ")
# # # # # class Teacher(Schoolmemeber):
# # # # #     def __init__(self,name,age,salary):
# # # # #         Schoolmemeber.__init__(self,name,age)
# # # # #         self.salary=salary
# # # # #         print("Созда учитель".format(self.name))
# # # # #     def tell(self):
# # # # #         Schoolmemeber.tell(self)
# # # # #         print('Зарплата {}'.format(self.salary))
# # # # # class student(Schoolmemeber):
# # # # #         def __init__(self, name,age,marks):
# # # # #             Schoolmemeber.__init__(self, name, age)
# # # # #             self.marks=marks
# # # # #             print('Создан студент {0}'.format(self.name))
# # # # #         def tell(self):
# # # # #             Schoolmemeber.tell(self)
# # # # #             print('Оценки'.format(self.marks))
# # # # #
# # # # # p = student ('vbvbv',15,12)
# # # # # p1 = Teacher("egor",15,1001)
# # # # # members=[p,p1]
# # # # # for member in members:
# # # # #     member.tell()
# # # # def reversit(text):
# # # #      return text[::-1]
# # # #      print(text)
# # # # def i_polindroma(text):
# # # #     return text == reversit(text)
# # # # somtihin = input('Ведите текст')
# # # # reversit('ghbf')
# # # infor='''Программировать очень весело и полезно
# # #          но гулят тоже нужно но не много
# # #          те вссе хорошо
# # #
# # # '''
# # # f = open('imfo.txt','w')
# # # f.write(infor)
# # # f.close()
# # # f1 = open('imfo.txt', 'r')
# # # while True:
# # #     line = f1.readline()
# # #     if len(line) == 10:
# # #         break
# # #     print(line,end='')
# # #
# # # f1.close()
# #
# # list=[2,3,4,5]
# # list = [i*2 for i in list if i==5]
# # print(list)
# def last(ls,*i1):
#     total=0
#     for i in i1:
#         total+=pow(i,ls)
#     return total
# print(last(3,2))