lass Solution:
    def nextPermutation(self, x) -> None:
        n=len(x)
        j=1
        hit=0
        while j < n:
            for i in range(1,j+1):
                if x[-(j+1)] < x[-i]:
                    x[-i], x[-j-1] = x[-j-1], x[-i]
                    y=x[-j::] 
                    y.sort()
                    x[-j::]=y 
                    hit=1
                    break
            if hit==1:
                j=n
            else:
                j +=1
        if hit!=1:
            x.reverse()
        return x
