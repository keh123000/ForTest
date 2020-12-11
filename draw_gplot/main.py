from flask import Flask,render_template

img_b64code = ''
imgDataURI = 'data:image/png;base64,%s' % img_b64code


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port=1680)
