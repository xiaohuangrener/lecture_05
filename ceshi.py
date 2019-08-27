import pandas as pd
from ceshi_tool import inspect_data,process_missing_data,visualize_attributes,\
                       visualize_attributes_stats

csv_data_path = "./starcraft.csv"

def ceshi():
    #step1:load data
    df_data = pd.read_csv(csv_data_path)

    #step2:inspect data
    inspect_data(df_data)

    #step3:process missing data -- drop or fill
    df_data = process_missing_data(df_data)

    #step4:visualize attributes
    column_names = ['LeagueIndex',  # 战队索引号
                    'HoursPerWeek',  # 每周游戏时间
                    'Age',  # 战队中玩家的年龄
                    'APM',  # 手速
                    'WorkersMade'  # 单位时间的建造数
                    ]
    visualize_attributes(df_data[column_names])

    visualize_attributes_stats(df_data[column_names],'APM')

if __name__ == "__main__":
    ceshi()