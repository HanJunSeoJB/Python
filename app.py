from flask import Flask, render_template, request, jsonify, url_for
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import uuid
import time
from urllib.request import urlretrieve

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['instagramUrl']

        # 브라우저 창을 숨긴 채로 실행되도록 설정
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(10)
        
        # 이미지 다운로드
        filenames = []
        while True:
            image = driver.find_element(By.CSS_SELECTOR, "img[class*='x5yr21d']").get_attribute('src')
            filename = f"{uuid.uuid4().hex}.jpg"
            urlretrieve(image, f'static/images/{filename}')
            filenames.append(filename)
            
            try:
                button = driver.find_element(By.CLASS_NAME, "_afxw")
                button.click()
                time.sleep(5)
            except:
                break
                
        driver.close()

        return jsonify({'image_urls': [url_for('static', filename=f'images/{filename}') for filename in filenames]})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)




