from flask import Flask, render_template, url_for, request, redirect
import csv
# flask use template to allow the server to send html file to the browser 

app = Flask(__name__)
print(__name__)

# use the route() decorator to tell Flask 
# what URL should trigger our function

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    # the parameter 'data' is a dictionary
    with open('database.txt', mode='a') as database:
        email= data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email},{subject}, {message}')
        

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

        

@app.route('/Submit_form', methods=['POST', 'GET']) # the browser want us to store, and get the data
def submit_form():
    if request.method == 'POST':
        try:
            # data = request.form['message']
            data = request.form.to_dict() 
            # convert all the form data transferred to dictionary
            # print(data)
            # write the data to the database.txt
            # write_to_file(data)

            write_to_csv(data)

            # return 'Form submitted!!'
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again! '

    #-----
    # return "Form is submitted!!" 






#---------

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/index.html')
# def my_home_index():
#     return render_template('index.html')

# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')

# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')

# @app.route('/work.html')
# def my_work():
#     return render_template('work.html')

# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')

#-----------

# @app.route('/<username>/<int:post_id>')   # trigerring route, every time hitting it, run the decorated function
# def hello_world(username = None, post_id = None):
#     # return 'Hello, Hana!!'
#     # print(url_for('static', filename='emo.ico'))

#     return render_template('index.html', nameee = username, post_id = post_id)






# @app.route('/about')   # trigerring route, every time hitting it, run the decorated function
# def about():
#     # return 'Hello, Hana!!'
#     return render_template('about.html')





# if __name__ == "__main__":
#     app.run(debug=True)

# http://127.0.0.1:5000; 
# the url or the address of laptop with port 5000

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)

