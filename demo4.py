from bs4 import BeautifulSoup
import concurrent.futures
import requests
from tkinter import *

def scrape(urls):
    response = requests.get(urls)

    soup = BeautifulSoup(response.content, "lxml")

    # 爬取文章標題
    titles = soup.find_all("a", rel="mid_name")

    for title in titles:
        print(title.getText().strip())


def tt():
    base_url = "https://search.books.com.tw/search/query/cat/all/sort/1/v/0/page/"
    urls = [f"{base_url}{page}/key/{my_input.get()}" for page in range(1, 6)]  # 1~5頁的網址清單


    # 同時建立及啟用10個執行緒
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(scrape, urls)

root = Tk()

root.title("爬蟲")
root.geometry("800x800")

my_frame = Frame(root)
my_frame.pack(side=TOP)
my_label = Label(my_frame, text="想查詢的書")
my_label.pack(side=LEFT)
my_input = Entry(my_frame)
my_input.pack(side=LEFT)

btn = Button(root, text = "確認", command=tt)
btn.pack()

img_gif = PhotoImage(file = 'thread.gif')
label_img = Label(root, image = img_gif)
label_img.pack()

result_label = Label(root)
result_label.pack(pady=20)

root.mainloop()




