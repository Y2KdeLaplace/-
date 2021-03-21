# subtitles loading out
# 2021.3.20 written by yiheng hu

## trans files forming
f1=open('MRI.txt','rb')
f2=open('trans.txt','wb')
n=1
for line in f1.readlines():
    if n==3:
        f2.write(line)
    elif (n-3)%5==0:
        f2.write(line)
    endmarker=(n+2)/5
    if endmarker==500:
        break
    n=n+1
f2.close()
f1.close()

## final script file forming
f2=open('trans.txt',encoding = "utf-8")
f3=open('script.txt','w')
data = f2.read()#会把换行\n符号读进去

#Plan A：得到结果中有部分的转义符号
#data=str(data)#对于list中多个str，要合并成一个可以直接用str()
#data=data.replace('\\n',' ')

#Plan B
data=data.split('\n')#根据换行符号分开list中的元素
data= ' '.join(data)#合并list元素，中间为空格

f3.write(data)
f2.close()
f3.close()

##supplement
#e = [str(i) for i in data]等价于data=map(str, data)——————让list中每个元素变成str