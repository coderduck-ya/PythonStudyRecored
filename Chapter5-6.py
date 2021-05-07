#if 多条件判断
testIfList=['aaa','bbb','cccc',222]


if 'eee' in testIfList  or 'ddd'  in testIfList:
    print(1)
elif 'aaa' in testIfList  and 'ddd' not in testIfList:
    print(2)
else:
    print(3)

for item in testIfList:
    if str(item)=='222':
        print(4)

#字典 创建
directory={'color':'aaa',2:3,'606':3}
# 用函数创建
directory = dict(color='Tom', 哈哈哈 = 3,ok=20)
# 用列表加元组创建
directory = [('color', 1.58), ('2', 1.29), ('606', 2.19)]# 创建包含3组key-value对的字典
directory = dict(directory)
#增删改查
print(directory['color'])
print(directory['2'])
directory['606']="哈哈哈"
directory['404']='妈个比韩茂荧'
directory[5]=2
del directory['color']
print(directory)

#遍历
for key,value in directory.items():
    print(str(key)+" : "+str(value))

for key in directory.keys():
# for value in directory.values():
    print(str(key)+" : "+str(directory[key]))

#列表中有字典
dir1={'niubi':'薛书亚'}
dir2={'laji':"sb"}
dir3={'666':"亚哥"}
dirList=[dir1,dir2,dir3,'哈哈哈']
print(dirList)
for num in range(0,10):
    dir3={'666':num}
    dirList.append(dir3)
print(len(dirList))
#字典中有列表
goodMan={
    'name':['薛书亚','coderduck',666],
    "age":18,
    'logo':[1,2,3,4,5]}
print(goodMan['name'][0])
for key in goodMan.keys():
    if key=='name':
        for item in goodMan[key]:
            print(item)
#字典中有字典
people={
    'one':{
        'name':"薛书亚",
        'age':18
    },
    'two':{
        'name':"傻逼韩茂荧草泥马",
        'age':1
    },
    "OK":"哈哈哈"
}
print(people['one'])