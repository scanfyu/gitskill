
url, endpos = get_next_target(page)

def get_next_target(page): # 寻找某页面的链接
    start_link = page.find('<a href=')                   # 找到链接所在位置
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)             # 链接前引号位置
    end_quote = page.find('"', start_quote + 1)          # 链接结尾的引号
    url = page[start_quote + 1:end_quote]                # 输出引号之间的内容
    return url, end_quote                                # 返回网页链接以及链接结尾

def crawl_web(seed): # 深度优先搜索 
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

def get_all_links(page):                             # 获取页面所有链接 调用get_next_target()
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:                                     # 若有链接则将链接加入links
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def add_to_index(index, keyword, url):                                        # 添加索引
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword])

get_all_links(get_page('https://xkcd.com/353/'))