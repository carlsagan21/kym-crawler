# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger('logger')
file_handler = logging.FileHandler('./info.log')
stream_handler = logging.StreamHandler()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


def crawl_oneday():
    headers = {'User-agent': 'Mozilla/5.0'}
    url_template = 'http://polisci.snu.ac.kr/bbs/view.php?id=kimym_dayone&no='
    for i in range(1, 100):
        url = url_template + str(i)
        try:
            html = requests.get(url, headers=headers).text
            soup = BeautifulSoup(html, 'html.parser')
            try:
                title = soup.find_all('td', class_='title_han')[0].contents[1].text

                try:
                    written_at_and_views = soup.find_all('td', class_='uks_eng')[0]
                    written_at = written_at_and_views.contents[0].split('\t')[1].split(',')[0]
                    views = written_at_and_views.contents[1].text

                    try:
                        content = soup.select('tr.list1 > td > table:nth-of-type(2) > tr > td')[0]
                        photo_list = content.find_all('p')
                        photos = []
                        for photo in photo_list:
                            photos.append(photo.contents[0].attrs['src'])
                        text = content.find('table').contents[1].contents[0].text

                        logger.info(
                            'title: {0} / written_at: {1} / views: {2} / photos: {3} / text: {4}'.format(title,
                                                                                                         written_at,
                                                                                                         views,
                                                                                                         str(
                                                                                                             photos),
                                                                                                         text))
                    except Exception as e:
                        logger.error('{0} Error: find content -> {1}'.format(str(i), str(e)))

                except Exception as e:
                    logger.error('{0} Error: find written_at -> {1}'.format(str(i), str(e)))

            except Exception as e:
                logger.error('{0} Error: find title -> {1}'.format(str(i), str(e)))

        except Exception as e:
            print('Error: request', e)
