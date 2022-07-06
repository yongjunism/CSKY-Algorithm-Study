import requests
from bs4 import BeautifulSoup
base = 'https://www.acmicpc.net/problem/'
import os

while True:
    print('문제 번호를 입력하세요. 중단하려면 n을 입력하세요.')
    num = input()
    if num == 'n' or num == 'N':
        break
    url = base + num
    print(url)

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("span", id="problem_title").get_text()
        sample_i = soup.select("pre[id^=sample-input]")

        quote = "'"
        os.system(f"mkdir \"BOJ {num} - {title}\"")
        os.system(f"echo import sys > \"BOJ {num} - {title}/BOJ_{num}.py\"")
        # os.system(f"echo sys.stdin = open\(\'input1.txt\'\) >> \"BOJ {num} - {title}/BOJ_{num}.py\"")
        # os.system(f"echo sys.stdin = open\({quote}input1.txt{quote}\) >> \"BOJ {num} - {title}/BOJ_{num}.py\"")
        os.system("echo sys.stdin = open\({0}input1.txt{1}\) >> \"BOJ {2} - {3}/BOJ_{4}.py\"".format(quote, quote, num, title, num))

        for i in range(len(sample_i)):
            for text_i in sample_i[i].text.strip().split('\n'):
                os.system(f"echo {text_i} >> \"BOJ {num} - {title}/input{i+1}.txt\"")

    else:
        print(response.status_code)
        break
