import pandas as pd

ws = pd.read_csv("dark_souls2\csv\wepon_set.csv", encoding='utf-8')
wepon_set = ws.set_index('名前').T.to_dict(orient='list')
hed = pd.read_csv("dark_souls2\csv\head_data.csv", encoding='utf-8')
head = hed.set_index('名前').T.to_dict(orient='list')
bd = pd.read_csv("dark_souls2\csv\leg_data.csv", encoding='utf-8')
body = bd.set_index('名前').T.to_dict(orient='list')
had = pd.read_csv("dark_souls2\csv\hand_data.csv", encoding='utf-8')
hand = had.set_index('名前').T.to_dict(orient='list')
ld = pd.read_csv("dark_souls2\csv\leg_data.csv", encoding='utf-8')
leg = ld.set_index('名前').T.to_dict(orient='list')

select_lineage = (input("素性を選択してください >>"))
select_rh1 = (input("右手の１番目のスロットに装備するものを選んでください >>"))
select_rh2 = (input("右手の２番目のスロットに装備するものを選んでください >>"))
select_rh3 = (input("右手の３番目のスロットに装備するものを選んでください >>"))
select_lh1 = (input("左手の１番目のスロットに装備するものを選んでください >>"))
select_lh2 = (input("左手の２番目のスロットに装備するものを選んでください >>"))
select_lh3 = (input("左手の３番目のスロットに装備するものを選んでください >>"))
select_head = (input("頭装備を選んでください >>"))
select_body = (input("胴体装備を選んでください >>"))
select_hand = (input("腕装備を選んでください >>"))
select_leg = (input("下半身装備を選んでください >>"))
possible_weight = float(input("装備可能重量の上限を入力してください >>"))

right_hand1 = wepon_set
right_hand2 = wepon_set
right_hand3 = wepon_set
left_hand1 = wepon_set
left_hand2 = wepon_set
left_hand3 = wepon_set

# 素性
lineage = {
    "戦士":[12, 7, 6, 6, 5, 15, 11, 5, 5, 5],
    "騎士":[13, 12, 6, 7, 4, 11, 8, 9, 3, 6],
    "剣士":[12, 4, 8, 4, 6, 9, 16, 6, 7, 5],
    "野盗":[11, 9, 7, 11, 2, 9, 14, 3, 1, 8],
    "聖職者":[14, 10, 3, 8, 10, 11, 5, 4, 4,12],
    "魔術師":[11, 5, 6, 5, 12, 3, 7, 8, 14, 4],
    "探索者":[10, 7, 6, 9, 7, 6, 6, 12, 5, 5],
    "持たざるもの":[1, 6, 6, 6, 6, 6, 6, 6, 6, 6]
}

def equipment(num):
    return (
        right_hand1[select_rh1][num],
        right_hand2[select_rh2][num], 
        right_hand3[select_rh3][num],
        left_hand1[select_lh1][num],
        left_hand2[select_lh2][num],
        left_hand3[select_lh3][num],
        head[select_head][num],
        body[select_body][num],
        hand[select_hand][num],
        leg[select_leg][num])

def missing_ability(num, ability):
    return 0 if max(equipment(num)) - lineage[select_lineage][ability] < 0 else max(equipment(num)) - lineage[select_lineage][ability]

def required_ability(status, num, ability):
    print(f"必要{status}:{int(max(equipment(num)))}. "f"{status}{"は条件を満たしています" if missing_ability(num, ability) == 0 else "が" + str(missing_ability(num, ability)) + "足りません"}")

current_weight = float(sum(equipment(4)))
weight_per = current_weight / possible_weight * 100

print(f"素性：{select_lineage}")
print(f"装備重量: {weight_per:.1f}%")
required_ability("筋力", 0 ,5)
required_ability("技量", 1, 6)
required_ability("理力", 2, 8)
required_ability("信仰", 3, 9)
print(f"最低装備ステータスを満たすためのレベルは"f"{int(missing_ability(0, 5) + missing_ability(1, 6) + missing_ability(2, 8) + missing_ability(3, 9) + lineage[select_lineage][0])}です")