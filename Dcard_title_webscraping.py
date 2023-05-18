from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pandas as pd

if __name__ == '__main__':
    scroll_times = 5 # int 捲動次數
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions().add_argument("--headless")
    keyword = '台語歌'
    driver.get(f'https://www.dcard.tw/topics/{keyword}?latest=true') # 取得url    
    prev_elem = None
    results = []

    for times in range(scroll_times):
        WebDriverWait(driver, 2)
        sleep(3)
        elems = driver.find_elements(By.CLASS_NAME, 'atm_40_ncl75p')

        if prev_elem in elems:
            elems = elems[elems.index(prev_elem):]

        for elem in elems:
            result = {
                'title': elem.find_elements(By.CLASS_NAME, 'atm_cs_1urozh')[-1].text,
                'href': elem.find_elements(By.CLASS_NAME, 'atm_cs_1urozh')[-1].get_attribute('href'),
                'susbtitle': elem.find_elements(By.CLASS_NAME, 'atm_cs_aajkn3')[-1].text,
                'num_of_hearts': elem.find_elements(By.CLASS_NAME, 'atm_lk_i2wt44')[-1].text
                }
            results.append(result)
        
        prev_elem = elems[-1]
        print(f'now scroll {times+1}/{scroll_times}')
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        
    df = pd.DataFrame(results)

    with open(f'dcard_{keyword}.csv', 'w') as f:
        df.to_csv(f)

    driver.quit()
    