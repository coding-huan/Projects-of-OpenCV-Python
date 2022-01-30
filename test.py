from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():
    return 'Hello world'


if __name__ == '__main__':
    print('切换分支到dev')
    app.run()
