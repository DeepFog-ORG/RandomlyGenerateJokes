import random

# 定义四个列表，分别存储笑话的开头、中间、结尾和关联词
joke_beginnings = ["为什么", "怎么样才能", "有一个人问我", "听说", "有一个笑话是这样的"]
joke_middles = ["因为", "所以", "但是", "然后"]
joke_endings = ["结果他就傻眼了", "你猜是谁", "哈哈哈哈", "世界就变得美好了", "然后大家都笑了"]
joke_connectors = ["，", "。", "，所以", "，但是", "，然后"]

# 随机选择一个开头、中间、结尾和关联词，生成笑话
def generate_joke():
    beginning = random.choice(joke_beginnings)
    middle = random.choice(joke_middles)
    ending = random.choice(joke_endings)
    connector = random.choice(joke_connectors)
    if connector == "，所以":
        joke = beginning + "，" + middle + "，" + ending
    else:
        joke = beginning + connector + middle + connector + ending
    return joke

# 生成10个笑话
for i in range(10):
    print(generate_joke())
