import os
import json
import base64
from PIL import Image
import wmi

import random
import string
from datetime import datetime

import json

from mongoengine.base import BaseDocument


# 将 MongoDB 的 document转化为dict形式
def convertMongoToDict(o):
    def convert(dic_data):
        # 对于引用的Id和该条数据的Id，这里都是ObjectId类型的
        from bson import ObjectId
        # 字典遍历
        for key, value in dic_data.items():
            # 如果是列表，则递归将值清洗
            if isinstance(value, list):
                for l in value:
                    convert(l)
            elif isinstance(value, datetime):
                dic_data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            else:
                if isinstance(value, ObjectId):
                    dic_data[key] = str(dic_data.pop(key))
        return dic_data

    def exec_doc_convert(o):
        """
        转化为son形式，son的说明，摘自官方
        SON data.
        A subclass of dict that maintains ordering of keys and provides a
        few extra niceties for dealing with SON. SON provides an API
        similar to collections.OrderedDict from Python 2.7+.
        """
        data = o.to_mongo()
        # 转化为字典
        data = data.to_dict()
        ret = convert(data)
        # # 将数据转化为json格式， 因json不能直接处理datetime类型的数据，故需要区分处理
        # ret = json.dumps(ret, cls=DateEncoder)
        return ret

    ret = None
    if isinstance(o, list):
        ret = []
        for obj in o:
            if isinstance(obj, BaseDocument):
                ret.append(exec_doc_convert(obj))
    elif isinstance(o, BaseDocument):
        ret = exec_doc_convert(o)

    # # 判断其是否为Document
    # if isinstance(o, BaseDocument):
    #     """
    #     转化为son形式，son的说明，摘自官方
    #     SON data.
    #     A subclass of dict that maintains ordering of keys and provides a
    #     few extra niceties for dealing with SON. SON provides an API
    #     similar to collections.OrderedDict from Python 2.7+.
    #     """
    #     data = o.to_mongo()
    #     # 转化为字典
    #     data = data.to_dict()
    #     ret = convert(data)
    # # 将数据转化为json格式， 因json不能直接处理datetime类型的数据，故需要区分处理
    # ret = json.dumps(ret, cls=DateEncoder)
    return ret


def get_current_time_str(fmt="%Y%m%d%H%M%S%f"):
    return datetime.now().strftime(fmt)


def get_random_str(length=5):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def change_ip():
    # Obtain network adaptors configurations
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # First network adaptor
    nic = nic_configs[0]
    print(nic)

    # IP address, subnetmask and gateway values should be unicode objects
    ip = u'192.168.0.168'
    subnetmask = u'255.255.255.0'
    gateway = u'192.168.0.1'

    # # Set IP address, subnetmask and default gateway
    # # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    # nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    # nic.SetGateways(DefaultIPGateway=[gateway])
    return 1


def convert_pic(src_fp, dst_fp=None, src_fmt='JPG', dst_fmt=None):
    if dst_fmt is None:
        dst_fmt = ['PNG']

    def convert(src_file, dst, dst_fmt: list):
        file_path, file_name = os.path.split(src_file)
        name, suffix = os.path.splitext(file_name)
        if suffix.strip('.').upper() == src_fmt:
            im = Image.open(src_file)
            for fmt in dst_fmt:
                dst_path = os.path.join(dst, fmt)
                if not os.path.exists(dst_path):
                    os.mkdir(dst_path)
                im.save(os.path.join(dst_path, name + '.' + fmt.lower()))

    if os.path.isfile(src_fp):
        file_path, file_name = os.path.split(src_fp)
        if not dst_fp:
            dst_fp = file_path
            convert(src_fp, dst_fp, dst_fmt)

    elif os.path.isdir(src_fp):
        if not dst_fp:
            dst_fp = src_fp
        for file in os.listdir(src_fp):
            src_file = os.path.join(src_fp, file)
            convert(src_file, dst_fp, dst_fmt)
    return 1


def get_b64code(fp):
    data = None
    if os.path.exists(fp):
        with open(fp, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            data = base64_data.decode()
    return data


# fp = 'D://DataCenter//tmp//fortest//img//AP.png'
# get_b64code(fp)


def read_json(fp):
    with open(fp, 'r') as f:
        load_dict = json.load(f)
        return load_dict


def write_json(fp, data):
    with open(fp, "w") as f:
        json.dump(data, f)
    return 1

#
# src_fp = 'D://DataCenter//tmp//fortest//img'
# for file in os.listdir(src_fp):
#     file_name,suffix = os.path.splitext(file)
#     data[file_name] = {
#         'b64code': '',
#         'url':''
#     }
#     src_file = os.path.join(src_fp, file)
#     data[file_name]['b64code'] = get_b64code(src_file)
#
#
# write_json(fp,data)

#
# a = read_json(fp)
# print(a['AP'])
