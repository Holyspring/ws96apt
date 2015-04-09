#coding:utf-8
import pandas as pd
from pandas import DataFrame
from pylab import mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif']=['SimHei'] #设置字体
mpl.rcParams['axes.unicode_minus']=False #编码
def dict_deal(dict_in):
    dict_out={}
    numAPP=0
    numMD=0
    numSJ=0
    numCS=0
    numDGS=0
    numDL=0
    for i in dict_in.keys():
        #print i,'+',a_read[i]

        if u'移动APP' in i:
            numAPP+=dict_in[i]
        if u'魔都' in i:
            numMD+=dict_in[i]
        if u'手机浏览器' in i:
            numSJ+=dict_in[i]
        if u'唱衰' in i:
            numCS+=dict_in[i]
        if u'大公司创新' in i:
            numDGS+=dict_in[i]
        if u'大佬' in i:
            numDL+=dict_in[i]
    dict_out['移动APP']=numAPP
    dict_out['魔都']=numMD
    dict_out['手机浏览器']=numSJ
    dict_out['唱衰']=numCS
    dict_out['大公司创新']=numDGS
    dict_out['大佬']=numDL
    return dict_out
df = pd.ExcelFile("wxgzhdata.xlsx").parse(u"3月")
df2=df.fillna(method="pad")#往后填充
d1=df2.groupby(u'文章标题').sum()[[u'总阅读人数',u'初次打开阅读人数',u'分享次数',u'每日增粉人数']]
a=d1.to_dict(outtype='dict')#list
#print a
a_read= a[u'总阅读人数']
f_read=a[u'初次打开阅读人数']
share=a[u'分享次数']
fans=a[u'每日增粉人数']

#print a_read
x={}
out_a_read=dict_deal(a_read)#总阅读人数dict
out_f_read= dict_deal(f_read)#初次打开阅读人数
out_share=dict_deal(share)#分享次数
out_fans=dict_deal(fans)#每日增粉人数
x['总阅读人数']=out_a_read
x['初次打开阅读人数']=out_f_read
x['分享次数']=out_share
x['增粉数']=out_fans
xf=DataFrame(x)
#print xf
xf.plot( kind='barh')
xf.T.plot( kind='barh')
plt.show()



