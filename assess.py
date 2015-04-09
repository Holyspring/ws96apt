#coding:utf-8
import pandas as pd
from pandas import DataFrame
from pylab import mpl
import matplotlib.pyplot as plt
from s106 import newdf_df
mpl.rcParams['font.sans-serif']=['SimHei'] #设置字体
mpl.rcParams['axes.unicode_minus']=False #编码
'''
newdf里有一个持续时间那么就是说在原始df填充后 包含唱衰的有5个,那么我需要找到最后一次唱衰的粉丝数
'''
newdf=newdf_df()[0]
dfgp_full=newdf_df()[1]
articlelist= newdf.index
#print dfgp_full
articlefq = {}.fromkeys((articlelist), 0)  # 创建一个默认字典
countdict = articlefq
##后面要用到粉丝数，所以先将粉丝数添加进去
#########################################################
for article in articlelist:
    for i in dfgp_full.values:
        if i[6]==article:
            countdict[article]=i[5]
newdf_dict=newdf.to_dict(outtype='dict')
newdf_dict['粉丝数']=countdict#将粉丝数添加到dict
newdf_df2=DataFrame(newdf_dict)
#print newdf_df2
#开始计算各种占比数
def per(a=0,b=0,c=None):
    dict={}
    row=0
    for index in newdf_df2.index:
        #newdf_df2已经固定不变
        data_row=newdf_df2.values[row]#当前index对应的行数据
        row+=1
        if c=='cb':
            assess_num=round((float(data_row[a])/(data_row[b]-data_row[1])*100),1)
        elif c=='eccb':
            assess_num=round((float(data_row[a]-data_row[b])/data_row[a]*100),1)
        else:
            assess_num=round((float(data_row[a])/data_row[b]*100),1)
        dict[index]=assess_num
    return dict
#print newdf_df2
#初次打开，初次打开读/粉丝数，1/6
#分享率,分享次数/总阅读,0/3
#分享拉粉率，每日增粉/分享次数,2/0
#增粉速率,每日增粉/粉丝数，2/6
#阅读涨粉率,每日增粉/总阅读，2/3
#传播涨粉率,每日增粉/（总阅读-初次打开），2/（3-1）
#二次传播率,（总阅读-初次打开）/总阅读，（3-1）/3
assess_dict={}
assess_dict['初次打开率']= per(a=1,b=6)
assess_dict['分享率']= per(a=0,b=3)
assess_dict['分享拉粉率']= per(a=2,b=0)
assess_dict['增粉率']= per(a=2,b=6)
assess_dict['阅读增粉率']= per(a=2,b=3)
assess_dict['传播涨粉率']= per(a=2,b=3,c='cb')
assess_dict['二次传播率']= per(a=3,b=1,c='eccb')
assess_df=DataFrame(assess_dict)

print assess_df
#no numeric data 刻度的问题，检查,刻度
assess_df.plot(kind='barh')
assess_df.T.plot(kind='barh')
plt.show()
