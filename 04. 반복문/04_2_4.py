character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
        },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }

for key in character:
    if type(character[key]) is str:
        print("{} : {}".format(key, character[key]))
    elif type(character[key]) is list:
        for i in character[key]:
            print("{} : {}".format(key, i))
    elif type(character[key]) is dict:
        for i in character[key]:
            print("{} : {}".format(i, character[key][i]))
    else:
        print("{} : {}".format(key, character[key]))
