import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
def fetch_cpi_data():
    # 定义数据获取的时间范围
    start_date = "2018-01-01"
    end_date = datetime.today().strftime('%Y-%m-%d')

    # 从 FRED (Federal Reserve Economic Data) 获取 CPI 数据
    cpi = web.DataReader("CPIAUCSL", "fred", start_date, end_date)
    cpi = cpi.resample('Q').mean()  # 按季度重新采样计算平均值

    # 计算过去四个季度的通胀率（同比变化百分比）
    cpi['Inflation (%)'] = cpi['CPIAUCSL'].pct_change(periods=4) * 100

    # 返回最近四个季度的通胀数据
    return cpi.iloc[-4:]

if __name__ == "__main__":
    inflation_data = fetch_cpi_data()
    print(inflation_data)