body = {
    'name': 'keh',
    'age': 26,
    'haja': "init_list",
    'indict': {
        'name': 'keh',
        'age': 26,
        'haja': ['我是中国人，我爱我的祖国。', '2048', 'and']
    }
}

# --------------------------------------   数据查询操作   --------------------------------------

# 查询所有
query_all = {
    "query": {
        # match_all 查询--可以查询到所有文档，是没有查询条件下的默认语句。
        "match_all": {}
    }
}

match_query = {
    "query": {
        # match 查询--标准查询，不管你需要全文本查询还是精确查询基本上都要用到它。
        # 做精确匹配搜索时，你最好用过滤语句，因为过滤语句可以缓存数据。
        "match": {
            "about": "rock"
        },
        # multi_match 查询--match查询的基础上同时搜索多个字段，在多个字段中同时查一个
        "multi_match": {
            "query": 'music',
            "fields": ["about", "interests"]
        }
    }
}

single_filter_query = {
    "query": {
        "bool": {
            "must_not": {
                "exists": {
                    "field": "name"
                }
            },
            "filter": [
                {
                    "term":
                        {
                            "new_type": 0
                        }
                },
                {
                    "terms": {
                        'hero_type': [1, 2]
                    }
                },
                {
                    "range": {
                        'ename': {
                            "gt": 50,
                            "lte": 350
                        }
                    },
                }
            ]
        }
        # "term": {
        #     "skin_img_data": ""
        # },
    }
}

multiple_filter_query = {
    "query": {
        #
        # # wildcards 查询--使用标准的shell通配符查询
        # "wildcard": {
        #     "skin_name": "冰*"
        # },
        # # regexp 查询
        # "regexp": {
        #     "skin_name": ".雪.*"
        # },
        # # prefix 查询 -- 以什么字符开头的
        # "prefix": {
        #     "skin_name": "冰"
        # },

        # term 过滤--term主要用于精确匹配哪些值，比如数字，日期，布尔值或 not_analyzed 的字符串(未经切词的文本数据类型)

        # terms 允许指定多个匹配条件。

        # range 过滤--按照指定范围查找一批数据  gt : 大于 | gte : 大于等于 | lt : 小于 | lte : 小于等于

        # exists 和 missing 过滤--查找文档中是否包含指定字段或没有某个字段，类似于SQL语句中的IS_NULL条件

        # bool 过滤 ---- 合并多个过滤条件查询结果的布尔逻辑
        # must :: 多个查询条件的完全匹配,相当于 and。
        # must_not :: 多个查询条件的相反匹配，相当于 not。
        # should :: 至少有一个查询条件匹配, 相当于 or。

        # bool 查询 ---- 与 bool 过滤相似，用于合并多个查询子句。不同的是，bool 过滤可以直接给出是否匹配成功，
        # 而bool 查询要计算每一个查询子句的 _score （相关性分值）
        "bool": {
            "must": {
                # "term": {
                #     "skin_name": "雪"
                # },
                "multi_match": {
                    "query": "之",
                    "fields": ["skin_name", "cname"]
                }

            },
            "must_not": {
                "exists": {
                    "field": "name"
                }
            },
            "should": [
                {
                    "term": {
                        'hero_type': 3
                    }
                },
                {
                    "term": {
                        'ename': 4
                    }
                },
            ],
            "minimum_should_match": 0,
            "filter": [
                {
                    "term":
                        {
                            "new_type": 0
                        }
                },
                {
                    "terms": {
                        'hero_type': [1, 2]
                    }
                },
                {
                    "range": {
                        'ename': {
                            "gt": 50,
                            "lte": 350
                        }
                    },
                }
            ]
        }
    },

    # 切片式查询
    "from": 0,  # 从第0条数据开始
    "size": 200,  # 获取200条数据
    # 排序
    "sort": {
        "ename": {  # 根据ename字段升序排序
            "order": "desc"  # asc升序，desc降序
        }
    }
}

# --------------------------------------   数据更新操作   --------------------------------------

# 根据ID更新


doc_body1 = {
    'script': "ctx._source.remove('age')"
}

# 增加字段
doc_body2 = {
    'script': "ctx._source.address = '合肥'"
}

# 修改部分字段
doc_body3 = {
    "doc": {"last_name": "xiao"}
}

# update_by_query：更新满足条件的所有数据，写法同上删除和查询
query = {
    "query": {
        "match": {
            "last_name": "xiao"
        }
    },
    "script": {
        "source": "ctx._source.last_name = params.name;ctx._source.age = params.age",
        "lang": "painless",
        "params": {
            "name": "wang",
            "age": 100,
        },
    }

}

if __name__ == '__main__':
    from common.esdb import *

es = EsOperation('http://192.168.0.178')
print(es)

index = 'skins'
a = es.query_data(index, multiple_filter_query)
# print(len(a))
print(a)
