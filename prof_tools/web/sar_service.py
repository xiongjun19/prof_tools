# coding=utf8


import os
import json
from flask import request, Blueprint
import subprocess


route_entity = Blueprint('prof', __name__)
path_prefix_cpu = '/tmp/cpu_'


def exec_cmd(cmd_str):
    # cmd_args = shlex.split(cmd_str)
    # subprocess.call(cmd_args)
    print("shell cmd is: {0}".format(cmd_str))
    subprocess.call(cmd_str, shell=True)


@route_entity.route('/cpu_prof', methods=['POST', 'GET'])
def get_entity_info():
    sen_triple_info = request.json
    f_name = sen_triple_info.get("file_name")
    if f_name is None:
        result = {
            "status": 1,
            "msg": "没有解析到文件名字, 请检查传入的参数"
        }
        return json.dumps(result, ensure_ascii=False)

    _run_cpu_profile(f_name)
    result = {
        "status": 0,
        "msg": "starting to do sar profiling"
    }
    return json.dumps(result, ensure_ascii=False)


@route_entity.route('/stop_cpu_prof', methods=['POST', 'GET'])
def get_entity_info():
    sen_triple_info = request.json
    f_name = sen_triple_info.get("file_name")
    if f_name is None:
        result = {
            "status": 1,
            "msg": "没有解析到文件名字, 请检查传入的参数"
        }
        return json.dumps(result, ensure_ascii=False)
    _stop_cpu_profile(f_name)
    result = {
        "status": 0,
        "msg": {
            "log": "terminated the collection",
            "f_path":  path_prefix_cpu + f_name
            }
    }
    return json.dumps(result, ensure_ascii=False)



def _run_cpu_profile(f_name):
    out_path = path_prefix_cpu + f_name
    cmd = nohup sar -buqdp -r ALL -n DEV -P ALL  1 > {0} &.format(out_path)
    exec_cmd(cmd)

def _stop_cpu_profile(f_name):
    after_cmd = 'ps aux | grep sar | grep buqdp | awk \'{print $2}\' | xargs kill -9'
    exec_cmd(after_cmd)


