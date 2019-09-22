
# -*- coding: UTF-8 -*-
print ("帮助把csv转化为xml，没解决英文逗号")
ps = raw_input("输入读取的文件xxx.csv和存储的文件xxx.txt  (abc.csv,save.txt)    :")
p1, p2 = [p for p in ps.split(',')]
import sys
reload(sys)
# sys.setdefaultencoding('utf-8')

p = "test2.csv"

p = p1

result=[]
f = []
try:
    f = open(p, 'r')    # 打开文件
    lines = f.readlines()
    for line in lines:
        # print line.decode('utf-8')
        line = line.replace('\r\n','')
        tmp = line.decode('utf-8')
        # print (tmp)
        result.append(tmp.split(','))
        # print (result[0][len(result[0])-1])
        # result.append(list(line.split(',')))

    # print result[0][0]


    # for line in f:
    #     result.append(list(line.split(',')))
    # print((result[0]))


finally:
    if f:
        f.close()


ps = raw_input("请输入  < 后面第一个跟随的文字 (如：COM_ANSWER_EVALUATION)    :")


out = ""
for i in range(1,len(result)):
    out += "<"+ps+ " "
    for i2 in range(len(result[1])):
        tmp1 = result[1][i2].encode('utf-8')
        out += tmp1 + "=\""
        tmp2 = result[i][i2].encode('utf-8')
        if i2 ==len(result[1])-1:
            out += tmp2 + "\""
            continue
        out += tmp2 + "\" "

    out += "/>\n"

print (out)



try:
    fo = open(p2, "w")

    fo.write(out)
finally:
    if fo:
        fo.close()                     # 确保文件被关闭


