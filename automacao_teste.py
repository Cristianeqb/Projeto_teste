import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ChromeOptions


def test_sample_page():
    file_path = pathlib.Path(__file__).parent.resolve()

    options = ChromeOptions()
    # options.add_argument("--headless")  # Comente esta linha para visualizar o navegador
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    # Certifique-se de que o caminho e o nome do arquivo HTML estão corretos
    driver.get(f"file:///{file_path}/sample-exercise.html")
    generate_code(driver)
    sleep(5)
    
    code = driver.find_element(By.ID, "my-value")
    input_field = driver.find_element(By.ID, "input")
    input_field.clear()
    input_field.send_keys(code.text)
    
    test_btn = driver.find_element(By.NAME, "button")
    test_btn.click()

    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert result.text == f"It works! {code.text}!"

    driver.quit()


def generate_code(driver):
    generate = driver.find_element(By.NAME, "generate")
    generate.click()


