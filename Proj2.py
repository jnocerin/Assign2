from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_site():
    return(render_template("Proj2Supp.html"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)