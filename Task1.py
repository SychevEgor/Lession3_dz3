lst = [2, 3, 4, 5, 6]
lst_result = []
for i in range(len(lst)//2):
      lst_result.append(lst[i] * lst[-i-1])
if len(lst) % 2 != 0:
      m = len(lst) //2
      lst_result.append(lst[m]*lst[m])

      print(lst[-i+3])
print(lst_result)
