import jieba
import jieba.analyse
import matplotlib.pyplot as plt

# 防止中文乱码
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

# 处理爬取的数据
txt = ''
with open('戴建业标题.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list1 = line.strip('\n').split('视频标题: ')
        list2 = str(list1[1]).split('播放量')
        txt = txt + str(list2[0])
txt2 = txt.strip('【戴建业】')

words  =  jieba.analyse.extract_tags(txt2, topK=10, withWeight=True, allowPOS=('ns', 'n', 'vn','nr'))  # 将名词存入列表（只取词频最高的前20位）
'''
counts = {}  # 构造字典，逐一遍历words中的中文单词进行处理，并用字典计数
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())  # 转换列表类型并排序  转换成键值对的元组形式
items.sort(key=lambda x: x[1], reverse=True)  # 以'值'排序

newitems = items[0:10:1]
# 转换成字典
tu = dict(newitems)
'''
tu = dict(words)
# 定义 x和 y的空列表，用于分别存放词语和权重
x = []
y = []
# 分别追加到x和y列表
for k in tu:
    x.append(k)
    y.append(tu[k]*100)  # 防止0的情况出现 使权重的展示更清晰可观
# 打印标题
plt.title('戴建业视频标题主题词')
# 打印x标签
plt.xlabel('主题词')
# 打印y标签
plt.ylabel('权重')
plt.xticks(rotation=0)
# 输出图表中间的文字各种格式的定义
for a, b in zip(x, y):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=12, )
# 以柱状形式打印图表
plt.bar(x, y, label='权重')
plt.legend()
# 图表展示
plt.show()

