input_data = [
    ['m',1],
    ['m',1],
    ['m',1],
    ['m',2],
    ['m',3],
    ['m',4],
    ['m',5],
    ['m',6],
    ['m',7],
    ['m',8],
    ['m',9],
    ['m',9],
    ['m',9],
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
    def name_ja(self):
        color_ja = {
            'm': '萬',
            's': '索', 
            'p': '筒', 
            'b': '北', 
            't': '東', 
            'x': '西', 
            'n': '南', 
            'w': '白', 
            'r': '中', 
            'g': '発'
        }
        number_ja = {
            '0': '',
            '1': '一',
            '2': '二',
            '3': '三',
            '4': '四',
            '5': '五',
            '6': '六',
            '7': '七',
            '8': '八',
            '9': '九'
        }
        return number_ja[str(self.number)] + color_ja[self.color]
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
    [Pai(w0), 2], ] uniqed_array[0][0].color '''

shunts_array = []
terts_array = []
korts_array = []
tanki_array = []
jantou_array = []

# [[m1, 3], [m7, 3], [w0, 3]]
#刻子を保留させる
raw_korts = list(filter(lambda x: x[1] >= 3, uniqed_array))
korts_array = list(map(lambda x: x[0], raw_korts))
for korts in raw_korts:
    target_index = uniqed_array.index(korts)
    uniqed_array[target_index][1] -= 3
uniqed_array = autodel(uniqed_array)

# print('uniqed_array')
# print(uniqed_array)
#順子を保留させる
first = uniqed_array[0][0]
last = uniqed_array[-1][0]
while len(uniqed_array) >= 1:
    first = uniqed_array[0][0]

    if len(uniqed_array) == 1:
        if uniqed_array[0][1] == 1:
            tanki_array.append(first)
        elif uniqed_array[0][1] == 2:
            jantou_array.append(first)
        break

    second = uniqed_array[1][0]
    third = uniqed_array[2][0] if len(uniqed_array) > 2 else None
    last = uniqed_array[-1][0]
    n = first.number
    c = first.color
    # if not first.is_jihai() and c == second.color:
    if c == second.color:
        if n+1 == second.number:
            terts_array.append([first, second]) #塔子をリストに保留
            
            if third != None and c == third.color and n+2 == third.number:
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
    # elif not first.is_jihai() and c != second.color:
    elif  c != second.color:
        if uniqed_array[0][1] == 1:
            tanki_array.append(first) # 単騎待ちとして確保
            uniqed_array[0][1] -= 1

        elif uniqed_array[0][1] == 2:
            jantou_array.append(first) # 雀頭として確保
            uniqed_array[0][1] -= 2


    uniqed_array = autodel(uniqed_array)


print('korts_array')
print(list(map(lambda x: x.name(), korts_array)))
print('shunts_array')
print(list(map(lambda x: list(map(lambda y: y.name(), x)), shunts_array)))
print('terts_array')
print(list(map(lambda x: list(map(lambda y: y.name(), x)), terts_array)))
print('tanki_array')
print(list(map(lambda x: x.name(), tanki_array)))
print('jantou_array')
print(list(map(lambda x: x.name(), jantou_array)))


#ノーテン判定
if len(terts_array) >= 2:
    print('ノーテンにござるwwww')
    exit(1)
elif len(tanki_array) >= 2:
    print('ノーテンにござるwwww')
    exit(1)
elif len(jantou_array) >=3:
    print('あぁ^~~~ノーテンの音ぉwwww')
    exit(1)

#雀頭がある場合->順子に繋がるかを考える



#待ちを解析(リャンメン(0、10を除外)、カンチャン、シャボ)

#タンキニキ
if len(tanki_array) ==1:
    print(tanki_array[0].name_ja(), '待ちに候')
    
#シャボンヌ
if len(jantou_array) ==2:
    print(jantou_array[0].name_ja(),jantou_array[1].name_ja(), '待ちに候') 

#ターツンゴ
if len(terts_array) ==1:
    a = terts_array[0][0]
    b = terts_array[0][1]
    # カンチャンゴ
    if b.number - a.number == 2:
        pai = Pai(a.color, a.number + 1)
        print('カン' + pai.name_ja() + '待ちに候。クソ待ちに候')
    # リャンメンゴ
    elif b.number - a.number == 1:
        pai1 = Pai(a.color, a.number - 1)
        pai2 = Pai(a.color, b.number + 1)
        if pai1.number == 0:
            print('ペン' + pai2.name_ja() + '待ちに候。ペンちゃんとはもの好きよのう')
        elif pai2.number == 10:
            print('ペン' + pai1.name_ja() + '待ちに候。ペンちゃんとはもの好きよのう')
        else:
            print(pai1.name_ja(), pai2.name_ja() + '待ちに候')




#雀頭がない場合->刻子を雀頭として考える->待ちを解析


