import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def selectDate(date):
    dateArr = date.split('-')
    year = dateArr[0]
    month = str(int(dateArr[1]) - 1)
    day = dateArr[2]
    # 先点日期输入框，sb
    driver.find_element_by_id('dateOfBirthInput').click()
    # 下拉选择框
    Select(driver.find_element_by_class_name('react-datepicker__year-select')).select_by_value(year)
    Select(driver.find_element_by_class_name('react-datepicker__month-select')).select_by_value(month)
    time.sleep(1)
    # 日期选择
    dayArr = driver.find_elements_by_class_name('react-datepicker__day')
    for dayArrItem in dayArr:
        # 遍历并判断日期是否符合
        currentDay = dayArrItem.get_attribute('innerHTML')
        if (currentDay == day):  # int()将字符串强转成整数
            # 符合点击并推出循环
            dayArrItem.click()
            break

def selectSubject(data):
    # data : 单个或多个subject 名称
    # 点击 subject 文本框的整体，，他喵的居然是一堆div
    driver.find_element_by_class_name('subjects-auto-complete__control').click()
    # # 使用js 给div添加文本  你没用了 找到input了，啊哈哈哈哈哈
    # js="document.getElementByClassName(\"div的ID\").innerHTML=\"En\";"
    # driver.execute_script(js)
    for item in data:
        driver.find_element_by_id('subjectsInput').send_keys(item)
        driver.find_element_by_id('subjectsInput').send_keys(Keys.ENTER)

def selectWebBrowser():
    print("请选择想要调用并执行脚本的浏览器：")
    print("1. Chrome")
    print("2. Firefox")
    print("3. Edge")
    seleter = input()
    if seleter == '1':
        print("chrome")
        return webdriver.Chrome(executable_path=r'D:\Program Files (x86)\Python39\chromedriver.exe')
    elif seleter == '2':
        return webdriver.Firefox(executable_path=r'D:\Program Files (x86)\Python39\geckodriver.exe')
        print("firefox")
    elif seleter == '3':
        return webdriver.Edge(executable_path=r'D:\Program Files (x86)\Python39\msedgedriver.exe')
        print("edge")
    else:
        print("错误输入.....")
        return selectWebBrowser()

# 随便写点
conf = {'firstName': 'Aa123',
        'lastName': '123!@#$',
        'userEmail': 'test@gamil.com',
        'userNumber': '1234567890',
        'date': '1994-3-25'}


driver = selectWebBrowser()

driver.maximize_window()
driver.get("http://toolsqa.com/automation-practice-form/")
time.sleep(1)  # sleep一下好想不那么容易报错？
# 一顿乱输
driver.find_element_by_id('firstName').send_keys(conf['firstName'])
driver.find_element_by_id('lastName').send_keys(conf['lastName'])
# 害~ 单项选择框,用不了Select()
driver.find_elements_by_class_name('custom-control-label')[0].click()
driver.find_element_by_id('userNumber').send_keys(conf['userNumber'])
driver.find_element_by_id('userEmail').send_keys(conf['userEmail'])
# 日期的格式必须是 ’yyyy-MM-DD‘ ，问就是懒
selectDate(conf['date'])
# 输那些有的，别整那些花里胡哨的
selectSubject(['English', 'o'])

# # 不搞了，就这样吧  选择爱好
driver.find_element_by_xpath("//*[@id='hobbies-checkbox-1']").send_keys(Keys.SPACE)
driver.find_element_by_xpath("//*[@id='hobbies-checkbox-2']").send_keys(Keys.SPACE)
driver.find_element_by_xpath("//*[@id='hobbies-checkbox-3']").send_keys(Keys.SPACE)

# 得，简单粗暴   上传图片
driver.find_element_by_class_name('form-control-file').send_keys(r'C:\\Users\whale\Desktop\头图\风铃.jpg')

# 选择城市
driver.find_element_by_id('react-select-3-input').send_keys('NCR')
driver.find_element_by_id('react-select-3-input').send_keys(Keys.TAB)
driver.find_element_by_id('react-select-3-input').send_keys(Keys.TAB)
time.sleep(1)
driver.find_element_by_id('react-select-4-input').send_keys('De')
driver.find_element_by_id('react-select-4-input').send_keys(Keys.TAB)

time.sleep(1)
# 提交
driver.find_element_by_id('submit').click()


time.sleep(2)
driver.quit()