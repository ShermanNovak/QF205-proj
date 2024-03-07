tickers_dict = {'A': 'Agilent Technologies Inc', 'AA': 'Alcoa Inc', 'AAPL': 'Apple Inc.', \
           'ABC': 'AmerisourceBergen Corp', 'ABT': 'Abbott Laboratories', 'ACE': 'ACE Limited', \
            'ACN': 'Accenture', 'ADBE': 'Adobe Systems Inc', 'ADI': 'Analog Devices Inc', \
            'ADM': 'Archer-Daniels-Midland Co', 'ADP': 'Automatic Data Processing', \
            'ADSK': 'Autodesk Inc', 'AEE': 'Ameren Corp', 'AEP': 'American Electric Power', \
            'AES': 'AES Corp', 'AET': 'Aetna Inc', 'AFL': 'AFLAC Inc', 'AGN': 'Allergan Inc', \
            'AIG': 'American Intl Group Inc', 'AIV': 'Apartment Investment & Mgmt', \
            'AIZ': 'Assurant Inc', 'AKAM': 'Akamai Technologies Inc', 'ALL': 'Allstate Corp', 'ALTR': 'Altera Corp', 'ALXN': 'Alexion Pharmaceuticals', 'AMAT': 'Applied Materials Inc', 'AMD': 'Advanced Micro Devices', 'AMGN': 'Amgen Inc', 'AMP': 'Ameriprise Financial', 'AMT': 'American Tower Corp A', 'AMZN': 'Amazon.com Inc', 'AN': 'AutoNation Inc', 'ANF': 'Abercrombie & Fitch Company A', 'ANR': 'Alpha Natural Resources', 'AON': 'Aon plc', 'APA': 'Apache Corporation', 'APC': 'Anadarko Petroleum Corp', 'APD': 'Air Products & Chemicals Inc', 'APH': 'Amphenol Corp A', 'APOL': 'Apollo Group Inc', 'ARG': 'Airgas Inc', 'ATI': 'Allegheny Technologies Inc', 'AVB': 'AvalonBay Communities, Inc.', 'AVP': 'Avon Products', 'AVY': 'Avery Dennison Corp', 'AXP': 'American Express Co', 'AZO': 'AutoZone Inc', 'BA': 'Boeing Company', 'BAC': 'Bank of America Corp', 'BAX': 
            'Baxter International Inc.', 'BBBY': 'Bed Bath & Beyond', 'BBT': 'BB&T Corporation', \
            'BBY': 'Best Buy Co. Inc.', 'BCR': 'Bard (C.R.) Inc.', 'BDX': 'Becton Dickinson', 'BEAM': 'Beam Inc.', \
            'BEN': 'Franklin Resources', 'BF.B': 'Brown-Forman Corporation', 'BHI': 'Baker Hughes Inc', \
            'BIG': 'Big Lots Inc.', 'BIIB': 'BIOGEN IDEC Inc.', 'BK': 'The Bank of New York Mellon Corp.', \
            'BLK': 'BlackRock', 'BLL': 'Ball Corp', 'BMC': 'BMC Software', 'BMS': 'Bemis Company', \
            'BMY': 'Bristol-Myers Squibb', 'BRCM': 'Broadcom Corporation', 'BRK.B': 'Berkshire Hathaway', \
            'BSX': 'Boston Scientific', 'BTU': 'Peabody Energy', 'BWA': 'BorgWarner', \
            'BXP': 'Boston Properties', 'C': 'Citigroup Inc.', 'CA': 'CA, Inc.', 'CAG': 'ConAgra Foods Inc.', \
            'CAH': 'Cardinal Health Inc.', 'CAM': 'Cameron International Corp.', 'CAT': 'Caterpillar Inc.', \
            'CB': 'Chubb Corp.', 'CBE': 'Cooper Industries', 'CBG': 'CBRE Group', 'CBS': 'CBS Corp.', \
            'CCE': 'Coca-Cola Enterprises', 'CCI': 'Crown Castle International Corp.', 'CCL': 'Carnival Corp.', \
            'CELG': 'Celgene Corp.', 'CERN': 'Cerner', 'CF': 'CF Industries Holdings Inc', 'CFN': 'Carefusion', \
            'CHK': 'Chesapeake Energy', 'CHRW': 'C. H. Robinson Worldwide', 'CI': 'CIGNA Corp.', \
            'CINF': 'Cincinnati Financial', 'CL': 'Colgate-Palmolive', 'CLF': 'Cliffs Natural Resources', \
            'CLX': 'Clorox Co.', 'CMA': 'Comerica Inc.', 'CMCSA': 'Comcast Corp.', 'CME': 'CME Group Inc.', \
            'CMG': 'Chipotle Mexican Grill', 'CMI': 'Cummins Inc.', 'CMS': 'CMS Energy', 'CNP': 'CenterPoint Energy', \
            'CNX': 'CONSOL Energy Inc.', 'COF': 'Capital One Financial', 'COG': 'Cabot Oil & Gas', \
            'COH': 'Coach Inc.', 'COL': 'Rockwell Collins', 'COP': 'ConocoPhillips', 'COST': 'Costco Co.', \
            'COV': 'Covidien plc', 'CPB': 'Campbell Soup', 'CRM': 'Salesforce.com', \
            'CSC': 'Computer Sciences Corp.', 'CSCO': 'Cisco Systems', 'CSX': 'CSX Corp.', \
            'CTAS': 'Cintas Corporation', 'CTL': 'CenturyLink Inc', 'CTSH': 'Cognizant Technology Solutions', \
            'CTXS': 'Citrix Systems', 'CVC': 'Cablevision Systems Corp.', 'CVH': 'Coventry Health Care Inc.', \
            'CVS': 'CVS Caremark Corp.', 'CVX': 'Chevron Corp.', 'D': 'Dominion Resources', \
            'DD': 'Du Pont (E.I.)', 'DE': 'Deere & Co.', 'DELL': 'Dell Inc.', 'DF': 'Dean Foods', \
            'DFS': 'Discover Financial Services', 'DGX': 'Quest Diagnostics', 'DHI': 'D. R. Horton', \
            'DHR': 'Danaher Corp.', 'DIS': 'Walt Disney Co.', 'DISCA': 'Discovery Communications', \
            'DLTR': 'Dollar Tree', 'DNB': 'Dun & Bradstreet', 'DNR': 'Denbury Resources Inc.', \
            'DO': 'Diamond Offshore Drilling', 'DOV': 'Dover Corp.', 'DOW': 'Dow Chemical', \
            'DPS': 'Dr Pepper Snapple Group', 'DRI': 'Darden Restaurants', 'DTE': 'DTE Energy Co.', \
            'DTV': 'DirecTV', 'DUK': 'Duke Energy', 'DV': 'DeVry, Inc.', 'DVA': 'DaVita Inc.', \
            'DVN': 'Devon Energy Corp.', 'EA': 'Electronic Arts', 'EBAY': 'eBay Inc.', 'ECL': 'Ecolab Inc.', \
            'ED': 'Consolidated Edison', 'EFX': 'Equifax Inc.', 'EIX': "Edison Int'l", \
            'EL': 'Estee Lauder Cos.', 'EMC': 'EMC Corp.', 'EMN': 'Eastman Chemical', \
            'EMR': 'Emerson Electric', 'EOG': 'EOG Resources', 'EQR': 'Equity Residential', \
            'EQT': 'EQT Corporation', 'ESRX': 'Express Scripts', 'ESV': 'Ensco plc', 'ETFC': 'E-Trade', \
            'ETN': 'Eaton Corp.', 'ETR': 'Entergy Corp.', 'EW': 'Edwards Lifesciences', \
            'EXC': 'Exelon Corp.', 'EXPD': "Expeditors Int'l", 'EXPE': 'Expedia Inc.', \
            'F': 'Ford Motor', 'FAST': 'Fastenal Co', 'FCX': 'Freeport-McMoran Cp & Gld', \
            'FDO': 'Family Dollar Stores', 'FDX': 'FedEx Corporation', 'FE': 'FirstEnergy Corp', \
            'FFIV': 'F5 Networks', 'FHN': 'First Horizon National', 'FII': 'Federated Investors Inc.', \
            'FIS': 'Fidelity National Information Services', 'FISV': 'Fiserv Inc', \
            'FITB': 'Fifth Third Bancorp', 'FLIR': 'FLIR Systems', 'FLR': 'Fluor Corp.', \
            'FLS': 'Flowserve Corporation', 'FMC': 'FMC Corporation', 'FOSL': 'Fossil, Inc.', \
            'FRX': 'Forest Laboratories', 'FSLR': 'First Solar Inc', 'FTI': 'FMC Technologies Inc.', \
            'FTR': 'Frontier Communications', 'GAS': 'AGL Resources Inc.', 'GCI': 'Gannett Co.', \
            'GD': 'General Dynamics', 'GE': 'General Electric', 'GILD': 'Gilead Sciences', \
            'GIS': 'General Mills', 'GLW': 'Corning Inc.', 'GME': 'GameStop Corp.', \
            'GNW': 'Genworth Financial Inc.', 'GOOG': 'Google Inc.', 'GPC': 'Genuine Parts', \
            'GPS': 'Gap (The)', 'GS': 'Goldman Sachs Group', 'GT': 'Goodyear Tire & Rubber', \
            'GWW': 'Grainger (W.W.) Inc.', 'HAL': 'Halliburton Co.', 'HAR': "Harman Int'l Industries", \
            'HAS': 'Hasbro Inc.', 'HBAN': 'Huntington Bancshares', 'HCBK': 'Hudson City Bancorp', \
            'HCN': 'Health Care REIT', 'HCP': 'HCP Inc.', 'HD': 'Home Depot', 'HES': 'Hess Corporation', \
            'HIG': 'Hartford Financial Svc.Gp.', 'HNZ': 'Heinz (H.J.)', 'HOG': 'Harley-Davidson', \
            'HON': "Honeywell Int'l Inc.", 'HOT': 'Starwood Hotels & Resorts', 'HP': 'Helmerich & Payne', \
            'HPQ': 'Hewlett-Packard', 'HRB': 'Block H&R', 'HRL': 'Hormel Foods Corp.', \
            'HRS': 'Harris Corporation', 'HSP': 'Hospira Inc.', 'HST': 'Host Hotels & Resorts', \
            'HSY': 'The Hershey Company', 'HUM': 'Humana Inc.', 'IBM': 'International Bus. Machines', \
            'ICE': 'IntercontinentalExchange Inc.', 'IFF': 'International Flav/Frag', \
            'IGT': 'International Game Technology', 'INTC': 'Intel Corp.', 'INTU': 'Intuit Inc.', \
            'IP': 'International Paper', 'IPG': 'Interpublic Group', 'IR': 'Ingersoll-Rand PLC', \
            'IRM': 'Iron Mountain Incorporated', 'ISRG': 'Intuitive Surgical Inc.', \
            'ITW': 'Illinois Tool Works', 'IVZ': 'Invesco Ltd.', 'JBL': 'Jabil Circuit', \
            'JCI': 'Johnson Controls', 'JCP': 'Penney (J.C.)', 'JDSU': 'JDS Uniphase Corp.', \
            'JEC': 'Jacobs Engineering Group', 'JNJ': 'Johnson & Johnson', 'JNPR': 'Juniper Networks', \
            'JOY': 'Joy Global Inc.', 'JPM': 'JPMorgan Chase & Co.', 'JWN': 'Nordstrom', 'K': 'Kellogg Co.', \
            'KEY': 'KeyCorp', 'KFT': 'Kraft Foods Inc-A', 'KIM': 'Kimco Realty', 'KLAC': 'KLA-Tencor Corp.', \
            'KMB': 'Kimberly-Clark', 'KMI': 'Kinder Morgan', 'KMX': 'Carmax Inc', 'KO': 'Coca Cola Co.', \
            'KR': 'Kroger Co.', 'KSS': "Kohl's Corp.", 'L': 'Loews Corp.', 'LEG': 'Leggett & Platt', \
            'LEN': 'Lennar Corp.', 'LH': 'Laboratory Corp. of America Holding', 'LIFE': 'Life Technologies', \
            'LLL': 'L-3 Communications Holdings', 'LLTC': 'Linear Technology Corp.', \
            'LLY': 'Lilly (Eli) & Co.', 'LM': 'Legg Mason', 'LMT': 'Lockheed Martin Corp.', \
            'LNC': 'Lincoln National', 'LO': 'Lorillard Inc.', 'LOW': "Lowe's Cos.", 'LRCX': 'Lam Research', \
            'LSI': 'LSI Corporation', 'LTD': 'Limited Brands Inc.', 'LUK': 'Leucadia National Corp.', \
            'LUV': 'Southwest Airlines', 'LXK': "Lexmark Int'l Inc", 'M': "Macy's Inc.", \
            'MA': 'Mastercard Inc.', 'MAR': "Marriott Int'l.", 'MAS': 'Masco Corp.', 'MAT': 'Mattel Inc.', \
            'MCD': "McDonald's Corp.", 'MCHP': 'Microchip Technology', 'MCK': 'McKesson Corp.', \
            'MCO': "Moody's Corp", 'MDT': 'Medtronic Inc.', 'MET': 'MetLife Inc.', 'MHP': 'McGraw-Hill', \
            'MJN': 'Mead Johnson', 'MKC': 'McCormick & Co.', 'MMC': 'Marsh & McLennan', 'MMM': '3M Co.', \
            'MNST': 'Monster Beverage', 'MO': 'Altria Group Inc', 'MOLX': 'Molex Inc.', 'MON': 'Monsanto Co.', \
            'MOS': 'The Mosaic Company', 'MPC': 'Marathon Petroleum', 'MRK': 'Merck & Co.', \
            'MRO': 'Marathon Oil Corp.', 'MS': 'Morgan Stanley', 'MSFT': 'Microsoft Corp.', \
            'MSI': 'Motorola Solutions Inc.', 'MTB': 'M&T Bank Corp.', 'MU': 'Micron Technology', \
            'MUR': 'Murphy Oil', 'MWV': 'MeadWestvaco Corporation', 'MYL': 'Mylan Inc.', \
            'NBL': 'Noble Energy Inc', 'NBR': 'Nabors Industries Ltd.', 'NDAQ': 'NASDAQ OMX Group', \
            'NE': 'Noble Corp', 'NEE': 'NextEra Energy Resources', 'NEM': 'Newmont Mining Corp. (Hldg. Co.)', \
            'NFLX': 'NetFlix Inc.', 'NFX': 'Newfield Exploration Co', 'NI': 'NiSource Inc.', \
            'NKE': 'NIKE Inc.', 'NOC': 'Northrop Grumman Corp.', 'NOV': 'National Oilwell Varco Inc.', \
            'NRG': 'NRG Energy', 'NSC': 'Norfolk Southern Corp.', 'NTAP': 'NetApp', \
            'NTRS': 'Northern Trust Corp.', 'NU': 'Northeast Utilities', 'NUE': 'Nucor Corp.', \
            'NVDA': 'Nvidia Corporation', 'NWL': 'Newell Rubbermaid Co.', 'NWSA': 'News Corporation', \
            'NYX': 'NYSE Euronext', 'OI': 'Owens-Illinois Inc', 'OKE': 'ONEOK', 'OMC': 'Omnicom Group', \
            'ORCL': 'Oracle Corp.', 'ORLY': "O'Reilly Automotive", 'OXY': 'Occidental Petroleum', \
            'PAYX': 'Paychex Inc.', 'PBCT': "People's United Bank", 'PBI': 'Pitney-Bowes', \
            'PCAR': 'PACCAR Inc.', 'PCG': 'PG&E Corp.', 'PCL': 'Plum Creek Timber Co.', \
            'PCLN': 'Priceline.com Inc', 'PCP': 'Precision Castparts', 'PCS': 'MetroPCS Communications Inc.', \
            'PDCO': 'Patterson Companies', 'PEG': 'Public Serv. Enterprise Inc.', 'PEP': 'PepsiCo Inc.', \
            'PFE': 'Pfizer Inc.', 'PFG': 'Principal Financial Group', 'PG': 'Procter & Gamble', \
            'PGR': 'Progressive Corp.', 'PH': 'Parker-Hannifin', 'PHM': 'Pulte Homes Inc.', \
            'PKI': 'PerkinElmer', 'PLD': 'ProLogis', 'PLL': 'Pall Corp.', 'PM': 'Philip Morris International', \
            'PNC': 'PNC Financial Services', 'PNW': 'Pinnacle West Capital', 'POM': 'Pepco Holdings Inc.', \
            'PPG': 'PPG Industries', 'PPL': 'PPL Corp.', 'PRGO': 'Perrigo', 'PRU': 'Prudential Financial', \
            'PSA': 'Public Storage', 'PSX': 'Phillips 66', 'PWR': 'Quanta Services Inc.', 'PX': 'Praxair Inc.', \
            'PXD': 'Pioneer Natural Resources', 'QCOM': 'QUALCOMM Inc.', 'QEP': 'QEP Resources', \
            'R': 'Ryder System', 'RAI': 'Reynolds American Inc.', 'RDC': 'Rowan Cos.', \
            'RF': 'Regions Financial Corp.', 'RHI': 'Robert Half International', 'RHT': 'Red Hat Inc.', \
            'RL': 'Polo Ralph Lauren Corp.', 'ROK': 'Rockwell Automation Inc.', 'ROP': 'Roper Industries', \
            'ROST': 'Ross Stores Inc.', 'RRC': 'Range Resources Corp.', 'RRD': 'Donnelley (R.R.) & Sons', \
            'RSG': 'Republic Services Inc', 'RTN': 'Raytheon Co.', 'S': 'Sprint Nextel Corp.', 'SAI': 'SAIC', \
            'SBUX': 'Starbucks Corp.', 'SCG': 'SCANA Corp', 'SCHW': 'Charles Schwab', \
            'SE': 'Spectra Energy Corp.', 'SEE': 'Sealed Air Corp.(New)', 'SHLD': 'Sears Holdings Corporation', \
            'SHW': 'Sherwin-Williams', 'SIAL': 'Sigma-Aldrich', 'SJM': 'Smucker (J.M.)', \
            'SLB': 'Schlumberger Ltd.', 'SLM': 'SLM Corporation', 'SNA': 'Snap-On Inc.', \
            'SNDK': 'SanDisk Corporation', 'SNI': 'Scripps Networks Interactive Inc.', 'SO': 'Southern Co.', \
            'SPG': 'Simon Property Group Inc', 'SPLS': 'Staples Inc.', 'SRCL': 'Stericycle Inc', \
            'SRE': 'Sempra Energy', 'STI': 'SunTrust Banks', 'STJ': 'St Jude Medical', \
            'STT': 'State Street Corp.', 'STX': 'Seagate Technology', 'STZ': 'Constellation Brands', \
            'SUN': 'Sunoco Inc.', 'SWK': 'Stanley Black & Decker', 'SWN': 'Southwestern Energy', \
            'SWY': 'Safeway Inc.', 'SYK': 'Stryker Corp.', 'SYMC': 'Symantec Corp.', 'SYY': 'Sysco Corp.', \
            'T': 'AT&T Inc', 'TAP': 'Molson Coors Brewing Company', 'TDC': 'Teradata Corp.', \
            'TE': 'TECO Energy', 'TEG': 'Integrys Energy Group Inc.', 'TEL': 'TE Connectivity Ltd.', \
            'TER': 'Teradyne Inc.', 'TGT': 'Target Corp.', 'THC': 'Tenet Healthcare Corp.', \
            'TIE': 'Titanium Metals Corp', 'TIF': 'Tiffany & Co.', 'TJX': 'TJX Companies Inc.', \
            'TMK': 'Torchmark Corp.', 'TMO': 'Thermo Fisher Scientific', 'TRIP': 'TripAdvisor', \
            'TROW': 'T. Rowe Price Group', 'TRV': 'The Travelers Companies Inc.', 'TSN': 'Tyson Foods', \
            'TSO': 'Tesoro Petroleum Co.', 'TSS': 'Total System Services', 'TWC': 'Time Warner Cable Inc.', \
            'TWX': 'Time Warner Inc.', 'TXN': 'Texas Instruments', 'TXT': 'Textron Inc.', \
            'TYC': 'Tyco International', 'UNH': 'United Health Group Inc.', 'UNM': 'Unum Group', \
            'UNP': 'Union Pacific', 'UPS': 'United Parcel Service', 'URBN': 'Urban Outfitters', \
            'USB': 'U.S. Bancorp', 'UTX': 'United Technologies', 'V': 'Visa Inc.', \
            'VAR': 'Varian Medical Systems', 'VFC': 'V.F. Corp.', 'VIAB': 'Viacom Inc.', \
            'VLO': 'Valero Energy', 'VMC': 'Vulcan Materials', 'VNO': 'Vornado Realty Trust', \
            'VRSN': 'Verisign Inc.', 'VTR': 'Ventas Inc', 'VZ': 'Verizon Communications', \
            'WAG': 'Walgreen Co.', 'WAT': 'Waters Corporation', 'WDC': 'Western Digital', \
            'WEC': 'Wisconsin Energy Corporation', 'WFC': 'Wells Fargo', 'WFM': 'Whole Foods Market', \
            'WHR': 'Whirlpool Corp.', 'WIN': 'Windstream Corporation', 'WLP': 'WellPoint Inc.', \
            'WM': 'Waste Management Inc.', 'WMB': 'Williams Cos.', 'WMT': 'Wal-Mart Stores', \
            'WPI': 'Watson Pharmaceuticals', 'WPO': 'Washington Post Co B', 'WPX': 'WPX Energy, Inc.', \
            'WU': 'Western Union Co', 'WY': 'Weyerhaeuser Corp.', 'WYN': 'Wyndham Worldwide', \
            'WYNN': 'Wynn Resorts Ltd', 'X': 'United States Steel Corp.', 'XEL': 'Xcel Energy Inc', \
            'XL': 'XL Capital', 'XLNX': 'Xilinx Inc', 'XOM': 'Exxon Mobil Corp.', \
            'XRAY': 'Dentsply International', 'XRX': 'Xerox Corp.', 'XYL': 'Xylem Inc.', 'YHOO': 'Yahoo Inc.', \
            'YUM': 'Yum! Brands Inc', 'ZION': 'Zions Bancorp', 'ZMH': 'Zimmer Holdings'}