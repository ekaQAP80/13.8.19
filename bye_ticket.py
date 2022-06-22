num_tic   = 0 #количество билетов
age_list   = [] #список значений цены от возраста
sum_order  = 0 #сумма заказа
price_1   = 0
price_2   = 990
price_3   = 1390
t = ''
t1 = 0

#                 количество билетов
while True:
    try:
       num_tic = int(input('введите количество билетов - '))
       if len(str(num_tic)) > 3 or num_tic < 0: print ('количество билетов не может быть отрицательным\n и нельзя купить больше 999 шт')
       else:
           break
    except ValueError:
        print("вводите только цифры, пожалуйста")

print()
#print('кол бил - ', num_tic)
#                  ввод возраста
for i in range(num_tic):
    while True:
        try:
            t = "введите возраст %d участника - " % (i + 1)
            t1 = float(input(t))
            if  t1 > 100  or t1 < 7:
                print('для участников младше 7 или старше 100 лет будет организована дополнительная конференция. следите за новостями')
            else:
                if t1 <= 18:
                    age_list.append(price_1)
                    print("цена билета -", price_1)
                elif 18 < t1 <= 25:
                    age_list.append(price_2)
                    print("цена билета -", price_2)
                elif 25 < t1:
                    age_list.append(price_3)
                    print("цена билета -", price_3)
                break
        except ValueError:
            print("вводите только цифры, пожалуйста")

#                 расчет стоимости заказа

#print(num_tic)
if num_tic < 3:
    sum_order = sum(age_list)
    print()
    print('сумма к оплате за %d билета -' % (num_tic), sum_order)
elif num_tic >= 3:
    sum_order = sum(age_list) - sum(age_list)/100*10
    print()
    print("сумма к оплате за %d билета с учетом 10%% скидки -" % (num_tic), sum_order)
