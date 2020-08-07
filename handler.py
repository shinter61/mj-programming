input_data = [
    ['m',1],
    ['m',2],
    ['m',3],
    ['m',4],
    ['m',5],
    ['m',6],
    ['m',7],
    ['m',8],
    ['m',9],
    ['p',2],
    ['s',3],
    ['s',2],
    ['s',1],
]

# リーパイ
def lipai (input_data):
    input_data.sort()
    return input_data

#　自動削除
def autodel (uniqed_array):
    return list(filter(lambda x: x[1] != 0, uniqed_array))

#　牌の定義
class Pai:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    def name(self):
        return self.color + str(self.number)
    def is_jihai(self):
        return self.number == 0

input_data = lipai(input_data)

# Paiオブジェクトに変換
pai_array = []
for raw_data in input_data:
    pai = Pai(raw_data[0], raw_data[1])
    pai_array.append(pai)

# 同じ牌を揃えて（牌、個数）のリストに変換
uniqed_array = []
for pai in pai_array:
    if pai.name() in list(map(lambda x: x[0].name(), uniqed_array)):
        target_index = list(map(lambda x: x[0].name(), uniqed_array)).index(pai.name())
        uniqed_array[target_index][1] += 1
    else:
        uniqed_array.append([pai, 1])
        
# print(uniqed_array)
'''
[
    [Pai(m2), 3],
    [Pai(m3), 2],
    [Pai(m4), 1],
    [Pai(m5), 2],
    [Pai(s1), 1],
    [Pai(s2), 1],
    [Pai(s3), 1],
    [Pai(w0), 2],
]
uniqed_array[0][0].color
'''

shunts_array = []
terts_array = []
korts_array = []
tanki_array = []
jantou_array = []

#刻子を保留させる


#順子を保留させる
first = uniqed_array[0][0]
last = uniqed_array[-1][0]

while len(uniqed_array) >= 2:
    first = uniqed_array[0][0]
    second = uniqed_array[1][0]
    third = uniqed_array[2][0]
    last = uniqed_array[-1][0]
    n = first.number
    c = first.color
    if not first.is_jihai() and c == second.color:
        if n+1 == second.number:
            terts_array.append([first, second]) #塔子をリストに保留
            if c == third.color and n+2 == third.number:
                shunts_array.append([first, second, third]) #順子をリストに保留
                uniqed_array[0][1] -= 1
                uniqed_array[1][1] -= 1
                uniqed_array[2][1] -= 1
                del terts_array[-1] #塔子リストから削除
            else:
                uniqed_array[0][1] -= 1
                uniqed_array[1][1] -= 1  #塔子をユニックから削除
        else:
            #カンチャンコース
            if n+2 == second.number:
                terts_array.append([first, second])
                uniqed_array[0][1] -= 1
                uniqed_array[1][1] -= 1  #塔子をユニックから削除
            else:
                if uniqed_array[0][1] == 1:
                    tanki_array.append(first) # 単騎待ちとして確保
                    uniqed_array[0][1] -= 1
                elif uniqed_array[0][1] == 2:
                    jantou_array.append(first) # 雀頭として確保
                    uniqed_array[0][1] -= 2

    uniqed_array = autodel(uniqed_array)


print('shunts_array')
print(list(map(lambda x: list(map(lambda y: y.name(), x)), shunts_array)))
print('terts_array')
print(list(map(lambda x: list(map(lambda y: y.name(), x)), terts_array)))
print('tanki_array')
print(list(map(lambda x: x.name(), tanki_array)))
print('jantou_array')
print(list(map(lambda x: x.name(), jantou_array)))


#ノーテン判定


#雀頭がある場合->順子に繋がるかを考える


#待ちを解析(リャンメン(0、10を除外)、カンチャン、シャボ)

print('待ち')
print('ノーテンやぞカス')

#雀頭がない場合->刻子を雀頭として考える->待ちを解析

print('待ち')
print('ノーテンやぞカス')
