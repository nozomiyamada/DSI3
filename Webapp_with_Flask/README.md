# Web Application with `Flask`

example (my website) - created by `Flask`

- https://www.thaicorpus.net/

## virtual environment

virtual environment ตือคือสภาพแวดล้อม python ที่จะแยกแต่ละโปรเจคออกจาก python หลักที่อยู่ในคอม ซึ่งใช้เพื่อทดลองว่า app ที่สร้างจะสามารถทำงานที่อื่นได้หรือไม่

1. สร้าง virtual environment (ชื่อ `my_venv`) 
2. activate virtual environment
3. install packages with `pip install`

~~~bash
$ cd XX/XX  ## ย้ายไปที่ folder ที่จะสร้าง virtual environment)
$ python3 -m venv my_venv  ## สร้าง virtual environment
$ source .venv/bin/activate  ## activate virtual environment
(.venv) $ pip install flask  ## install package ต่างๆ
(.venv) $ pip install numpy
(.venv) $ pip install pandas
...
~~~

install package ที่ต้องการเสร็จแล้ว output เป็น `requirements.txt` 

~~~bash
(.venv) $ pip freeze > requirements.txt
~~~

เวลาตั้ง environment บน server ใช้ `requirements.txt` แล้ว install ได้ทีเดียว

~~~bash
(.venv) $ pip install -r requirements.txt
~~~

## packages ที่ต้องการเพื่อสร้าง app

- `flask`
- `gunicorn` (optional)
    - application server สำหรับ python
    - ไม่จำเป็น แต่มีดีกว่าตอนที่ deploy บน web

`pandas` มันกิน ram เยอะ (~500MB) ถ้าไม่จำเป็นก็ไม่ควรใช้


## directories 
~~~
(root directory)/
　├ my_venv/
　├ .gitignore  ## list of files ที่ไม้ต้องอัปโหลดโดย git
　├ static/  ## folder ที่จะใส่ static file เช่น `.jpg`
　├ templates/  ## folder ที่จะใส่ file `.html` 
　│　├ layout.html
　│　└ top.html
　├ requirements.txt  ## list of python packages
　├ run.sh  ## shell script ที่จะรันโปรแกรม (ไม่จำเป็น)
　└ app.py  ## main program
~~~

## `app.py`

~~~python
from flask import Flask, request, jsonify, render_template

## instantiate flask app
app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
    ) 

### top page ###
@app.route('/', methods=['GET', 'POST'])
def page_top():
    return render_template('toppage.html') # rendering "templates/toppage.html"

### second page ###
@app.route('/2', methods=['GET', 'POST'])
def page_second():
	if request.method == 'GET':
		return render_template('page2.html') # rendering "templates/page2.html"
	elif request.method == 'POST':
		text = request.form['input_text'].upper() # get text from form -> uppercase
		return render_template('page2.html', return_text=text) # re-rendering "page2.html" with variable "return_text"

### third page ###
@app.route('/3', methods=['GET', 'POST'])
def page_third():
    return render_template('page3.html') # rendering "templates/page3.html"

## word length page - return character length of the word as JSON
@app.route('/<word>', methods=['GET', 'POST'])
def page_length(word):
    return jsonify({'word': word, 'length': len(word)})

if __name__ == "__main__":
    # debug=True -> reload automatically when update app.py
    app.run(host="0.0.0.0", port=8000, debug=True)
~~~


## `jsonify` vs `render_template`

`jsonify()` จะ return ข้อมูลอย่างเดียว (เหมือน PokeAPI) 

ส่วน `render_template` จะให้ HTML file ที่พร้อมข้อมูลและ rendering เรียบร้อยแล้ว จึงใช้เวลานานกว่าส่งข้อมูลอย่างเดียว

ถ้าข้อมูลใหญ่ ควรส่งข้อมูลอย่างเดียวและให้ JavaScript เปลี่ยนเนื้อหาเว็บไซต์ (เช่น Ajax + vue.js)

## run application

~~~bash
$ source my_venv/bin/activate  ## activate 
(my_venv) $ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
~~~

หรือ `run.sh` (shell script ซึ่งมีคำสั่งข้างบน)

~~~bash
$ source run.sh
~~~

ใส่ `http://0.0.0.0:8000/` ใน URL bar 

## stop application 
- กด `CTRL+C` (win) or `command+C` (mac)
- แล้วพิมพ์ `deactivate`


## top page -> rendering page 

`http://0.0.0.0:8000/`

![toppage](https://user-images.githubusercontent.com/44984892/111415872-61cfbf80-8715-11eb-90f4-d711cbe3f5cd.png)

## second page -> rendering page & send form (POST method)

`http://0.0.0.0:8000/2`

![page2](https://user-images.githubusercontent.com/44984892/111420500-ea525e00-871d-11eb-9e5d-fbecc81c7b84.png)

## third page -> rendering page with static file

`http://0.0.0.0:8000/3`

![page3](https://user-images.githubusercontent.com/44984892/111420593-179f0c00-871e-11eb-9505-748dadf4d50e.png)

## any word after base URL -> return json 

`http://0.0.0.0:8000/(anyword)`

![anyword](https://user-images.githubusercontent.com/44984892/111415865-5ed4cf00-8715-11eb-967d-e5b24db1ee7b.png)
