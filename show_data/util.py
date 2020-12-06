import os
import json
import base64
from PIL import Image


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
            s = base64_data.decode()
            data = 'data:image/png;base64,%s' % s
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


fp = './img_data_mapping.json'

data = {
}

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
