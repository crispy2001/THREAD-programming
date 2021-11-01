# THREAD-programming

## 設計
身為一個熱愛讀書，國家未來棟樑的我們，喜愛讀書。為了更快速查到我想要的書，而且不想看到煩人的廣告，我設計了一個在博客來的爬蟲:D


### 環境
python3

### 程式邏輯
使用者輸入想查的書 -> 程式去製造多個thread同時去抓五頁內的書 -> 印出到terminal來 

### 函式介紹
```python=
def tt():
    base_url = "https://search.books.com.tw/search/query/cat/all/sort/1/v/0/page/"
    urls = [f"{base_url}{page}/key/{my_input.get()}" for page in range(1, 6)]  
    # 1~5頁的網址清單


    # 同時建立及啟用10個執行緒
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(scrape, urls)
```
```python=
def scrape(urls):
    response = requests.get(urls)

    soup = BeautifulSoup(response.content, "lxml")

    # 爬取文章標題
    titles = soup.find_all("a", rel="mid_name")

    for title in titles:
        print(title.getText().strip())

```

#### UI的示意圖
![](https://i.imgur.com/sDJB6PU.png)


#### 程式補充說明
- 要裝lxml套件
- 使用Python3內建concurrent.futures模組的ThreadPoolExecutor類別，來同時啟動多個執行緒(Thread)
- 有爬蟲和沒爬蟲的比較
    - 我單純寫沒有thread的爬蟲的5頁查詢花了2.59s，而用了multi-thread的花0.9s。因為只有5頁不會差到很多，但實際上是看得出他的差距的。

## DEMO截圖
![](https://i.imgur.com/6H5JtyV.png)

![](https://i.imgur.com/I9zQRau.png)
