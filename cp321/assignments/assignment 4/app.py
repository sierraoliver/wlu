import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#Part A: Load, Inspect, Clean 

df_raw = pd.read_csv("COVID_Country_Sample.csv", sep=None, engine="python")
df_raw["date"] = pd.to_datetime(df_raw["date"])

print("=== HEAD ===")
print(df_raw.head())
print("\n=== INFO ===")
df_raw.info()
print()

df = df_raw.copy()

#handle missing values:

#new_vaccinations: missing early on means 0 doses administered, fill with 0
df["new_vaccinations"] = df["new_vaccinations"].fillna(0)
df["vaccinations_per_hundred"] = df["vaccinations_per_hundred"].fillna(0)

#handle outliers

#cap new_cases at 99th percentile per country
#preserves trend while removing extreme spikes
def cap_outliers(series, q=0.99):
    cap = series.quantile(q)
    return series.clip(upper=cap)

df["new_cases"] = df.groupby("country")["new_cases"].transform(cap_outliers)

#3-month rolling averages - for frontend toggle
df["new_cases_rolling"] = (
    df.groupby("country")["new_cases"]
    .transform(lambda s: s.rolling(3, min_periods=1).mean())
)

df["new_vaccinations_rolling"] = (
    df.groupby("country")["new_vaccinations"]
    .transform(lambda s: s.rolling(3, min_periods=1).mean())
)

df["new_deaths_rolling"] = (
    df.groupby("country")["new_deaths"]
    .transform(lambda s: s.rolling(3, min_periods=1).mean())
)

#save cleaned csv
df.to_csv("COVID_Country_Sample_Cleaned.csv", index=False)


#Part B: Flask routes 

@app.route("/")
def index():
    countries = sorted(df["country"].unique().tolist())
    date_min = df["date"].min().strftime("%Y-%m")
    date_max = df["date"].max().strftime("%Y-%m")
    summary = {
        "countries": countries,
        "date_range": f"{date_min} → {date_max}",
        "default_country": countries[0],
    }
    return render_template("index.html", summary=summary)


#Part D: JSON data endpoint

@app.route("/data")
def data():
    country = request.args.get("country", "Canada")
    metric = request.args.get("metric", "new_cases")
    smooth = request.args.get("smooth", "false").lower() == "true"

    allowed_metrics = {
        "new_cases": "new_cases",
        "new_vaccinations": "new_vaccinations",
        "new_deaths": "new_deaths",
    }

    country_df = df[df["country"] == country].reset_index(drop=True)

    raw_col = allowed_metrics.get(metric, "new_cases")
    rolling_col = raw_col + "_rolling"

    subset = country_df[["date", raw_col, rolling_col]].copy()
    subset["date"] = subset["date"].dt.strftime("%Y-%m-%d")
    subset = subset.rename(columns={raw_col: "value", rolling_col: "rolling"})

    return jsonify(subset.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)
