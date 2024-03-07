from flask import Flask, render_template, request
from datetime import datetime, timedelta
from scipy.optimize import minimize
import numpy as np
import pandas as pd
import yfinance as yf
from fredapi import Fred
import os
from dotenv import load_dotenv
import helpers
import sp500tickers

load_dotenv()
FRED_KEY = os.getenv('FRED_KEY')

app = Flask(__name__)

@app.route("/")
def form_page():
    tickers = list(sp500tickers.tickers_dict.keys())
    return render_template("index.html", tickers=tickers)

@app.route("/", methods=['POST'])
def optimise_portfolio():
    selected_tickers = request.form.getlist('ticker[]')
    tickers = [s for s in selected_tickers if s != '']

    if len(tickers) < 2:
        return 'At least 2 tickers need to be selected'    

    end_date = datetime.today()
    start_date = end_date - timedelta(days = 5 * 365)
    adj_close_df = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    log_returns = np.log(adj_close_df/adj_close_df.shift(1))
    log_returns = log_returns.dropna()
    cov_matrix = log_returns.cov()*252
    fred = Fred(api_key=FRED_KEY)
    ten_year_treasury_rate = fred.get_series_latest_release('GS10')/100
    risk_free_rate = ten_year_treasury_rate.iloc[-1]
    constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights)-1}
    bounds = [(0,0.5) for _ in range(len(tickers))]
    initial_weights = np.array([1/len(tickers)]*len(tickers))
    optimise_results = minimize(helpers.neg_sharpe_ratio, initial_weights, args=(log_returns, cov_matrix, risk_free_rate), method='SLSQP', constraints=constraints, bounds=bounds)
    optimal_weights = optimise_results.x
    optimal_portfolio_return = helpers.expected_returns(optimal_weights, log_returns)
    optimal_portfolio_volatility = helpers.standard_deviation(optimal_weights, cov_matrix)
    optimal_sharpe_ratio = helpers.sharpe_ratio(optimal_weights, log_returns, cov_matrix, risk_free_rate)
    return render_template('results.html', optimal_weights=zip(range(len(tickers)), tickers, optimal_weights), optimal_portfolio_return=optimal_portfolio_return, optimal_portfolio_volatility=optimal_portfolio_volatility, optimal_sharpe_ratio=optimal_sharpe_ratio)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
