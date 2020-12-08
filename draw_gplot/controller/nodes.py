# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 20:44
# @Author  : keh123000
# @Email   : 26467568@qq.com
# @File    : nodes.py

from flask import Blueprint, render_template

nodes = Blueprint('nodes', __name__)


@nodes.route('/nodes/<int:node_id>', methods=['GET'])
def getNodes(node_id):
    return '获取指定节点信息'


@nodes.route('/nodes', methods=['POST'])
def addNode():
    return '新增节点信息'


@nodes.route('/nodes/<int:node_id>', methods=['GET'])
def getNodeById(node_id):
    return '获取指定节点信息'


@nodes.route('/nodes/<int:node_id>', methods=['PUT'])
def updateNode(node_id):
    return '修改节点信息'
