s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

words = dict()
for i in s.split():
	words[i] = words.get(i, 0) + 1
res = sorted(words.items(), key=lambda x: x[1], reverse=True)

word = [res[0]]
for k, v in res[1: ]:
	if word[0][1] == v:
		word.append((k, v))
# print(res)
print(sorted(word)[0][0])