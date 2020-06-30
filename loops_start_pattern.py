# 1)
for i in range(4):  # range start with 0(zero).
    for j in range(i):
        print("*", end='')  # end The end key of print function will set the string that                              needs to be appended when printing is done
    print()
'''
*
**
***
****'''

# 2)
n = 5
for i in range(n):  # range start with 0(zero).
    for j in range(n):
        print("*", end='')
    n = n - 1
    print()
'''
****
***
**
*  '''


# 3)
n = 7
k = 7
for i in range(n):
    for j in range(k):
        print(' ', end='')
    for m in range(i):
        print("*", end='')
    k = k - 1
    print()
'''
      *
     **
    ***
   ****
  *****
 ******
'''

# 4)
n = 7
k = 7
for i in range(n):
    for j in range(k):
        print(' ', end='')
    for m in range(i):
        print("*", end=' ')
    k = k - 1
    print()

'''
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
'''

# 5)
n = 7
k = 7
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for m in range(k):
        print('*', end=' ')
    print()
    k = k - 1

'''
* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
'''

# 6)
n = 7
k = 7

for i in range(n):
    for m in range(k):
        print('*', end=' ')
    for j in range(i):
        print(' ', end='')
    k = k - 1
    print()


'''
* * * * * * * 
* * * * * *  
* * * * *   
* * * *    
* * *     
* *      
* 
'''
