import urllib

def read_text():
    quotes = open("F:\OOP\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    # print(output)
    connection.close()
    if "true" in output:
        print("用语警告！")
    elif "false" in output:
        print("本文用语无问题！")
    else:
        print("无法正常浏览文档！")

read_text()