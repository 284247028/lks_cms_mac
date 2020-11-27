from config import *
from methods import *
# coding=utf-8
import re
import os
import time
import requests
import tkinter as tk
from config import *
from methods import *
from tkinter import ttk
from tkinter import Menu
from tkinter import Spinbox
from datetime import datetime
from selenium import webdriver
from tkinter import scrolledtext
from tkinter import messagebox as mBox
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.common.action_chains import ActionChains

def cms(wangzhan):  # tt cc是内容、标题的列表
    df = res('/Users/lilong/Desktop/res/')
    tt = df[0]
    cc = df[1]
    # print(str_W_Con)
    # print('#'*100)
    # Body = {'txt': str_W_Con}  # 入参
    # res = requests.post(url_num, headers=headers, data=Body)  # 接口调用
    # resTest = json.loads(res.text)
    # Test = resTest['data']
    # cms(wangzhan,lanmu,tt,Test)
    # injection(shkqn_url, '82')
    driver_path = '/Users/lilong/Desktop/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)
    print('Tick! The time is: %s' % datetime.now())
    print(wangzhan)
    driver.get(wangzhan)  # 网站
    driver.find_element_by_name("userid").send_keys('ongwen')  # 用户名
    driver.find_element_by_name("pwd").send_keys('Little147258')  # 密码
    driver.find_element_by_name("sm1").click()  # 登录
    time.sleep(1)
    for title, content in zip(tt, cc):
        Body = {'txt': content}  # 入参
        res_api = requests.post(url_num, headers=headers, data=Body)  # 接口调用
        resTest = json.loads(res_api.text)
        Test = resTest['data']
        print(Test)


        # time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/ul/li[4]/a').click()  # 点击内容维护
        time.sleep(2)
        # 切换到iframe
        driver.switch_to.frame("main")  # 板块
        a = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/input[1]')  # 添加文档

        ActionChains(driver).move_to_element(a).click(a).perform()  # 行为链点击文档
        time.sleep(1)
        b = driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)  # 标题
        c = Select(driver.find_element_by_xpath('//*[@id="typeid"]'))  # 文章栏目位置
        d = c.select_by_value('82')  # 文章栏目索引
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # JS控制，window滚动条
        time.sleep(1)
        Ycode = driver.find_element_by_xpath('//*[@id="cke_8"]').click()  # 点击转换源码处
        driver.find_element_by_xpath('//*[@id="cke_contents_body"]/textarea').send_keys(Test)
        driver.find_element_by_xpath('/html/body/form/table[6]/tbody/tr/td[2]/input').click()  # 点击提交
        driver.switch_to.parent_frame()
    driver.quit()
    print("ok")
cms(shkqn_url)