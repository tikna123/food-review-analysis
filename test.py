'''


given square matrix, size n by n 
rotate matrix by 90


matrix = [1,2,3
          4,5,6   = >  
          7,8,9]

        [ 7,4,1
           8,5,2
           9,6,3
        ]

def rotate_matrix(matrix):
    n = len(matrix)

    steps = n//2

    for step in range(steps):
        for i in range(step,n-step-1):
            t = matrix[step][i]
            matrix[step][i] = matrix[n-1-i][step]
            matrix[n-1-i][step] = matrix[n-1-step][n-1-i]
            matrix[n-1-step][n-1-i] = matrix[i][n-1-step]
            matrix[i][n-1-step]= t



given an array, size n+1
each elemnt of array is 1,2,3..n 
unknown number whihc is between 1 to n..
only 1 duplicate number.
inital state: not sorted
find duplicate number in array

'''


def find_dup(arr):
    slow = arr[0]
    fast = arr[slow]

    while fast !=slow:
        slow = arr[slow]
        fast = arr[arr[fast]]

    fast = 0

    while slow!=fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return fast 

arr = [5,2,3,2,4,1]


print(find_dup(arr))



Given 2d matrix, square matrix
implement 2 functions
1) sum(x1,y1,x2,y2) return summation of elements between rectangle
2) update(x,y,v) no return anything. it should update(x,y) to v


sum(x1,y1,x2,y2)
=> temp[x2][y2] - temp[x1-1][y2] - temp[x2][y1-1] + temp[x1-1][y1-1]


   x1,y1

([1,2,3,4]
[5,6,7,8]
[9,10,11,12]
[13,14,15,16])

         (0-1,0-0)=> 1
         (0-2,0-0)=>3
         input=> (x1,y1),(x2,y2)
                            
                             []

                if x1<n/2&&y1<m/2    x1<n/2 && y1>m/2        x1>n/2 && y1<m/2     x1>n/2 && yl>m/2
                [1,2,5,6],sum             [3,4,7,8]             [9,10,13,14]         [11,12,15,16]              

            [1] [2] [5] [6]          [3] [4] [7] [8]         [9] [10] 


                x2, y2

    quad_tree
    {
      top_left 
      top_right
      bot_left
      bot_right                    
    }          
    
    quad(top_l, bot_r)
    {
        top_left = top_l
        bo
    }           0-n,0-m
           0-n/2    n/2-n        0-m/2      m/2-m

