import json
import urllib.request

information = {}

def book_parse(isbn):
    API_KEY = "AS1D3DN4"
    url = "http://isbndb.com/api/v2/json/{}/book/{}".format(API_KEY, isbn)
    url_price = "http://isbndb.com/api/v2/json/{}/prices/{}".format(API_KEY, isbn)
    book_price = urllib.request.urlopen(url_price).read().decode('utf-8')
    actual_book = json.loads(book_price)
    book_data = urllib.request.urlopen(url).read().decode('utf-8')
    actual = json.loads(book_data)
    #print(actual)
    information["cover"] = "http://covers.openlibrary.org/b/isbn/{}-L.jpg".format(isbn)
    information["amazon"] = "http://www.amzn.com/{}".format(isbn)
    information["ban"] = ""
    if "error" not in actual:
        information["title"] = actual["data"][0]["title"]
        information["publisher"] = actual["data"][0]["publisher_name"]
        information["author"] = actual["data"][0]["author_data"][0]["name"]
        information["isbn13"] = actual["data"][0]["isbn13"]
        information["price"] = actual_book["data"][0]["price"]
        if actual["data"][0]["summary"] == '':
            information["summary"] = "No Summary"
        else:
            information["summary"] = actual["data"][0]["summary"]
    else:
        information["summary"] = "eror"
        information["price"] = "error"
    information["ban"] = "http://www.barnesandnoble.com/s/{}".format(information["isbn13"])
    information["apple"] = "http://itunes.apple.com/us/book/{}".format(information["isbn13"])

def book_summary(isbn):
    return information["summary"]
def book_cover(isbn):
    return "http://covers.openlibrary.org/b/isbn/{}-L.jpg".format(isbn)
def book_title(isbn):
    return information["title"]
def book_publisher(isbn):
    return information["publisher"]
def book_author(isbn):
    return information["author"]
def book_price(isbn):
    return information["price"]
def book_amazon(isbn):
    return

def book_all(isbn):
    book_parse(isbn)
    return information