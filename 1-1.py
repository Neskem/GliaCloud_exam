def order_pick(files, top):
    for i in range(top):
        print(files[i][0] + ' ' + str(files[i][1]))


def file_counting(urls):
    d = dict()
    for url in urls:
        file_name = url.split('/')[-1]
        if file_name in d:
            d[file_name] += 1
        else:
            d[file_name] = 1
    return sorted(d.items(), key=lambda kv: -kv[1])


def main():
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]
    top = 3
    counting_urls = file_counting(urls)
    order_pick(counting_urls, top)


if __name__ == '__main__':
    main()