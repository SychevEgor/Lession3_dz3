user_number = int(input('Введите чило'))
f1 = 1
f2 = 1
lst = [1,1]
for i in range(2,user_number):
    f_sum = f1 +f2
    f1 = f2
    f2 = f_sum
    lst.append(f2)
lst_revest = lst[:]
lst_revest.reverse()
for i in range(len(lst_revest)):
    lst_revest[i] =  lst_revest[i] * -1
lst_revest.append(0)
itog_lst = lst_revest + lst
print(itog_lst)