

def get_next_target(self):
    start_link = self.find('<a href=')                   # 找到链接所在位置
    start_quote = self.find('"', start_link)             # 链接前引号位置
    end_quote = self.find('"', start_quote + 1)          # 链接结尾的引号
    url = self[start_quote+1 : end_quote]                # 输出引号之间的内容
    return url, end_quote


