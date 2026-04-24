from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_pickle('covid_dataset_curated.pkl')

@app.route('/')
def index():
    columns = df.columns.tolist()
    return render_template('index.html', columns=columns)

@app.route('/submit', methods=['POST'])
def submit():
    data = {}
    for col in df.columns:
        data[col] = request.form.get(col)
    # Here you can process the data, e.g., add to dataset, predict, etc.
    return f"Submitted data: {data}"

if __name__ == '__main__':
    app.run(debug=True)