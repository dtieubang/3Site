import requests
from bs4 import BeautifulSoup
import streamlit as st

# Hàm tìm kiếm trên Amazon
def search_amazon(query):
  url = f"https://www.amazon.com/s?k={query}"
  headers = {"User-Agent": "Mozilla/5.0"}
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, "html.parser")
  results = []
  for item in soup.select(".s-result-item"):
      title = item.select_one("h2 .a-link-normal")
      if title:
          title = title.get_text(strip=True)
          link = "https://www.amazon.com" + item.select_one("h2 .a-link-normal")["href"]
          results.append({"title": title, "link": link})
  return results

# Hàm tìm kiếm trên eBay
def search_ebay(query):
  url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  results = []
  for item in soup.select(".s-item"):
      title = item.select_one(".s-item__title")
      if title:
          title = title.get_text(strip=True)
          link = item.select_one(".s-item__link")["href"]
          results.append({"title": title, "link": link})
  return results

# Hàm tìm kiếm trên Bookbuy.vn
def search_bookbuy(query):
  url = f"https://www.bookbuy.vn/search?q={query}"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  results = []
  for item in soup.select(".product-item"):
      title = item.select_one(".product-title a")
      if title:
          title = title.get_text(strip=True)
          link = "https://www.bookbuy.vn" + item.select_one(".product-title a")["href"]
          results.append({"title": title, "link": link})
  return results

# Tạo giao diện người dùng với Streamlit
st.title("Product Search Dashboard")
query = st.text_input("Enter product name", "Xbox Series S 1TB")

if query:
  st.header("Amazon Results")
  amazon_results = search_amazon(query)
  for result in amazon_results:
      st.write(f"[{result['title']}]({result['link']})")

  st.header("eBay Results")
  ebay_results = search_ebay(query)
  for result in ebay_results:
      st.write(f"[{result['title']}]({result['link']})")

  st.header("Bookbuy.vn Results")
  bookbuy_results = search_bookbuy(query)
  for result in bookbuy_results:
      st.write(f"[{result['title']}]({result['link']})")
