#coding:utf-8
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
def newdf_df():
    df = pd.ExcelFile("wxgzhdata.xlsx").parse(u"3月")
    articlelist = [ u'移动APP',u'魔都',u'手机浏览器',u'唱衰',u'大公司创新',u'大佬']  # 个别数据处理只能 case by case
    # 根据内容给计算器计数
    def countbytitle(contents):
        for article in articlelist:
            try :
                contents.index(article) # 主题名字都是原标题的一部分
                countdict[article]+=1
                return article
            except :
                pass

    # 计算每个主题系列包含的篇幅
    articlefq = {}.fromkeys((articlelist), 0)  # 创建一个默认字典
    countdict = articlefq  # apply 传递多个参数不会，只好用全局变量了
    df[u'文章标题'].apply(countbytitle)

    # 数据清洗，不能放前面
    dfgp = df   # 还是保留原数据不动
    dfgp = dfgp.fillna(method="pad")  # 空数据填充
    dfgp = dfgp.dropna()  # 删除掉还是空的数据
    dfgp_full=dfgp
    # 计算每个主题系列占据的阅读天数
    articlehis = {}.fromkeys((articlelist), 0)
    countdict = articlehis
    dfgp[u'文章标题'] = dfgp[u'文章标题'].apply(countbytitle)  # 文章题目合并

    # 计算每个主题一般汇总求和数据
    dfgp = dfgp.groupby(u'文章标题').sum()[[u'总阅读人数',u'初次打开阅读人数',u'分享次数',u'每日增粉人数']]

    # 把三个结果拼接成一个新的数据集
    newdf = pd.concat([dfgp,pd.Series(articlefq), pd.Series(articlehis)], axis=1)
    newdf.columns = ['总阅读','初次打开读','分享次数','增粉数','篇幅','持续时间']
    return newdf,dfgp_full

