from flask import Flask,render_template  #Flask 불러오기
app= Flask(__name__) ## Flask 생성

## decorator
@app.route('/') ## scheme:// domain.com:5000/path/to/somewhere?id=q122&pw=123....
                ## 127.0.0.1 => localhost 기본 경로로 라우팅 한 거
def helloworld():
    return render_template('index.html')
@app.route('/hello')
def hello():
    return 'Hello'

if __name__ =='__main__': ##  Flask 기본틀
    app.run()


