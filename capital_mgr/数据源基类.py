# -*- coding: utf-8 -*-
"""数据源基�?""

class DataSourceBase:
    """数据源基�?""
    
    def get_price(self, symbol):
        """获取价格"""
        raise NotImplementedError
    
    def get_kline(self, symbol, period):
        """获取K�?""
        raise NotImplementedError
