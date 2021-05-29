# import matplotlib.pyplot as plt
#
# pets=['Dog','Cat','Fish','Hamster','Rabbit']
# students=[8,11,6,4,1]
# colors=['red','green','blue','yellow','cyan']
#
# plt.bar(pets, students, color=colors)
#
# plt.xlabel('Pets')
# plt.ylabel('Students')
# plt.title('pets survey in class')
# plt.grid(axis='y')
#
# plt.show()







# import  matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# font_list=fm.findSystemFonts()
#
#
#
# #print(font_list)
# path=font_list[font_list.index('C:\\Windows\\Fonts\\malgun.ttf')]
# font_name = fm.FontProperties(fname=path, size=18).get_name()
# plt.rc('font', family=font_name)
#
# countries = ['조개나라','뇨니나라','음식나라','퐁이나라','종이나라']
# gold = [342, 321, 302, 432, 126]
# silver = [433, 458, 156, 384, 258]
# bronze = [145, 115, 218, 135, 498]
#
# bottom_silver = gold
# bottom_bronze = [a + b for a, b in zip(gold, silver)]
##
# fig, ax = plt.subplots()
# p1 = ax.bar(countries, gold, color='gold', label='Gold')
# p2= ax.bar(countries, silver, bottom=bottom_silver, label= 'Silver')
# p3= ax.bar(countries, bronze, bottom=bottom_bronze, label= 'Bronze')
#
# plt.xlabel('나라')
# plt.ylabel('메달 수')
# plt.title('3021년 만화 올림픽')
# plt.legend()
#
# ax.bar_label(p1, label_type='center')
# ax.bar_label(p2, label_type='center')
# ax.bar_label(p3, label_type='center')
# plt.show()



# import matplotlib.pyplot as plt
#
# countries = ['USA', 'GBR', "China", 'Russia', 'Germany']
# gold = [34, 53, 24, 54, 24]
# colors = ['red', 'green', 'blue', 'yellow', 'cyan']
# explode = [0, 0, 0, 0, 0]
#
# plt.pie(gold, explode=explode, labels=countries, colors=colors, autopct="%.1f%%")
# plt.title('medal')
# plt.show()