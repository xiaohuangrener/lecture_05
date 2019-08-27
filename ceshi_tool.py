import matplotlib.pyplot as plt
import pandas as pd

def inspect_data(df_data):
    '''
    查看df_data基本信息
    :param df_data:
    :return:
    '''
    print("数据信息：")
    print(df_data.info())
    print("数据预览：")
    print(df_data.head())

def process_missing_data(df_data):
    '''
    处理缺失数据
    :param df_data:
    :return:df_data
    '''
    if df_data.isnull().values.any():
        df_data = df_data.fillna(0.)   #用0填充
        #df_data = df_data.dropna       删除NaN
    return df_data

def visualize_attributes(df_data,save_fig=True):
    fig = plt.figure(figsize=(10.0,5.0))
    axe1 = fig.add_subplot(2,2,1)
    axe2 = fig.add_subplot(2,2,2)
    axe3 = fig.add_subplot(2,2,3)
    axe4 = fig.add_subplot(2,2,4)

    axe1.scatter(df_data['LeagueIndex'],df_data['HoursPerWeek'],color='r')
    axe1.set_xlabel(u'战队')
    axe1.set_ylabel(u'每周游戏时间')

    axe2.scatter(df_data['LeagueIndex'],df_data['Age'],color='g')
    axe2.set_xlabel(u'战队')
    axe2.set_ylabel(u'年龄')

    axe3.scatter(df_data['LeagueIndex'], df_data['APM'],color='b')
    axe3.set_xlabel(u'战队')
    axe3.set_ylabel(u'APM')

    axe4.scatter(df_data['LeagueIndex'], df_data['WorkersMade'])
    axe4.set_xlabel(u'战队')
    axe4.set_ylabel(u'单位时间的建造数')

    if save_fig:
        plt.savefig("./league_attributes.jpg")
    plt.show()

def visualize_attributes_stats(df_data,attr,save_data=True,save_fig=True):
    '''
    可视化战队属性统计值
    :param df_data:
    :param save_data:
    :param save_fig:
    :return:
    '''
    league_indexs = range(1,9)
    stats_min = []
    stats_max = []
    stats_mean = []

    for league_index in league_indexs:
        filter_data = df_data.loc[df_data['LeagueIndex']==league_index,attr]
        stats_min.append(filter_data.min())
        stats_max.append(filter_data.max())
        stats_mean.append(filter_data.mean())

    league_indexs_series = pd.Series(league_indexs,name="League_Index")
    stats_min_series = pd.Series(stats_min,name="min")
    stats_max_series = pd.Series(stats_max, name="max")
    stats_mean_series = pd.Series(stats_mean, name="mean")

    df_results = pd.concat([league_indexs_series,stats_min_series,stats_max_series,stats_mean_series],axis=1)

    if save_data==True:
        df_results.to_csv("./df_results.csv",index=None)

