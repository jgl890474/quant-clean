"""
事件驱动系统的核�?
"""
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

class 事件类型(Enum):
    行情事件 = 1
    信号事件 = 2
    订单事件 = 3
    成交事件 = 4

@dataclass
class 行情事件:
    时间�? datetime
    代码: str
    开�? float
    最�? float
    最�? float
    收盘: float
    成交�? float
