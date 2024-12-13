#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-12 12:08
# @Desc   : 调用智谱GLM4 API
# --------------------------------------------------------
"""
import os
from dotenv import load_dotenv, find_dotenv
from zhipuai import ZhipuAI


def kk_get_api_key():
    """使用本地环境变量获得api_key"""
    load_dotenv(find_dotenv())
    api_key = os.getenv("ZHIPU_API_KEY")
    return api_key


def kk_get_glm_params(prompt: str):
    """
    构造GLM请求参数messages
    params: prompt 用户输入的prompt
    """
    messages = [
        {"role": "user", "content": prompt}
    ]
    return messages

def kk_get_glm_completions(prompt, model="glm-4v-flash", temperature=0.3):
    """
    调用智谱GLM4 API，获取大模型调用结果
    params: prompt 用户输入的prompt
    model: 模型名称
    temperature: 温度
    """
    messages = kk_get_glm_params(prompt)
    response = client.chat.completions.create(model=model, messages=messages, temperature=temperature)
    if len(response.choices) > 0:
        return response.choices[0].message.content
    else:
        return "模型调用失败"


if __name__ == "__main__":
    # 初始化智谱AI客户端
    client = ZhipuAI(api_key=kk_get_api_key())
    print(kk_get_glm_completions("请告诉我如何开始学习中国历史？有哪些书籍可以推荐？"))
