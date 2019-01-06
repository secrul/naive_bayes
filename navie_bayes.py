import math

NU = 5000
ss = 0#统计垃圾邮件个数
f_a = []#记录测试邮件的0/1，因为一会要集合去重，去除1/0
ft = open(r"D:\train.txt")
la = []#来存储测试数据
label = []
read = ft.readlines()
for line in read:
    te = line.rstrip('\n').split(' ')
    for i in te:
        i = i.lower()
    label += te#存储词库,需要前面的0/1标签，予以保留
    if te[0] == '0':
        ss += 1
        f_a.append(0)
    else:
        f_a.append(1)
    del(te[0])
    la.append(list(set(te)))#去除测试集中重复单词，去除了0/1标签,保存每一封邮件的单词
ft.close()

hh = NU - ss
ps = ss / NU
ph = 1 - ps

sa_s =set(label)#单词去重
la_s = list(sa_s)
val = []
la_s.remove('1')
la_s.remove('0')
for i in range(len(la_s)):
    val.append(0)
dds = dict(zip(la_s,val))
ddh = dict(zip(la_s,val))

ct = -1
tt = 0
for aa in la:#遍历训练集，找出每一个单词在垃圾邮件和非垃圾邮件是否出现
    ct += 1
    for i in aa:
        if i in sa_s:
           if f_a[ct] == 0:
               dds[i] += 1
           else:
               ddh[i] += 1

for i in la_s:#有可能单词只在垃圾邮件中出现，那么可能出现乘0
    if dds[i] == 0 or ddh[i] == 0:
        dds[i] += 1
        ddh[i] += 1

f_b = []#记录测试邮件的0/1，因为一会要集合去重，去除1/0
ft = open(r"D:\test.txt")
lb = []#来存储测试数据
read = ft.readlines()
for line in read:
    te = line.rstrip('\n').split()
    for i in te:#转小写
        i = i.lower()
    if te[0] == '0':
        f_b.append(0)
    else:
        f_b.append(1)
    del(te[0])
    lb.append(list(set(te)))#去除测试集中重复单词
ft.close()
corr = 0
ct = 0
ans = []
for li in lb:#遍历每一个测试邮件
    ts = math.log(ps, 10)
    th = math.log(ph, 10)
    for i in li:
        if i in sa_s:#测试单词在训练集中
            ts += math.log(dds[i], 10)  #
            th += math.log(ddh[i], 10)  #
            if dds[i] == 1:#测试集中垃圾邮件没有出现i
                ts -= math.log(ss + 1, 10)
            else:
                ts -= math.log(ss, 10)
            if ddh[i] == 1:
                th -= math.log(hh + 1, 10)
            else:
                th -= math.log(hh, 10)
    if ts > th:
        ans.append(0)
    if ts < th:
        ans.append(1)
with open(r"D:\ans.txt",'w') as f:
    for x in ans:
        f.write(str(x))
        f.write('\n')
