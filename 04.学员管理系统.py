#需求
'''
1. 添加学员
2. 删除学员
3. 修改学员信息
4. 查询学员信息
5. 显示所有学员信息
6. 退出系统
'''
#步骤分析
'''
1. 显示功能界面
2. 用户输入功能序号
3. 根据用户输入的功能序号，执行不同的功能
    3.1 定义函数
    3.2 调用函数
'''
#定义显示功能界面
def info_print():
    ss='请选择功能界面'
    print(ss.center(30,'*'))
    print('1.添加学院')
    print('2删除学员')
    print('3修改学员信息')
    print('4查询学员')
    print('5显示学员信息')
    print('6退出')
    print('*'*30)
#存在信息的列表
info=[]
#添加学员
'''
1. 接受输入信息，并保存
2. 判断学员信息是否存在
3 已经存在，则报错提示
4. 如果不存在，则准备空字典
'''

def add_info():
    #用户输入学号手机号姓名
    new_id=input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')
    #判断是否添加学员
    global info
    for i in info:
        if new_name in i['name']:
            print('此用户已经存在')
            return

    #如果不重复，将个人信息添加到字典
    info_dict={}
    info_dict['id']=new_id
    info_dict['name']=new_name
    info_dict['tel']=new_tel

    #将个人信息字典加大会员列表
    info.append(info_dict)
    print(info)

#删除学员
'''
1.用户输入学员
2.判断是否存在

'''
def del_info():
    #接受用户要删除的学员姓名
    del_name=input('请输入要删除的学员')
    global info
    for i in info:
         if i['name']==del_name:
            info.remove(i)
            break
         else :
            print(f'您输入的姓名{del_name}不存在')
    print(info)

def modify_info():
    #修改学员信息
    #接受用户输入的学员名
    modify_name=input('请输入要修改信息的学员')
    #学员信息列表
    global info
    #判断名字是否存在在学员列表中
    for i in info:
        if i['name']==modify_name:
            i['tel']=input('请输入新的手机号码')
            break
    else:
        print('学员不存在')
    print(info)

def search_info():
    #查找学员信息
    #输入要查找的学员名
    search_name=input('请输入你要查找的会员名：')
    global info

    for i in info:
        if i['name']==search_name:
            print(f'{search_name}的学号为{i["id"]},手机号码为{i["tel"]}')
            break
    else:
        print('查询的学员不存在')
    print(info)

def print_all():
    #打印所有学员信息
    print('学号\t姓名\t手机号')
    global info
    for i in info:
        print(f"{i['id']}\t\t {i['name']}\t \t{i['tel']}")








while 1:
    #显示功能界面
    info_print()
    #接受用户选项
    use_num=int(input('请输入相关的功能序号：'))

    if use_num==1:
        #print('添加')
        add_info()
    elif use_num==2:
        #print('删除')
         del_info()
    elif use_num==3:
         #print('修改')
        modify_info()
    elif use_num==4:
        #print('查询')
        search_info()
    elif use_num==5:
        #print('显示')
        print_all()
    elif use_num==6:
        exif=input('确认退出吗？y/n?')
        if exif=='y'or 'Y':
            break
    else:
        print('输入的功能选项有错')