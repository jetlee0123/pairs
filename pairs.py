# -*- coding: utf-8 -*-
import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By 

I=0

# xpathを定義してfind関数で要素をリストで取得
xpath_first_prof = '/html/body/div[1]/div[1]/main/ul/li[2]/div/div/a[3]/button'
## [>]ボタンのxpathは毎日変わる？（8/23のものが24日は使えず）
# xpath_next_prof = '/html/body/div[2]/div[10]/div/div[1]/div/div[3]/div[2]/a'
xpath_next_prof = '/html/body/div[2]/div[9]/div/div[1]/div/div[3]/div[2]/a'
xpath_block_ad = '/html/body/div[2]/div[7]/div/div[1]/div[2]/button'
xpath_close_button = '/html/body/div[2]/div[10]/div/div[1]/div/div[1]/button[1]' 

#get_element関数(要素を取得する)
def get_element(xpath, max_retry):
  I=0
  while I < max_retry:
        I=I+1
        try:
	  elems = chro.find_element_by_xpath(xpath)
	  break	
        except:
          #time.sleep(1)だと足跡が付いてない？(5000人やって足跡返しが少ない)
	  time.sleep(2) 
  return elems

#自動ログイン開始
#chro = webdriver.Chrome('/chromedriver')
chro = webdriver.Chrome('/Users/user/Desktop/pairs/chromedriver')
chro.get("https://pairs.lv/#/login")#Facebookページ遷移〜ペアーズログインページ遷移
#key = raw_input('ログイン後、pairsのトップページが出たらyを押してください')
#if key == "y":
# src= "https://pairs.lv/#/search/one/%s"%str(I)
# chro.get(src)

#広告を閉じる8/23に表示されていた広告が翌日に表示されず
## if(広告の有無)を条件判定として入れたい
# elems_block_ad = get_element(xpath_block_ad,30)
# elems_block_ad.click()

#画面を下までスクロール
Scroll_Count=0
while Scroll_Count < 30:
    time.sleep(random.randint(2,3))
    Scroll_Count+=1
    chro.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#1人目のプロフを開く
elems_first_prof = get_element(xpath_first_prof,50)
elems_first_prof.click()

#5０００人に到達するまで繰り返す（足跡間隔はランダムで5〜10秒の間）
time.sleep(4)

while I < 5000:
    I=I+1
    elems_next_prof = get_element(xpath_next_prof,50)
    elems_next_prof.click()
    print(str(I))     
else:
    print("5000人に足跡を付けました")
