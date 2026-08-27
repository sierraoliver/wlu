# COVID-19 Country Tracker — Flask + Plotly

Interactive web visualization of COVID-19 data across 5 countries (Canada, United States, United Kingdom, India, and Japan).

## Setup & Run
```bash
# 1. Install dependencies
pip install flask pandas

# 2. Run the app
flask run
# or: python app.py
```

Then open **http://127.0.0.1:5000** in your browser.


## Project Structure

```
assignment 4/
├── app.py                   # Flask app 
├── COVID_Country_Sample.csv # Dataset 
├── templates/
│   └── index.html           
├── static/                  
└── README.md
```

## Features

| Part | What's implemented |
|------|--------------------|
| A    | pandas load, `head()` / `info()`, missing-value fill, outlier capping at p99, 3-month rolling mean |
| B    | Flask root route `/` renders `index.html` with country list + date range |
| C    | Plotly line chart; country dropdown; metric radio buttons (cases / vaccinations / deaths) |
| D    | `/data?country=X&metric=Y` returns JSON; `fetch()` updates chart without page reload |
| E    | Insights section explaining wave patterns, vaccination roll-out, correlation caveat, and design choices |
| F    | Dark responsive layout; axis labels; legend; chart caption; mobile-friendly at 600px breakpoint |

## Data Cleaning Decisions

- **Missing `new_vaccinations`**: filled with `0` — no vaccination programme existed in 2020 so absence of data means zero doses.
- **Missing `vaccinations_per_hundred`**: same reasoning, filled with `0`.
- **Outlier spikes**: capped at the 99th percentile per country — preserves trend shape while removing implausible single-month artefacts present in the sample data.
- **Rolling mean**: 3-month window with `min_periods=1` computed server-side for all three metrics and returned alongside raw values for the smooth toggle.

## Dependencies
```
flask >= 2.3
pandas >= 2.0
```