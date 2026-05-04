import numpy as np

class 绩效分析:
    @staticmethod
    def 计算夏普比率(收益率序�?:
        if len(收益率序�? == 0 or收益率序�?std() == 0:
            return 0
        return np.sqrt(252) * 收益率序�?mean() / 收益率序�?std()
    
    @staticmethod
    def 计算最大回�?权益曲线):
        if len(权益曲线) == 0:
            return 0
        累计最�?= np.maximum.accumulate(权益曲线)
        回撤 = (权益曲线 - 累计最�? / 累计最�?
        return float(回撤.min())
