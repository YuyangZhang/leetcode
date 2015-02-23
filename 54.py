class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix==[]:
            return []
        result=[]
        drt=1
        x=0
        y=0
        xmax=len(matrix[0])
        ymax=len(matrix)
        visited=[]
        for i in range(0,len(matrix)):
            tmp=[]
            for j in range(0,len(matrix[0])):
                tmp.append(0)
            visited.append(tmp)
        while True:
            result.append(matrix[y][x])
            visited[y][x]=1
            if drt==1:
                if x+1!=xmax and visited[y][x+1]!=1:
                    x+=1
                else:
                    if y+1!=ymax and visited[y+1][x]!=1:
                        drt=2
                        y+=1
                    else:
                        return result
            elif drt==2:
                if y+1!=ymax and visited[y+1][x]!=1:
                    y+=1
                else:
                    if x!=0 and visited[y][x-1]!=1:
                        drt=3
                        x-=1
                    else:
                        return result
 
            elif drt==3:
                if x!=0 and visited[y][x-1]!=1:
                    x-=1
                else:
                    if y!=0 and visited[y-1][x]!=1:
                        drt=4
                        y-=1
                    else:
                        return result
            elif drt==4:
                if y-1!=0 and visited[y-1][x]!=1:
                    y-=1
                else:
                    if x!=xmax and visited[y][x+1]!=1:
                        drt=1
                        x+=1
                    else:
                        return result
            
print(Solution().spiralOrder([
]))
