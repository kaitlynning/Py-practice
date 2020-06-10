def f(rows):
  for x in range(rows):
    if x == 0 or x == rows-1:
        print('*'*rows) 
    else:
        print('*'+ ' '*(rows-2) + '*')
f(rows)
f(5)
f(6)

'''

空心正方形
****
*  *
*  *
****
*****
*   *
*   *
*   *
*****
******
*    *
*    *
*    *
*    *
******

'''
