from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


@app.route('/resume')
def resume():
    pass


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/mailing', methods=['POST'])
def mail():
    msg = Message("Hello",
                  sender="brenno_ribeiro@my.uri.edu",
                  recipients=["brenno_ribeiro@my.uri.edu"])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)
    return True


if __name__ == '__main__':
    app.run(debug=True)
