import mysql.connector as ms
import matplotlib.pyplot as pl

sc={}
def distinctions():
    t=()
    t1=()
    t2=()
    db1=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur1=db1.cursor()
    sql="select subcode,subname from subtable"
    cur1.execute(sql,)
    p=cur1.fetchall()
    s="%-8s"*len(p)
    tup=()
    for i in p:
        tup+=(i[1],)
    print('\nNo. of distinctions in each subject\n') 
    print(s %tup)
    
    for i in p:
        a=0
        b=0
        m,g=ret_submarksandgender(i[0])
        for j in range(len(m)):
            if g[j]=='M' and m[j]>=75:
                a+=1
            if g[j]=='F' and m[j]>=75:
                b+=1
        t+=(a+b,)
        t1+=('M='+str(a),)
        t2+=('F='+str(b),)
    print(s %t)
    print(s %t1)
    print(s %t2)

    
def create_subtable():
    
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql="use 12res"
    
    cur.execute(sql,)
    sql='create table subtable(subcode char(5),subname varchar(30), primary key(subcode))'
    cur.execute(sql,)
    for i in sc:
        sql='insert into subtable values(%s,%s)'
        val=(i,sc[i])
        cur.execute(sql,val)
    db.commit()

def findfailures():
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql="use 12res"
    
    cur.execute(sql,)
    sql="select roll,name,result, avg from result  where result=%s or result=%s"
    val=('COMP','FAIL')
    cur.execute(sql,val)
    p=cur.fetchall()
    print('FAILURES/ COMPARTMENTALS')
    k=1
    for i in p:
        print(i[0],i[1],i[2],i[3])
        k+=1
        
    print('\n\n')
    db.commit()

def passanalysis():
    db1=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur1=db1.cursor()
    db2=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur2=db2.cursor()
    db3=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur3=db3.cursor()
    db4=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur4=db4.cursor()
    sql="select count(*) from result  where result=%s"
    val=('PASS',)
    cur1.execute(sql,val)
    p1=cur1.fetchall()
    sql="select count(*) from result"
    cur2.execute(sql)
    p2=cur2.fetchall()
    sql='select gender from result where result=%s'
    val=('PASS',)
    cur3.execute(sql,val)
    p3=cur3.fetchall()
    sql='select gender from result'
    cur4.execute(sql)
    p4=cur4.fetchall()
    tm=tf=m=f=0
    for i in p3:
        if i[0]=='M':
            m+=1
        else:
            f+=1
    for i in p4:
        if i[0]=='M':
            tm+=1
        else:
            tf+=1
    
    print('TOTAL PASS:',p1[0][0])
    print('TOTAL APPEARED:',p2[0][0])
    print('PASS %:',p1[0][0]/p2[0][0]*100)
    print('TOTAL MALE PASSED:',m)
    print('TOTAL FEMALE PASSED:',f)
    print('MALE PASS %:',m/tm*100)
    print('FEMALE PASS %:',f/tf*100)
    
    print('\n\n')
    db1.commit()
    db2.commit()
def findtoppers():
    
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql="use 12res"
    
    cur.execute(sql,)
    sql="select roll,name,avg from result  order by avg desc"
    
    cur.execute(sql,)
    p=cur.fetchall()
    print('\n\nTOPPERS')
    k=1
    for i in p:
        print(i[0],i[1],i[2])
        k+=1
        if k==4:
            break
    print('\n\n')
    db.commit()
def heading(stream):
    print('\n\n',stream,'\n')
    print('%-4s%-10s%-30s%10s%10s%10s%10s%10s%10s%9s'%('SNO','Roll','Name','sub1','sub2','sub3','sub4','sub5','sub6','avg'))
    
def ret_subname(scode):
    
    db1=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur1=db1.cursor()
    sql="select subname from subtable where subcode=%s"
    val=(scode,)
    cur1.execute(sql,val)
    q=cur1.fetchone()
    return q[0]
   
  
        
def science():
    code='042'
    heading('SCIENCE')
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql="use 12res"
    cur.execute(sql,)
    
    sql="select * from result where subcode1=%s or subcode2=%s or subcode3=%s or subcode4=%s or subcode5=%s or subcode6=%s order by avg desc"
    val=(code,code,code,code,code,code)
    cur.execute(sql,val)
    p=cur.fetchall()
    k=1
    ch=''
    for i in p:
        if i[19]==0:
            print("%-4d%-10s%-30s%10s%10s%10s%10s%10s%10s%9.1f" %(k,i[0],i[2],'('+ret_subname(i[3])+')'+str(i[4]),'('+ret_subname(i[6])+')'+str(i[7]),'('+ret_subname(i[9])+')'+str(i[10]),'('+ret_subname(i[12])+')'+str(i[13]),'('+ret_subname(i[15])+')'+str(i[16]),ch,i[25]))
        else:
            print("%-4d%-10s%-30s%10s%10s%10s%10s%10s%10s%9.1f" %(k,i[0],i[2],'('+ret_subname(i[3])+')'+str(i[4]),'('+ret_subname(i[6])+')'+str(i[7]),'('+ret_subname(i[9])+')'+str(i[10]),'('+ret_subname(i[12])+')'+str(i[13]),'('+ret_subname(i[15])+')'+str(i[16]),'('+ret_subname(i[18])+')'+str(i[19]),i[25]))
        k+=1  
    db.commit()    
    
def commerce():
    code='055'
    heading('COMMERCE')
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql="use 12res"
    cur.execute(sql,)
    
    sql="select * from result where subcode1=%s or subcode2=%s or subcode3=%s or subcode4=%s or subcode5=%s or subcode6=%s order by avg desc"
    val=(code,code,code,code,code,code)
    cur.execute(sql,val)
    p=cur.fetchall()
    k=1
    ch=''
    for i in p:
        if i[19]==0:
            print("%-4d%-10s%-30s%10s%10s%10s%10s%10s%10s%9.1f" %(k,i[0],i[2],'('+ret_subname(i[3])+')'+str(i[4]),'('+ret_subname(i[6])+')'+str(i[7]),'('+ret_subname(i[9])+')'+str(i[10]),'('+ret_subname(i[12])+')'+str(i[13]),'('+ret_subname(i[15])+')'+str(i[16]),ch,i[25]))
        else:
            print("%-4d%-10s%-30s%10s%10s%10s%10s%10s%10s%9.1f" %(k,i[0],i[2],'('+ret_subname(i[3])+')'+str(i[4]),'('+ret_subname(i[6])+')'+str(i[7]),'('+ret_subname(i[9])+')'+str(i[10]),'('+ret_subname(i[12])+')'+str(i[13]),'('+ret_subname(i[15])+')'+str(i[16]),'('+ret_subname(i[18])+')'+str(i[19]),i[25]))
        k+=1       
    
    db.commit()    

def humanities():
    cd='028'
    heading('HUMANITIES')
    
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql="use 12res"
    cur.execute(sql,)
    
    sql="select * from result where subcode1 not in (%s,%s) and subcode2 not in (%s,%s) and subcode3 not in (%s,%s) and subcode4 not in (%s,%s) and subcode5 not in (%s,%s) and subcode6 not in (%s,%s) order by avg desc"
    val=('055','042','055','042','055','042','055','042','055','042','055','042')
    cur.execute(sql,val)
    p=cur.fetchall()
    k=1
    ch=''
    for i in p:
        if i[19]==0:
            print("%-4d%-10s%-30s%10s%10s%10s%10s%10s%10s%9.1f" %(k,i[0],i[2],'('+ret_subname(i[3])+')'+str(i[4]),'('+ret_subname(i[6])+')'+str(i[7]),'('+ret_subname(i[9])+')'+str(i[10]),'('+ret_subname(i[12])+')'+str(i[13]),'('+ret_subname(i[15])+')'+str(i[16]),ch,i[25]))
        else:
            print("%-4d%-10s%-30s%10s%10s%10s%10s%10s%10s%9.1f" %(k,i[0],i[2],'('+ret_subname(i[3])+')'+str(i[4]),'('+ret_subname(i[6])+')'+str(i[7]),'('+ret_subname(i[9])+')'+str(i[10]),'('+ret_subname(i[12])+')'+str(i[13]),'('+ret_subname(i[15])+')'+str(i[16]),'('+ret_subname(i[18])+')'+str(i[19]),i[25]))
        k+=1  
    
    db.commit()      
def change_to_simple_format(fname):
    f=open(fname,"r")
    f1=open('result.txt',"w")
    ml=f.readlines()
    for i in ml:
        if i!=[] and i[0] in '0123456789':
            f1.write(i)
    f.close()
    f1.close()

def transfer_to_mysql():
    f=open('result.txt',"r")
    ml=f.readlines()
    db=ms.connect(host='localhost', user='root', passwd='')
  
    cur=db.cursor()
    
    sql="drop database 12res"
    cur.execute(sql,)
    sql="create database 12res"
    cur.execute(sql,)
    sql="use 12res"
    
    cur.execute(sql,)
    sql='''create table result(roll int, gender char(1), name varchar(30), subcode1 char(3), marks1 int(3), grade1 char(3),
subcode2 char(3), marks2 int(3), grade2 char(3), subcode3 char(3), marks3 int(3), grade3 char(3), subcode4 char(3), marks4 int(3), grade4 char(3),
subcode5 char(3), marks5 int(3), grade5 char(3), subcode6 char(5), marks6 int(3), grade6 char(5), gg1 char(2), gg2 char(2), gg3 char(2), result char(10),avg decimal(5,2),primary key(roll))'''
    cur.execute(sql,)
    
    for l in ml:
        l=l.split()
        roll=int(l[0])
        gender=l[1]
        name=''
        c=1
        for i in l[2:]:
            c+=1
            if i.isalpha():
                name+=(i+' ')
            else:
                break
        subcode=[]
        marks=[]
        grade=[]
        p=0
        for i in range(6):
            if l[c][0].isalpha():
                subcode.append('NULL')
                marks.append(0)
                grade.append('NULL')
                break
            subcode.append(l[c])
            cod={'101':'Fn eng','001':'EngEl','002':'HinEl','118':'GER','118':'FREN','022':'Sans','301':'engC','302':'hinC','322':'sansC',\
                 '041':'math','042':'phy','043':'chem','048':'phyed','044':'bio','045':'btech','030':'eco','027':'hist','028':'polsc',\
                 '054':'bstd','055':'acc','066':'Entre','049':'fart','083':'cs','065':'ip','029':'Geog','040':'Philo','037':'Psyc',\
                 '039':'Socio','064':'HomeSc','067':'MWT','072':'MassMed','076':'NCC','078':'Theatr'}
          
            if l[c] not in sc.keys():
                sc[l[c]]=cod[l[c]]
            marks.append(int(l[c+1]))
            grade.append(l[c+2])
            c+=3
            p+=1
        tmarks=marks.copy()
        tmarks.sort(reverse=True)
        tot=0
        for j in range(5):
            tot+=tmarks[j]
        avg=tot/5    
        grade1=l[c]
        grade2=l[c+1]
        grade3=l[c+2]
        result=l[c+3]
        val=(roll,gender,name,subcode[0],marks[0],grade[0],subcode[1],marks[1],grade[1],subcode[2],marks[2],grade[2],subcode[3],marks[3],grade[3],subcode[4],marks[4],grade[4],subcode[5],marks[5],grade[5],grade1,grade2,grade3,result,avg)            
        sql='insert into result values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql,val)
    db.commit()

def overall():
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql="use 12res"
    cur.execute(sql,)
    
    sql="select roll, gender, name, avg from result order by avg desc"
    cur.execute(sql,)
    p=cur.fetchall()
    k=1
    for i in p:
        print("%-4d%-15d%-5s%-30s%-6.1f" %(k,i[0],i[1],i[2],i[3]))
        k+=1  
    
    db.commit()

def ret_submarksandgender(code):
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql='use 12res'
    cur.execute(sql,)
    sql='select gender,subcode1,marks1,subcode2,marks2,subcode3,marks3,subcode4,marks4,subcode5,marks5,subcode6,marks6 from result where subcode1=%s or subcode2=%s or subcode3=%s or subcode4=%s or subcode5=%s or subcode6=%s'
    val=(code,code,code,code,code,code)
    cur.execute(sql,val)
    p=cur.fetchall()
    db.commit()
    m=[]
    a=[]
    for i in p:
        a+=i[0]
        for j in range(1,len(i),2):
            if i[j]==code:
                m.append(int(i[j+1]))
                break      
    return m,a

def ret_submarks(code):
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql='use 12res'
    cur.execute(sql,)
    sql='select subcode1,marks1,grade1,subcode2,marks2,grade2,subcode3,marks3,grade3,subcode4,marks4,grade4,subcode5,marks5,grade5,subcode6,marks6,grade6 from result where subcode1=%s or subcode2=%s or subcode3=%s or subcode4=%s or subcode5=%s or subcode6=%s'
    val=(code,code,code,code,code,code)
    cur.execute(sql,val)
    p=cur.fetchall()
    db.commit()
    m=[]
    g=[]
    for i in p:
        for j in range(0,len(i),3):
            if i[j]==code:
                m.append(int(i[j+1]))
                g.append(i[j+2])
                break      
    return m,g
                
def slabn():
    t=[]
    db1=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur1=db1.cursor()
    sql="select subcode,subname from subtable"
    cur1.execute(sql,)
    p=cur1.fetchall()
    
    print("%-20s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-15s%-10s%-20s" %('subject name','90-100','80-89','70-79','60-69','50-59','40-49','33-39','below 33/FE','FTE','total appeared'))
    for i in p:
        a=b=c=d=e=f=g=h=x=0
        tp=ret_submarks(i[0])
        m=tp[0]
        q=tp[1]
        for w in q:
            if w=='FTE':
                x+=1
                
        for k in m:
            if k>=90:
                a+=1
            elif k>=80:
                b+=1
            elif k>=70:
                c+=1
            elif k>=60:
                d+=1
            elif k>=50:
                e+=1
            elif k>=40:
                f+=1
            elif k>=33:
                g+=1
            else:
                h+=1
        tt=a+b+c+d+e+f+g+h
        print("%-20s%-10d%-10d%-10d%-10d%-10d%-10d%-10d%-15d%-10d%-20d" %(i[1],a,b,c,d,e,f,g,h,x,tt))
        marks=[a,b,c,d,e,f,g,h]
        popu=['90-100','80-89','70-79','60-69','50-59','40-49','33-39','below 33/FE'] 
        ll=[popu,marks]
        t.append(ll)
    o=1
    while o==1:
        aa=[]
        b=[]
        k=1
        print('Choose from the following:')
        print('Graph for')
        for j in p:
            print(k,'for',j[1])
            aa.append(k)
            b.append(j[1])
            k+=1
        print(k,'to exit')
        r=int(input())
        if r==k:
            break
        for u in aa:
            if r==u:
                pl.bar(t[r-1][0],t[r-1][1])
                pl.title(b[r-1]+' marks visual analysis', loc='center')
                pl.show()
                break
                
    db1.commit()
    
def slabp():
    t=[]
    db1=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur1=db1.cursor()
    sql="select subcode,subname from subtable"
    cur1.execute(sql,)
    p=cur1.fetchall()
    db1.commit()
    print("%-20s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-15s%-10s%-20s" %('subject name','90-100','80-89','70-79','60-69','50-59','40-49','33-39','below 33/FE','FTE','total appeared'))
    for i in p:
        a=b=c=d=e=f=g=h=x=0
        tp=ret_submarks(i[0])
        m=tp[0]
        q=tp[1]
        for w in q:
            if w=='FTE':
                x+=1
                
        for k in m:
            if k>=90:
                a+=1
            elif k>=80:
                b+=1
            elif k>=70:
                c+=1
            elif k>=60:
                d+=1
            elif k>=50:
                e+=1
            elif k>=40:
                f+=1
            elif k>=33:
                g+=1
            else:
                h+=1
        tt=a+b+c+d+e+f+g+h
        print("%-20s%-10.1f%-10.1f%-10.1f%-10.1f%-10.1f%-10.1f%-10.1f%-15.1f%-10.1f%-20d" %(i[1],a/tt*100,b/tt*100,c/tt*100,d/tt*100,e/tt*100,f/tt*100,g/tt*100,h/tt*100,x/tt*100,tt))
        marks=[a,b,c,d,e,f,g,h]
        popu=['90-100','80-89','70-79','60-69','50-59','40-49','33-39','below 33/FE'] 
        ll=[marks,popu]
        t.append(ll)
    o=1
    while o==1:
        aa=[]
        b=[]
        k=1
        print('Choose from the following:')
        print('Graph for')
        for j in p:
            print(k,'for',j[1])
            aa.append(k)
            b.append(j[1])
            k+=1
        print(k,'to exit')
        r=int(input())
        if r==k:
            break
        for u in aa:
            if r==u:
                pl.pie(t[r-1][0],labels=t[r-1][1])
                pl.title(b[r-1]+' marks visual analysis', loc='center')
                pl.show()
                break
                
    db1.commit()

def subtop(code):
    db=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur=db.cursor()
    sql='use 12res'
    cur.execute(sql,)
    sql='select * from result where subcode1=%s or subcode2=%s or subcode3=%s or subcode4=%s or subcode5=%s or subcode6=%s'
    val=(code,code,code,code,code,code)
    cur.execute(sql,val)
    p=cur.fetchall()
    db.commit()
    m=[]
    g=[]
    t=[]
    for i in p:
        for j in range(3,21,3):
            if i[j]==code:
                m.append(int(i[j+1]))
                t.append([i[0],i[2]])
                break

    k=0      
    for u in m:
        if u==max(m):
            print(t[k][0],t[k][1],u)
        k+=1
            
def choice():
    db1=ms.connect(host='localhost', user='root', passwd='',db='12res')
    cur1=db1.cursor()
    sql="select subcode,subname from subtable"
    cur1.execute(sql,)
    p=cur1.fetchall()
    db1.commit()
    for i in p:
        print(i[1])
        subtop(i[0])
        print()
       
        

def main():
    print('''RESULT ANALYSIS SOFTWARE
made by Siddharth Pal 12-A''')
    fn=input("Enter filename (65512.txt):")
    change_to_simple_format(fn)
    transfer_to_mysql()
    create_subtable()
    print('\nData successfully entered!\n')
    t=1
    while t==1:
        print('''Choose from the following:\n
Press
1  for overall result
2  for result by stream
3  for result of science stream
4  for result of commerce stream
5  for result of humanities stream
6  for pass analysis
7  for toppers
8  for failures
9  for slab wise subject analysis (numbers)
10 for slab wise subject analysis (percentage)
11 distinctions
12 for subject toppers
13 to exit''')
        x=int(input())
        print()
        if x==1:
            overall()
        elif x==2:
            science()
            commerce()
            humanities()
        elif x==3:
            science()
        elif x==4:
            commerce()
        elif x==5:
            humanities()
        elif x==6:
            passanalysis()
        elif x==7:
            findtoppers()
        elif x==8:
            findfailures()
        elif x==9:
            slabn()
        elif x==10:
            slabp()
        elif x==11:
            distinctions()
        elif x==12:
            choice()
        elif x==13:
            t=0
        else:
            print('invalid input')
        print('\n')
if __name__=="__main__":
    main()
    
    
        
    
    
