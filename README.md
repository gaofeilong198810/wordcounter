# 简介
- 用于解决阅读英语小说时，单词不认识的尴尬情况
- 使用nltk统计英语小说中的单词频次，排除掉停词、地名、人名、已经认识的单词
- 统计结果可以按照单词出现的频次排序（倒序） or 按照单词出现的先后顺序排序

# 咋用
1. 把需要统计的英文单词书放在input目录下
2. resource下所有的文件都会被认为是黑名单，包括：书内的人名、地名、已经认识的单词等等
3. 执行（最后一个参数控制按照单词出现的顺序还是按照出现频次的顺序来排序）：
```
python word_counter.py input/bookname.txt output/wordfile.txt [WORD|COUNT]
```
# 目录说明
1. input：输入文件，要统计的书的文件
2. resource：黑名单，这里的单词不统计
3. output：统计结果

# 输出文件格式
单词，频次，词性

# requirs
- python 2.x or python 3+
- nltk

# how to manually download a nltk corpus
http://pan.baidu.com/s/1hq7UUFU

# contact me

email: 
gaofeilong198810@163.com

## merge command
```
join -a1 -o 1.1 2.1 c1s.txt youdaoss.txt 
```
