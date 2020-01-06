# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2630
# 색종이 만들기.


# return sum of all members of some specific matrix
def sum_range(matrix: tuple, size: int, index_i: int, index_j: int) -> int:
    """
    입력받은 전체 행렬(matrix) 에서 요소 (index_i, index_j) 에서 (index_i + size, index_j + size) 까지의 범위에 대해
    각 요소의 합을 구하여 리턴한다.
    :param matrix: tuple, 전체 매트릭스
    :param size: int, 특정 행렬의 크기
    :param index_i: int, 시작 행의 번호
    :param index_j: int, 시작 열의 번호
    :return: int, 행렬 요소의 합
    """
    _result = 0
    for _row in matrix[index_i:index_i + size]:
        for _col in _row[index_j:index_j+size]:
            # print(_row)
            # print(_col)
            _result += int(_col)
    return _result


# return result
def analyzed_result(matrix: tuple, size: int, check_point: tuple):
    _result = dict()
    _result['Zeros'] = 0
    _result['Ones'] = 0
    _result['Check_Again'] = list()
    for (index_i, index_j) in check_point:
        _sum_result = sum_range(matrix, size, index_i, index_j)
        if _sum_result == 0:
            _result['Zeros'] += 1
        elif _sum_result == size**2:
            _result['Ones'] += 1
        else:
            _result['Check_Again'].append((index_i, index_j))
    return _result


# 입력: N
# 입력: N x N

_numbers = tuple()
_dimension = int(str(input()))

# ***** take input *****
for _ in range(_dimension):
    _numbers += (tuple(input().replace(' ', '')),)

# print(_numbers)
# print(sum_range(_numbers, 4, 4, 4))

# print(analyzed_result(_numbers, 4, ((0, 0),)))  # {'Zeros': 0, 'Ones': 0, 'Check_Again': [(0, 0)]}
# print(analyzed_result(_numbers, 4, ((4, 4),)))  # {'Zeros': 0, 'Ones': 1, 'Check_Again': []}
# print(analyzed_result(_numbers, 2, ((6, 2),)))  # {'Zeros': 0, 'Ones': 1, 'Check_Again': []}

_answer = {'Zeros': 0, 'Ones': 0}
_check_point = ((0, 0),)

while _dimension >= 1:
    _analyzed = analyzed_result(_numbers, _dimension, _check_point)

    _answer['Zeros'] += _analyzed['Zeros']
    _answer['Ones'] += _analyzed['Ones']
    _dimension = int(_dimension / 2)

    if len(_analyzed['Check_Again']) > 0:
        _new_check_point = tuple(_analyzed['Check_Again'])  # 딕셔너리 앞에 tuple 처리를 하지 않으면 값을 참조하여 무한루프에 빠진다. 아주 중요했지만 지금에야 비로소...
        _check_point = _new_check_point
        for (_index_i, _index_j) in _new_check_point:  # 점검해야 할 포인트를 기준으로 N/2 만큼의 3 개의 포인트를 추가로 만든다 = 4등분
            _check_point += ((_index_i + _dimension, _index_j),)
            _check_point += ((_index_i, _index_j + _dimension),)
            _check_point += ((_index_i + _dimension, _index_j + _dimension),)


print(_answer['Zeros'])
print(_answer['Ones'])
