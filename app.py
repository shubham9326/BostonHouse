from flask import Flask,request,render_template

app=Flask(__name__)
@app.route('/')
def Home():
    return render_template('templates/index.html')


if __name__=="__main__":
    app.run(debug=True)