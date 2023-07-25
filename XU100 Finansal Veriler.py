
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd

chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\\Users\gunay.comert\Desktop\pyFiles\chromedriver113.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
hisseListesi=['KMPUR', 'YEOTK', 'KONTR', 'MZHLD', 'YYLGD']
def main():
    dfs = []
    for i in hisseListesi:
        driver.get(f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={i}")

        ## CARİ DEĞERLER ##
        hisseAdi = aciklama = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl58_g_81d0c4e3_49e1_40c1_84ae_878b4c967bbb']/div/div[1]/div/div[1]/div[1]/div[1]/span")
        cdDict = [hisseAdi.text]
        for row in range(1, 11):
            aciklama = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d']/div[2]/div/table//tbody//tr[" + str(row) + "]//th")
            deger = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d']/div[2]/div/table//tbody//tr[" + str(row) + "]//td")
            cdDict.append(deger.text)

        df = pd.DataFrame([], columns=['SEMBOL','F/K','FD/FAVÖK','PD/DD','FD/Satışlar','Yabancı Oranı (%)','Ort Hacim (mn$) 3A/12A','Piyasa Değeri','Net Borç','Yurtdışı Çarpan İskontosu (%)','Halka Açıklık Oranı (%)'])  
        df.loc[len(df)] = cdDict
        dfs.append(df)
            
        ## MALİ TABLO ##
        for row in range(1, 4):
            aciklama = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl58_g_4ab017ec_4d0c_418b_8969_c9456348cd53']/div[2]/div/div/table//tbody//tr[" + str(row) + "]//td[1]")
            simdikiTarih = driver.find_element(By.XPATH, "//*[@id='select2-ddlMaliTabloFirst-container']")
            simdiki = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl58_g_4ab017ec_4d0c_418b_8969_c9456348cd53']/div[2]/div/div/table//tbody//tr[" + str(row) + "]//td[2]")
            oncekiTarih = driver.find_element(By.XPATH, "//*[@id='select2-ddlMaliTabloSecond-container']")
            onceki = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl58_g_4ab017ec_4d0c_418b_8969_c9456348cd53']/div[2]/div/div/table//tbody//tr[" + str(row) + "]//td[3]")
        
    driver.close()
    print(pd.concat(dfs))

if __name__ == '__main__':
    main()
## cd C:\Program Files\Google\Chrome\Application\ chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
