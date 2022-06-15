import requests
from bs4 import BeautifulSoup
import os

base = 'https://www.acmicpc.net/problem/'

while True:

    print('문제 번호를 입력하세요. 중단하려면 1을 입력하세요.')
    num = input()
    if num == '1' or num == 'n':
        break
    url = base + num
    print(url)
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find("span", id="problem_title").get_text()
        sample_i = soup.select("pre[id^=sample-input]")

        os.system(f"mkdir \"BOJ {num} - {title}\"")
        os.system(f"echo import sys > \"BOJ {num} - {title}/BOJ_{num}.py\"")
        os.system(f"echo sys.stdin = open('input1.txt') >> \"BOJ {num} - {title}/BOJ_{num}.py\"")

        for i in range(len(sample_i)):
            for text_i in sample_i[i].text.strip().split('\n'):
                os.system(f"echo {text_i} >> \"BOJ {num} - {title}/input{i + 1}.txt\"")

    else:
        print(response.status_code)
        break