import os.path

filename='student.txt'
def main():
    while True:
        menum()
        choice=int(input('请选择:'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗？Y/N\n')
                if answer=='Y'or answer=='y':
                    print('谢谢您的使用!')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
        else:
            print('您输入有误！请重新输入')
def menum():
    print('========================学生信息管理系统==========================')
    print('----------------------------功能菜单-----------------------------')
    print('\t\t\t\t\t\t1:录入学生信息')
    print('\t\t\t\t\t\t2:查找学生信息')
    print('\t\t\t\t\t\t3:删除学生信息')
    print('\t\t\t\t\t\t4:修改学生信息')
    print('\t\t\t\t\t\t5:排序')
    print('\t\t\t\t\t\t6:统计学生总人数')
    print('\t\t\t\t\t\t7:显示所有学生信息')
    print('\t\t\t\t\t\t0:退出系统')
    print('----------------------------------------------------------------')
def insert():
    student_list=[]
    while True:
        id=input('请输入ID(如1001)：')
        if not id:#如果输入的id是空字符串，空字符串的布尔值是False，加not是True，则跳出循环
            break
        name=input('请输入姓名：')
        if not name:
            break
        flag=0
        while flag==0:
           try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩：'))
            java=int(input('请输入Java成绩：'))
            flag=1
           except:
            print('输入无效，不是整数类型，请重新输入。')
            continue
        #将录入的学生信息保存到字典之中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加学生信息？y/n\n')
        if answer=='y'or answer=='Y':
            continue
        else:
            break
    #调用save()函数
    save(student_list)
    print('学生信息录入完毕')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2：')
            if mode=='1':
                id=input('请输入学生ID：')
            elif mode=='2':
                name=input('请输入学生姓名：')
            else:
                print('你输入的有误，请重新输入！')
                continue
            with open(filename,'r',encoding='utf-8')as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否继续查找？y/n\n')
            if answer=='y':
                continue
            else:
                break
        else:
            return#结束整个search函数的调用了，啥也没返回，因为整个函数调用都结束了
                        #所以也不会在这个函数里边一直循环了。
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示！')
        return#直接返回，啥也不显示。
    #定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','python成绩','java成绩','总成绩'))
    #定义内容的显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:#在这个列表中遍历，其实这个列表中就一个字典
        print(format_data.format(item.get('id'),item.get('name'),
                                 #item.get('id')等价于item['id']
                                 item.get('english'),item.get('python'),
                                 item.get('java'),
        item.get('english')+item.get('python')+item.get('java')))
def delete():
   while True:
       student_id=input('请输入要删除的学生ID：')
       if student_id!='':
           if os.path.exists(filename):
               with open(filename,'r',encoding='utf-8')as file:
                   student_old=file.readlines()
           else:
               student_old=[]
           flag=False#标记是否删除
           if student_old:
               with open(filename,'w',encoding='utf-8')as wfile:#写的方式会覆盖掉原文件中的内容
                   d={}
                   for item in student_old:
                       d=dict(eval(item))#现在item是一个字符串，将我们的字符串转换为字典（eval的作用），存入字典中
                       if d['id']!=student_id:
                           wfile.write(str(d)+'\n')
                       else:
                           flag=True
                   if flag:
                       print('ID为{}的学生信息已被删除'.format(student_id))
                   else:
                       print('没有找到ID为{}的学生信息'.format(student_id))
           else:
               print('无学生信息')
               break
           show()
           answer=input('是否继续删除？y/n\n')
           if answer=='y'or answer=='Y':
               continue
           else:
               break
       else:
           print('您输入有误，请重新输入！')
           continue
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学生的ID：')
    if student_old!='':
        with open(filename,'w',encoding='utf-8')as wfile:
            for item in student_old:
                d=dict(eval(item))
                if d['id']==student_id:
                    print('找到学生信息了，可以修改该学生的信息了')
                    while True:
                        try:
                           d['name']=input('请输入姓名：')
                           d['english'] = int(input('请输入英语成绩：'))
                           d['python'] = int(input('请输入python成绩：'))
                           d['java'] = int(input('请输Java成绩：'))
                           break
                        except:
                            print('你输入的有错误，请重新输入!')
                    wfile.write(str(d)+'\n')
                    print('修改成功！')
                else:
                    wfile.write(str(d)+'\n')
            answer=input('是否继续修改其他学生的信息?y/n\n')
            if answer=='y'or answer=='Y':
                modify()
            else:
                pass
    else:
        print('你输入的学号有误，请重新输入！')
        modify()
def sort():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            student_list=rfile.readlines()
            student_new=[]
            for item in student_list:
                d=dict(eval(item))
                student_new.append(d)
            asc_or_desc=input('请选择(0：升序 1：降序)：')
            if asc_or_desc=='0':
                asc_or_desc_boll=False
            elif asc_or_desc=='1':
                asc_or_desc_boll=True
            else:
                print('你的输入有误，请重新输入！')
                sort()
            #选择排序方式
            mode=input('请选择排序方式(1：按英语成绩排序 2：按python成绩排序 3：按java成绩排序：4：按总成排序)：')
            if mode=='1':
                student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_boll)
        #这种方法是排列表中的字典的方法，因为列表中每个元素都是字典，要按字典中的某个键值进行排序，是这样的
        #key=lambda x表示列表中的一个字典，然后后边的意思是按字典中english的键值进行排序
            elif mode == '2':
                student_new.sort(key=lambda x:x['python'],reverse=asc_or_desc_boll)
            elif mode == '3':
                student_new.sort(key=lambda x:int(x['java']),reverse=asc_or_desc_boll)
            elif mode == '4':
                student_new.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['java']),reverse=asc_or_desc_boll)
            else:
                print('您的输入有误，请重新输入！')
                sort()
            show_student(student_new)
    else:
        return
def total():
    if os.path.exists(filename):
        with open (filename,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')#前边加个f，是格式化的形式输出
                #print('一共有{}名学生'.format(len(students)))等价
            else:
                print('还没有录入学生信息！')
def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            student=rfile.readlines()
            for item in student:
                student_list.append(eval(item))
            if  student_list:
                show_student(student_list)
    else:
        print('暂未保存数据！')
if __name__=='__main__':
    main()