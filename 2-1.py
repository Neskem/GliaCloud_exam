import aiohttp
import asyncio
import time

import requests
from bs4 import BeautifulSoup
import multiprocessing as mp


async def get_ptt_board(board, session):
    url = "https://www.ptt.cc/bbs/{}/index.html".format(board)
    r = await session.get(url)
    html = await r.text()
    await asyncio.sleep(0.1)
    return html


def get_article_content(article):
    url = "https://www.ptt.cc{}".format(article)
    html = requests.get(url=url)
    return html


def parse(board, html):
    board_article = list()
    soup = BeautifulSoup(html, "lxml")
    for article in soup.select(".r-ent"):
        post = dict()
        post['board'] = board

        # If the article has already been deleted, it can not find the title and content.
        if article.find('a') is not None:
            post['title'] = article.find('a').string
            url = article.find('a')['href']
            res_detail = get_article_content(url)
            if res_detail.status_code == 200:
                soup = BeautifulSoup(res_detail.text, "lxml")
                post['content'] = soup.find("div", {"id": "main-content"})
            else:
                post['content'] = None
        else:
            post['title'] = None
            post['content'] = None

        post['author'] = article.find('div', class_='author').string
        post['date'] = article.find("div", class_="date").string
        board_article.append(post)
        print(board_article)
    return board_article


async def main(loop):
    pool = mp.Pool(8)
    board = 'NBA'
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(get_ptt_board(board, session))]
        finished, unfinished = await asyncio.wait(tasks)
        htmls = [f.result() for f in finished]

        parse_jobs = [pool.apply_async(parse, args=(board, html,)) for html in htmls]
        pool.close()
        pool.join()

        return parse_jobs


if __name__ == "__main__":
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
    print("Async total time: ", time.time() - t1)