from bs4 import BeautifulSoup


def crawl_oneday():
    soup = BeautifulSoup('http://polisci.snu.ac.kr/bbs/view.php?id=kimym_dayone&no=2', 'html.parser')
    soup