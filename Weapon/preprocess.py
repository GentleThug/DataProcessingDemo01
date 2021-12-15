import re
from langconv import Converter

def quan_2_ban(sentence):
    """
    全角转半角
    :param argv:
    :return:
    """
    new_sentence = ''
    for uchar in sentence:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        # 转完之后不是半角字符返回原来的字符
        if inside_code < 0x0020 or inside_code > 0x7e:
            new_sentence += uchar
        else:
            new_sentence += chr(inside_code)
    return new_sentence

def lower_sen(sentence):
    """
    大写转小写
    :param argv:
    :return:
    """
    new_sentence = sentence.lower()
    return new_sentence

def ch_2_eng(sentence):
    """
    中文特殊符号批量识别并转为英文符号，避免后续全角转半角将引号转换了，英文双引号和单引号可以区分
    :param argv:
    :return:
    """
    ustring = sentence
    # 中文特殊符号批量识别
    pattern = re.compile('[，。！：“”【】？；、（）‘’『』「」﹃﹄〔〕—·]')
    fps = re.findall(pattern, ustring)
    # 对有中文特殊符号的文本进行符号替换
    if len(fps) > 0:
        ustring = ustring.replace('，', ',')
        ustring = ustring.replace('！', '!')
        ustring = ustring.replace('：', ':')
        ustring = ustring.replace('“', '"')
        ustring = ustring.replace('”', '"')
        ustring = ustring.replace('【', '[')
        ustring = ustring.replace('】', ']')
        ustring = ustring.replace('〈', '<')
        ustring = ustring.replace('〉', '>')
        ustring = ustring.replace('？', '?')
        ustring = ustring.replace('；', ';')
        ustring = ustring.replace('、', ',')
        ustring = ustring.replace('（', '(')
        ustring = ustring.replace('）', ')')
        ustring = ustring.replace('‘', "'")
        ustring = ustring.replace('’', "'")
        ustring = ustring.replace('’', "'")
        ustring = ustring.replace('『', "[")
        ustring = ustring.replace('』', "]")
        ustring = ustring.replace('「', "[")
        ustring = ustring.replace('」', "]")
        ustring = ustring.replace('﹃', "[")
        ustring = ustring.replace('﹄', "]")
        ustring = ustring.replace('〔', "{")
        ustring = ustring.replace('〕', "}")
        ustring = ustring.replace('—', "-")

    return ustring

def fan_2_jian(sentence):
    """
    简体转繁体
    :param argv:
    :return:
    """

    new_sentence = sentence.lower()
    new_sentence = Converter('zh-hans').convert(new_sentence)
    return new_sentence

def mainPreProcess(sentence):
    newsentence = ch_2_eng(sentence)
    newsentence = quan_2_ban(newsentence)
    newsentence = fan_2_jian(newsentence)
    return newsentence

print(quan_2_ban('我在吃饭。？！?!“"”“”‘’'))