# 题目：文本颜色设置。

# 终端的字符颜色是用转义序列控制的，是文本模式下的系统显示功能，和具体的语言无关;
# 书写过程如下：
# 开头部分: \033[显示方式;前景色;背景色m   这是三个可选参数。可以只写其中一个；
# 结尾部分: \033[0m
#
# 开头部分参数具体如下：
# 显示方式: 0（默认值）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
# 前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
# 背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）

class bcolors:
    HEADER = '\033[95m'#pink
    OKBLUE = '\033[94m'#blue
    OKGREEN = '\033[92m'#green
    WARNING = '\033[93m'#yellow
    FAIL = '\033[91m'#red
    ENDC = '\033[0m'#black
    BOLD = '\033[1m'#black+bold
    UNDERLINE = '\033[4m'#black+underline
print(bcolors.WARNING + "Which color do you like?" + bcolors.ENDC)
print('\033[95m%s\033[0m' % 'I like this color.')