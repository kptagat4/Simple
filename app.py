from flask import Flask, render_template, request, redirect
app = Flask(__name__)
entries = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def new():
    return render_template('user.html')

@app.route('/entries', methods=["POST"])
def createdEntries():
    if request.method == 'POST':
        entry = {
            'name': request.form['name'],
            'age': request.form['age'],
            'date of birth': request.form['date of birth'],
            'gender': request.form['gender']
        }

        entries.append(entry)
        return render_template('entries.html', entries=entries)


@app.route('/view_entries')
def viewEntries():
    return render_template('entries.html', entries=entries)

@app.route('/delete_entry/<int:index>')
def delete_entry(index):
    if 0 <= index < len(entries):
        entries.pop(index)
    return redirect('/view_entries')

if __name__ == '__main__':
    app.run(debug=True)