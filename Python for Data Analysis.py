# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Python for Data Analysis

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm

b = [1, 2, 3]


# +
# b?

# +
# print?
# -

def add_numbers(a, b):
    '''
    Add two numbers together
    
    Returns
    -------
    the_sum : type of arguments
    '''
    
    return a + b


# +
## ??를 사용하면 가능한 경우 함수의 소스 코드도 보여준다.
# add_numbers??

# +
## *load*? 할 경우 모든 함수 목록을 가져올 수 있다.
# np.*load*?

# +
s = 'python'

list(s)
# -

s[:3]   # 슬라이싱 이라고 부르는 s[:3] 문법 

s = '12\\34'   # 역슬래시(\)는 이스케이프 문자 특수한 목적의 문자를 나타내기 위해 사용.
print(s)

# 두 문자열을 더하면 두 문자 열이 이어붙인 새로운 문자열이 생성
a = 'this is the first half '
b = 'and this is the second half'

a + b

# ## 날자와 시간

# +

from datetime import datetime, date, time
# -

dt = datetime(2011, 10, 29, 20, 30, 21)

dt.day

dt.minute

# strftime 메서드는 datetime을 문자열로 만들어줌
dt.strftime('%m/%d/%Y %H:%M')

# ## 흐름 제어

x = 0

## if 문은 조건을 검사하여 그 조건이 True일 경우 if 블록 내의 코드를 수행한다.
if x < 0:
    print("It's negative")

if x < 0 :
    print("it's negative")
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('positive but smller than 5')
else:
    print('positive and larger than or equal to 5')
