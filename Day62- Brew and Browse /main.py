from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.datetime import TimeField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    map_link = URLField('Maps link', validators=[DataRequired()])
    open = TimeField(label='Open', validators=[DataRequired()])
    close = TimeField(label='Close', validators=[DataRequired()])
    coffee = SelectField(label='Coffee',
                         choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                         validators=[DataRequired()])
    wifi = SelectField('Wifi',
                       choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                       validators=[DataRequired()])
    power = SelectField('Power',
                        choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


def get_cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        return list_of_rows


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    new_entry = []
    if form.validate_on_submit():
        for field in form:
            # Skip unnecessary fields like 'submit' and 'csrf_token'
            if field.name not in ['submit', 'csrf_token']:
                # Convert time to 12-hour format with AM/PM
                if field.name in ['open', 'close']:
                    formatted_time = field.data.strftime("%I:%M %p")
                    new_entry.append(formatted_time)
                else:
                    new_entry.append(str(field.data))
        # Open the CSV file in append mode and write the new row
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_entry)
        # Return the updated list after adding new entry
        list_of_rows = get_cafes()
        return render_template('cafes.html', cafes=list_of_rows)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    list_of_rows = get_cafes()
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
