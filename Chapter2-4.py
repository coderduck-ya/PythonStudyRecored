'''
字符串方法:
    单引号双引号无区别
    .title()  首字母大写
    .upper()/.lower()  全大写/全小写
    +直接拼接  在print中输出用+ str(target)
    .rstrip()/.lstrip()/strip()   去除左右两边空白字符串
    
列表方法:
    列表可以修改元素 元组元素不能修改 元组性能更高 不会轻易被垃圾回收
    ★  切片  ★
    append(value)
    insert(index,value)
    del 列表名称[index]
    pop()#返回弹出的元素值
    remove(value)
    sort()#排序改变原列表顺序
    sorted()#返回顺序列表
    reverse()#逆序
    len()
'''
LIST=[]
if not LIST:
    print("空")
LIST=[1,'33',0.3,"hello",[1,2,3,4]]
#for遍历列表
for item in LIST:
    print(item)
#产生随机数组
LIST=list(range(1,10,2))
#简单的创建数组
LIST=[value**2 for value in range(1,11)]

print(max(LIST))
print(sum(LIST))

#测试for循环与range(left,right,step) [left,right)

ans=0
for value in range(1,1000001):
    ans=value+ans
print(ans)
#数组的赋值操作
newList=LIST #给LIST地址  对newList的操作也会影响LIST
# newList=LIST[:] #返回的LIST引用 
LIST.append('hhh')
newList.append(11111)
print(LIST)
print(newList)

#元组用()列表用[] 只能修改元组的引用