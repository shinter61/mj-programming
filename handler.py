input_data = [
    ['m',4],
    ['s',1],
    ['s',1],
    ['s',1],
    ['w',0],
    ['w',0],
    ['w',0],
    ['m',2],
    ['m',4],
    ['m',2],
    ['m',3],
    ['m',4],
    ['m',2],
]

# リーパイ
input_data.sort()
print(input_data)

#　牌の定義
class Pai:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    def name(self):
        return self.color + str(self.number)

pai_array = []
for raw_data in input_data:
    pai = Pai(raw_data[0], raw_data[1])
    pai_array.append(pai)

uniqed_array = []
for pai in pai_array:
    if pai.name() in list(map(lambda x: x[0].name(), uniqed_array)):
        target_index = list(map(lambda x: x[0].name(), uniqed_array)).index(pai.name())
        uniqed_array[target_index][1] += 1
    else:
        uniqed_array.append([pai, 1])
        
print(uniqed_array)
'''
同じ値を数えて(数字,色,個数)のリストに変換
[
    [m,2,3],
    [m,3,1],
    [m,4,3],
    [s,1,3],
    [w,NUUUUUL,3],
]

'''

#刻子を保留させる


#順子を保留させる



#雀頭がある場合->順子に繋がるかを考える


#待ちを解析(リャンメン(0、10を除外)、カンチャン、シャボ)

print('待ち')
print('ノーテンやぞカス')

#雀頭がない場合->刻子を雀頭として考える->待ちを解析

print('待ち')
print('ノーテンやぞカス')
