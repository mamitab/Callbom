from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

# Kullanıcıdan telefon numarasını al
phone_number = input("Lütfen telefon numaranızı girin: ")

# ChromeDriver yolunu belirtin
driver_path = 'path_to_chromedriver'  # Buraya ChromeDriver'ın yolunu yazın

# WebDriver'ı başlatın
driver = webdriver.Chrome(driver_path)

# Hedef siteye gidin
driver.get("https://www.nissan.com.tr/services/sizi-arayalim.html")

# Rastgele veri oluşturma fonksiyonları
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email():
    return random_string(5) + "@example.com"

# Kayıt alanlarını bulup doldurun
try:
    # İsim alanını bul ve doldur
    name_field = driver.find_element(By.ID, "firstname")
    name_field.send_keys(random_string())
    
    # Soyisim alanını bul ve doldur
    surname_field = driver.find_element(By.ID, "lastname")
    surname_field.send_keys(random_string())
    
    # E-posta alanını bul ve doldur
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(random_email())
    
    # Telefon numarası alanını bul ve kullanıcıdan alınan numara ile doldur
    phone_field = driver.find_element(By.ID, "phone")
    phone_field.send_keys(phone_number)
    
    # Şehir alanını bul ve doldur
    city_field = driver.find_element(By.ID, "city")
    city_field.send_keys(random_string())
    
    # Onay kutusunu bul ve işaretle
    consent_checkbox = driver.find_element(By.ID, "consent")
    consent_checkbox.click()
    
    # Gönder butonunu bul ve tıkla
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    # Başarılı bir şekilde gönderildiğini kontrol etmek için biraz bekleyin
    time.sleep(5)
finally:
    # Tarayıcıyı kapat
    driver.quit()
