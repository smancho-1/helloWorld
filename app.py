from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Sarah Mancho! I am adding first code change.'
@app.route('/hello/')
def hello():
    return render_template('hello.html')
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/about-css/')
def about_css():
    return render_template('about-css.html')
@app.route('/favorite-course', methods=['GET','POST'])
def favorite_course():
    print(f'Subject: {request.form.get("subject")}')
    print(f'Course_number: {request.form.get("course_number")}')
    return render_template('favorite-course.html')
@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
