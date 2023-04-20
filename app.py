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
        image = driver.find_element(By.CSS_SELECTOR, "img[class*='x5yr21d']").get_attribute('src')
        driver.close()

        # UUID를 사용하여 고유한 파일 이름 생성
        filename = f"{uuid.uuid4().hex}.jpg"

        # 이미지를 서버에 다운로드
        urlretrieve(image, f'static/images/{filename}')

        return jsonify({'image_url': url_for('static', filename=f'images/{filename}')})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


