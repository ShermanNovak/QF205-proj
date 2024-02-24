from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def hello_world():
    tickers = ['AAPL', 'GOOG', 'MSFT']
    return render_template("index.html", tickers=tickers)

@app.route("/", methods=['POST'])
def optimise_portfolio():
    selected_tickers = request.form.getlist('ticker[]')
    data = yf.download(selected_tickers, start="2023-01-01", end="2024-01-01")
    print(data)
    return f'{selected_tickers}'

if __name__ == "__main__":
    app.run(port=8000, debug=True)
