import xlrd
import datetime
import time
import configparser
import json
import os

sleep = time.sleep


# 读取指定Excel文件，指定Sheet页内容
def read_xls(file_name="", sheet="", n_head=0, n_tail=0):
    """
    功能描述: 用于读取sheet页内容
    参数1 file_name: excel文件名
    参数2 sheet: sheet页名
    参数3 dir_path: 文件目录
    参数4 nHead: 开始行数, 默认为0
    参数5 nTail: 结束行数, 默认为0
    返回值: 返回sheet页内容的列表,列表里面套有多个元祖,每一个元祖的内容即为一行内容

    """
    datalist = []
    just_read_head = 0
    try:
        data = xlrd.open_workbook(file_name)
    except Exception as e:
        print(e)
    if sheet == "":
        table = data.sheet_by_index(0)
    else:
        table = data.sheet_by_name(sheet)
    # 行数
    nrows = table.nrows
    # 列数
    ncols = table.ncols
    datalist.clear()
    n = 0
    nFlag = 0
    nBegin = n_head
    nEnd = nrows - n_tail
    if just_read_head == 1:
        # 只读一行
        nEnd = nBegin + 1
    for rownum in range(nBegin, nEnd):
        row = table.row_values(rownum)
        if row:
            nLen = len(row)
            for i in range(nLen):
                ctp = table.cell(rownum, i).ctype
                if 3 == ctp:
                    # row[i] = xlrd.xldate.xldate_as_datetime(table.cell(rownum,i).value,1).strftime(
                    #     '%Y-%m-%d %H:%M:%S')
                    base_date = datetime.date(1899, 12, 31).toordinal() - 1
                    date = table.cell(rownum, i).value
                    # 若时间戳是浮点数，则转换为整数
                    if isinstance(date, float) and date:
                        date = int(date)
                        stamp = base_date + date
                        # 将时间戳转换为datetime格式
                        date = datetime.date.fromordinal(stamp)
                        # 转换为时间字符串
                        format_date = time.strftime('%Y-%m-%d', date.timetuple())
                    else:
                        format_date = None
                    row[i] = format_date
                elif ctp == 2 and row[i] % 1 == 0.0:
                    row[i] = int(row[i])
                    row[i] = str(row[i])

                elif 1 == ctp:
                    row[i] = row[i][0:3900]
                else:
                    row[i] = str(row[i])
            datalist.append(tuple(row))
            n = n + 1
            nFlag = nFlag + 1
            if nFlag == 5000:
                nFlag = 0
    return datalist


# 读取配置文件
def get_config_item(cfg_file='', section='', param='') -> str:
    """
    读取配置文件
    :param cfg_file: 配置文件全路径
    :param section:
    :param param: 需要提取的参数名
    :return: 提取的参数值
    """
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding="utf-8")
    return config.get(section, param) if param else config.items(section)


def read_config(fp):
    """"读取配置"""
    with open(fp) as json_file:
        config = json.load(json_file)
    return config


# 判断指定文件目录的指定文件是否存在
def judge_file_exist(file_path, file_name, wait_time=3, suffix=""):
    """
    判断指定文件目录的指定文件是否存在
    :param file_path: 指定文件目录
    :param file_name: 指定文件名
    :param wait_time: 给予的判断时间，默认为3秒
    :return: 判断结果，True 为存在，False 为不存在
    """
    result = False
    file_path = file_path.strip()
    try:
        i = 0
        if '.' in file_name:
            _namme = file_name.split('.')[0]
        else:
            _namme = file_name
        # path = os.path.join(file_path, file_name)
        while i < wait_time:
            # for root, dirs, files in os.walk(file_path):
            files = os.listdir(file_path)
            for j in range(len(files)):
                file = files[j]
                if '.' in file:
                    the_namme = file.split('.')[0]
                    suffix_ = file.split('.')[-1]
                    if suffix:
                        if suffix == suffix_:
                            if _namme in the_namme:
                                result = True
                                break
                    else:
                        if _namme in the_namme:
                            result = True
                            break
                else:
                    if _namme in file:
                        result = True
                        break
            if result:
                break
            else:
                sleep(1)
                i = i + 1
    except Exception as e:
        print('文件存在判断出现异常，异常原因如下：')
        print(e)
    return result
