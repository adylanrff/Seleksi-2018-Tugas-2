import json
from flask import Flask, render_template

baseFilePath = "data/"

def readJSONDataSet():
    dataset = []
    for i in range(2, 68):
        filename = 'output' + str(i) + '.json'
        if filename:
            path = baseFilePath + "raw/" + filename
            with open(path, 'r') as f:
                datastore = json.load(f)
                dataset.append(datastore)
    return json.dumps(dataset)

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("dashboard.html", dataset=readJSONDataSet())


if __name__ == '__main__':
    app.run()
