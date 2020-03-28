def delete_starting_evens(lst):
#While loops 符合條件了才認為是真，才可以執行以下程式碼
#check at least 1 element by len(lst); check 1 element is ood by mod(%）
  while (len(lst) > 0 and lst[0] % 2 == 0):
#if both are True, slice off 1 element by lst = lst[1:]
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

'''
#if顧名思義就是如果怎樣，那就怎樣
#while True表示永遠為真，不管是什麼條件都會向下執行

[11, 12, 15]
[]

'''

