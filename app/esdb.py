from elasticsearch import Elasticsearch
from elasticsearch import helpers
from common.utils import *
from get_data import *


class EsOperation(object):
    def __init__(self, host, port=9200, user='', pwd=''):
        self.es = self.get_conn(host, port, user, pwd)

    def __del__(self):
        self.es.close()

    def __repr__(self):
        return '连接成功'

    def get_conn(self, host, port=9200, user='', pwd=''):
        es = Elasticsearch(hosts=host, port=port, sniff_on_start=True,
                           sniff_on_connection_fail=True,
                           sniff_timeout=60,
                           http_auth=(user, pwd),
                           timeout=120)
        return es

    def insert_one_data(self, index, body={}, id=get_current_time_str() + get_random_str()):
        return self.es.index(index=index, doc_type="_doc", id=id, body=body)

    def insert_many_data(self, index: str, data_list: list):

        def get_chunked_data(data, length):
            for i in range(0, len(data), length):
                yield data[i:i + length]

        for chunk_list in get_chunked_data(data_list, 1000):
            actions = [
                {"_index": index, "_id": get_current_time_str() + get_random_str(), "_source": data}
                for data in chunk_list]
            a = helpers.bulk(self.es, actions)
            print(a[1])
        return True

    def delete_data(self, index, query=None, id=None):
        if id:
            return self.es.delete(index, id)
        return self.es.delete_by_query(index, body=query)

    def update_data(self, index, id=None, body={}):
        if id:
            return self.es.update(index, id, body=body)
        return self.es.update_by_query(index, body=body)

    def get_count(self, index, query=None):
        """
        获取满足条件的数据总数
        :param index:索引
        :param query:查询条件
        :return:数据总数
        """
        return self.es.count(index=index, body=query).get('count')

    def query_all_data(self, index, query, scroll='5m', size=1000):
        """
        获取所有满足条件的数据
        :param index:索引
        :param query:查询条件
        :param scroll:设置游标查询窗口保持时间，默认5分钟
        :param size:单次查询数量，默认1000条
        :return:查询结果集列表
        """
        result = []
        search_result = self.es.search(index=index, body=query, scroll=scroll, size=size)
        result = search_result.get("hits").get("hits")
        scroll_id = search_result["_scroll_id"]
        total = search_result["hits"]["total"]["value"]
        for i in range(int(total / size)):
            res = self.es.scroll(scroll_id=scroll_id, scroll=scroll)  # scroll参数必须指定否则会报错
            result += res["hits"]["hits"]
        return result


    def query_data(self,index, query):
        result = self.es.search(index=index, body=query)
        return result
