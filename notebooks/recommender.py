import pandas as pd
import sqlite3
import os

def get_recommendations(user_risk_appetite):
    """
    Recommends the Top 3 Mutual Funds based on Sharpe Ratio and Risk Appetite.
    Accepts: 'Low', 'Moderate', or 'High'
    """
    # 1. Load the required data
    scorecard_path = '../data/processed/fund_scorecard.csv'

    if not os.path.exists(scorecard_path):
        return "Error: Scorecard data not found. Please ensure Day 4 tasks are complete."

    df_scorecard = pd.read_csv(scorecard_path)

    # Load dimensions to get the Category
    conn = sqlite3.connect('../data/db/bluestock_mf.db')
    df_dim = pd.read_sql_query("SELECT amfi_code, category FROM dim_fund", conn)
    conn.close()

    df_merged = pd.merge(df_scorecard, df_dim, on='amfi_code', how='inner')

    # 2. Define the Risk Mapping Logic
    # Debt = Low Risk | Hybrid = Moderate Risk | Equity = High Risk
    risk_mapping = {
        'Low': ['Debt'],
        'Moderate': ['Hybrid', 'Debt'], # Moderate can also invest in Debt safely
        'High': ['Equity', 'Hybrid', 'Debt'] # High risk can invest in anything, but prefers Equity
    }

    allowed_categories = risk_mapping.get(user_risk_appetite.capitalize(), [])

    if not allowed_categories:
        return "Invalid risk appetite. Please choose 'Low', 'Moderate', or 'High'."

    # 3. Filter and Sort
    # Filter by allowed categories, remove funds with no Sharpe ratio, and sort highest to lowest
    df_filtered = df_merged[df_merged['category'].isin(allowed_categories)].copy()
    df_filtered = df_filtered.dropna(subset=['sharpe_ratio'])
    df_filtered = df_filtered.sort_values(by='sharpe_ratio', ascending=False)

    # 4. Extract the Top 3
    top_3 = df_filtered.head(3)[['scheme_name', 'category', 'cagr_3Y_pct', 'sharpe_ratio']]
    top_3.reset_index(drop=True, inplace=True)
    top_3.index += 1 # Start index at 1 for clean presentation

    print(f"\n🎯 TOP 3 FUND RECOMMENDATIONS FOR '{user_risk_appetite.upper()}' RISK APPETITE:")
    print("-" * 75)
    print(top_3.to_string())
    print("-" * 75)

    return top_3

# If the script is run directly, test it with a 'Moderate' profile
if __name__ == "__main__":
    get_recommendations('Moderate')
