import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st

# Hàm tìm kiếm trên Amazon
def search_amazon(query):
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  driver.get(f"https://www.amazon.com/s?k={query}")
  time.sleep(3)  # Đợi trang tải xong
  results = []
  items = driver.find_elements(By.CSS_SELECTOR, ".s-result-item")
  for item in items:
      title_element = item.find_element(By.CSS_SELECTOR, "h2 .a-link-normal")
      if title_element:
          title = title_element.text
          link = title_element.get_attribute("href")
          results.append({"title": title, "link": link})
  driver.quit()
  return results

# Hàm tìm kiếm trên eBay
def search_ebay(query):
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  driver.get(f"https://www.ebay.com/sch/i.html?_nkw={query}")
  time.sleep(3)  # Đợi trang tải xong
  results = []
  items = driver.find_elements(By.CSS_SELECTOR, ".s-item")
  for item in items:
      title_element = item.find_element(By.CSS_SELECTOR, ".s-item__title")
      if title_element:
          title = title_element.text
          link = item.find_element(By.CSS_SELECTOR, ".s-item__link").get_attribute("href")
          results.append({"title": title, "link": link})
  driver.quit()
  return results

# Hàm tìm kiếm trên Bookbuy.vn
def search_bookbuy(query):
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  driver.get(f"https://www.bookbuy.vn/search?q={query}")
  time.sleep(3)  # Đợi trang tải xong
  results = []
  items = driver.find_elements(By.CSS_SELECTOR, ".product-item")
  for item in items:
      title_element = item.find_element(By.CSS_SELECTOR, ".product-title a")
      if title_element:
          title = title_element.text
          link = title_element.get_attribute("href")
          results.append({"title": title, "link": link})
  driver.quit()
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
