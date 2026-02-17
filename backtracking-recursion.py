#code to generate all the combinations while permuting a string using backtracking in a recursion
'''def combine(s,ans=" "):
    if len(s)==0:
        print(ans)
        return
    for i in range(len(s)):
        ch=s[i]
        left_over=s[:i]+s[i+1:]
        combine(left_over,ans+ch)
s=input("enter a string:")
combine(s)'''

#simple backtracking sunsets
#code to generate subsets froma list using simple backtracking of recursion
'''def subset(arr,index=0,current=[]):
    if index==len(arr):
        print(current)
        return
    subset(arr,index+1,current+[arr[index]])
    subset(arr,index+1,current)
arr=list(map(int,input("enter nums with spaces:").split()))'''


#code for maze 
'''S 0 0 
   0 1 0
   0 0 E
   0->free
   1->blocked
   start(0,0)
   end-(2,2)
   moves:R->right
         D->down
process
at each cell   
    -cell valid or not
    -if reached end(2,2)->print path
    -try right
        -try right
        -explore fully
    return 
    -try down
        -try down
        -explore fully
    return
   '''
#code for maze
'''def maze(grid,i,j,n,path):
    if i>=n or j>=n or grid[i][j]==1:
        return
    if i==n-1 and j==n-1:
        print(path)
        return
    maze(grid,i,j+1,n,path+"R")
    maze(grid,i+1,j,n,path+"D")
grid=[[0,0,0],[0,0,0],[0,0,0]]
maze(grid,0,0,3," ")'''

