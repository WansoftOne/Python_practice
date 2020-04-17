from flask import Flask, render_template, request, flash, redirect
from contact_model import Contact

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True

@app.route(r'/' , methods=['GET'])
def contact_book():
    #show all contacts in the view
    contacts = []
    for i in range(10):
        contacts.append(
            Contact("name{}".format(i), "phone{}".format(i), "email{}".format(i))) 

    return render_template('contact_book.html', contacts=contacts)

@app.route(r'/add', methods=['GET','POST'])
def add_contact():
    if request.form:
        print(request.form.get('name'))
        print(request.form.get('phone'))
        print(request.form.get('email'))
        flash('Contact added!')

    return render_template('add_contact.html')

@app.route(r'/contacts/<name>', methods=['GET'])
def contact_detail(name):
    contact = Contact(name, 'phone{}'.format(name), 'email{}'.format(name))
    
    return render_template('detail_contact.html', contact=contact)

@app.route(r'/delete', methods=['POST'])
def delete_contact():
    name = request.form.get('name')
    print(name)
    return redirect('contact/{}'.format(name))


if __name__ == "__main__":
    app.run()
