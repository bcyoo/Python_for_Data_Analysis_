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

# # 흐름 제어

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

a = 5
b = 7
c = 8
d = 4

# +
if a < b or c > d:
    print('Made it')
    
## 예제에서 왼쪽 조건이 Ture이므로 오른쪽 c > d 조건은 검사하지않는다.
# -

# # for문

# +
for value in collection:
    # value를 이용하는 코드 작성
    
## for 문은 cotinue 예약어를 사용해서 남은 블록을 건너뛰고 다음 순회로 넘어 갈 수 있다.
## None 값은 건너 뛰고 리스트에 있는 모든 정수를 더하는 다음 코드를 살펴보자

# +
sequence = [1, 2, None, 4, None, 5]

total = 0

for value in sequence:
    if value is None:
        continue
    total += value
    
total

## for 문은 cotinue 예약어를 사용해서 남은 블록을 건너뛰고 다음 순회로 넘어 갈 수 있다.
## None 값은 건너 뛰고 리스트에 있는 모든 정수를 더한다

# +
sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for x in sequence:
    if x == 5:
        break
    total_until_5 += x

total_until_5

## for문은 braek 예악어를 사용해서 빠져날 수 있다. x가 sequence를 돌다가 5를 만나면 braek 하여
## 1, 2, 4, 6을 더하여 13의 결과값이 total_untile_5에 들어간다.
# -

## break 예약어는 가장 안쪽에 있는 for문만 빠져나감. 바깥쪽에 있는 for문은 계속 실행된다.
for i in range(4):
    for j in range(4):
        if j > i :
            break
        print((i, j))

# # while문

# +
## while문은 조건을 명시하여 해당 조건이 False가 되거나 break 문을 사용해서 
## 명시적으로 반복을 끝낼 때까지 블록 내의 코드를 수행함.

x = 256
total = 0

while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2

total
# -

# # pass

## pass는 아무 것도 하지 않음을 나타낸다.
## 블록내에 어떤 작업도 실행하지 않을 때 사용한다.
x = -2
if x < 0 :
    print('negative')
elif x == 0 :
    # 여기에 내용을 채울것
    pass
else : 
    print('positive')

range (10)

list(range(10))
