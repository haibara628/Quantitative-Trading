import akshare as ak

if __name__ == '__main__':
    # stock_sse_summary_df = ak.stock_sse_summary()
    # print(stock_sse_summary_df)

    stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
    print(stock_sh_a_spot_em_df)

    column_name = '代码'  # 例如 '代码', '名称', '最新价' 等

    # 获取指定列并转换为 list
    column_list = stock_sh_a_spot_em_df[column_name].tolist()
    print(column_list)

    stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
    print(stock_sz_a_spot_em_df)

    stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
    print(stock_bj_a_spot_em_df)

    stock_szse_summary_df = ak.stock_szse_summary(date="20200619")
    print(stock_szse_summary_df)

    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20240528',
                                            adjust="")
    print(stock_zh_a_hist_df)