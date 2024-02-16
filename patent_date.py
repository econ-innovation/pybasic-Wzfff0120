#! /Applications/Python 3.12
import sys
import urllib.request
import json

def patent_date(input_file, output_file):
    with open(input_file, "r") as file:
        for pt in file.readlines():
            patent = json.loads(pt)
            ipc = patent.get('ipc', '')
            filing_date = patent.get('filing_date',
                                     '')  # filing_date = patent["filing_date"]与filing_date = patent.get('filing_date', '')有什么区别呢
            publication_date = patent.get('publication_date', '')
            grant_date = patent.get('grant_date', '')
            priority_date = patent.get('priority_date', '')
            with open(output_file, "a") as fo:
                fo.write(f'{filing_date}|{publication_date}|{grant_date}|{priority_date}\n')

if __name__ == '__main__': #当patent_date.py被运行时，该if语句下面的内容将被运行;参考：https://blog.csdn.net/yjk13703623757/article/details/77918633
    input_file = sys.argv[1]
    output_file = sys_argv[2]
    patent_date(input_file, output_file)

#命令行输入
#python3  patent_date.py "input_file" "output_file"