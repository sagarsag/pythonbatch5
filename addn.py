def sum(num,n):
    i=0
    s=0
    while i<n:
          s=s+num[i]
          i=i+1
    return s
n=int(input('enter size of array\n'));
num=[]
i=0
print('enter array elements');
while i<n:
      r=int(input());
      i=i+1
      num.append(r)
s=sum(num,n);
print('sum={0}'.format(s))
