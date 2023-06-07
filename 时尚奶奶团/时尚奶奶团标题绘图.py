import jieba
import jieba.analyse
import matplotlib.pyplot as plt

# 防止中文乱码
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

# 处理爬取的数据
txt = ''
with open('时尚奶奶团标题.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list1 = line.strip('\n').split('视频标题: ')
        list2 = str(list1[1]).split('播放量')
        txt = txt + str(list2[0])

words  =  jieba.analyse.extract_tags(txt, topK=15, withWeight=True, allowPOS=('ns', 'n', 'vn','nr'))  # 将名词存入列表（只取词频最高的前20位）

tu = dict(words)
# 定义 x和 y的空列表，用于分别存放词语和权重
x = []
y = []
# 分别追加到x和y列表
for k in tu:
    x.append(k)
    y.append(tu[k]*100)  # 防止0的情况出现 使权重的展示更清晰可观
# 打印标题
plt.title('时尚奶奶团视频标题主题词')
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
