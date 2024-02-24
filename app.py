from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

# hello
# zach

# Standardizing the set period used for portfolio optimisation
start_date = '2006-01-15'
end_date = '2023-10-01'

ind = (data.index >= start_date)*(data.index <= end_date)

data = data[ind]

SP500 = SP500[ind]

TBill = TBill[ind]





# Extracting risk free rate
file_name = '' #TO FILL the datafile downloaded from FRED
df = pd.read_csv(file_name)

df['DATE']=pd.to_datetime(df['DATE']) #set the DATE column as datetime object
df['WTB3MS'] = pd.to_numeric(df['WTB3MS'], errors='coerce') #set the return column as numeric

RET_data=pd.DataFrame(columns=['RET'], index=df.DATE) #create a new dataframe
RET_data['RET'] = (df['WTB3MS'].values/100 + 1) ** (1/52) - 1 #edit the unit of the return data

RET_data_weekly = (RET_data['RET']+1).resample('W').prod() - 1 #convert the data to the same weekly frequency as above

TBill = pd.DataFrame(columns=['T-Bill'], index=RET_data_weekly.index)
TBill['T-Bill'] = RET_data_weekly

ind = (TBill.index >= df_week.index[[0]][0])*(TBill.index <= df_week.index[[-1]][0])
TBill = TBill[ind] #keep the same start and end date as the stock returns data





Freq = 52 # frequency factor (given weekly data, it is 52)

# Functions for annualizing returns and standard deviation; x is a scalar input
def ann_ret(x):
    return (x+1)**Freq-1
def ann_std(x):
    return x*np.sqrt(Freq)

# Function used to find the Annualized geometric mean of x [note: x is series of weekly data]
def ann_geo_mean(x):
    n = len(x)
    return np.exp(np.sum(np.log(1+x)) * Freq / n) - 1

# Function used to find the Annualized Sharpe Ratio of x; x is a series of simple returns
def ann_sr(x, rf):
    n = len(x)
    ret_expected = np.sum(x-rf)/n # more widely used as arithmetic mean in sharpe ratio calculation
    ret_avg = np.sum(x)/n
    std_dev = np.sqrt( np.sum( (x - ret_avg)**2 ) / n )
    annu_ret_expected = (ret_expected+1)**Freq-1
    annu_std_dev = std_dev * np.sqrt(Freq)
    return annu_ret_expected/annu_std_dev

# Function used to find the Maximum drawdown (optional)
def mdd(x):
    wealth = (x+1).cumprod() #x is a return vector
    cummax = wealth.cummax() #determine cumulative maximum value
    drawdown = wealth/cummax - 1 #calculate drawdown vector
    return drawdown.min()


# sharlene
