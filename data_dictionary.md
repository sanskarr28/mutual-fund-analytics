# Bluestock Mutual Fund Analytics: Data Dictionary

## 1. Dimension Table: `dim_fund`
**Source:** `01_fund_master.csv`
**Description:** The central master table containing static details and classification for every mutual fund scheme.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `amfi_code` | TEXT (PK) | Unique 6-digit identifier assigned by AMFI. Primary Key. |
| `fund_house` | TEXT | The Asset Management Company (e.g., SBI Mutual Fund). |
| `scheme_name` | TEXT | The full official name of the mutual fund scheme. |
| `category` | TEXT | Broad asset class (e.g., Equity, Debt, Hybrid). |
| `sub_category` | TEXT | Specific investment focus (e.g., Large Cap, Mid Cap). |
| `plan` | TEXT | Direct or Regular plan type. |
| `launch_date` | DATE | The date the fund was introduced to the market. |
| `benchmark` | TEXT | The market index used to measure the fund's performance. |
| `expense_ratio_pct` | REAL | The annual maintenance charge levied by the AMC (in %). |
| `exit_load_pct` | REAL | The fee charged if units are sold within a specific period (in %). |
| `min_sip_amount` | REAL | Minimum INR required to start a Systematic Investment Plan. |
| `min_lumpsum_amount` | REAL | Minimum INR required for a one-time investment. |
| `fund_manager` | TEXT | Name of the primary fund manager. |
| `risk_category` | TEXT | Risk classification (e.g., Very High, Moderate). |
| `sebi_category_code` | TEXT | Standardized classification code assigned by SEBI. |

---

## 2. Fact Table: `fact_nav`
**Source:** `02_nav_history.csv` (Cleaned & Forward-Filled)
**Description:** Daily Net Asset Value (NAV) historical pricing for all funds.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `amfi_code` | TEXT (FK) | Foreign key mapping to `dim_fund`. |
| `date` | DATE | The trading date (weekends/holidays are forward-filled). |
| `nav` | REAL | The Net Asset Value price per unit on the given date. |

---

## 3. Fact Table: `fact_transactions`
**Source:** `08_investor_transactions.csv` (Cleaned)
**Description:** Log of all individual investor transactions (SIPs, Lumpsums, Redemptions).

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `investor_id` | TEXT | Unique identifier for the investor. |
| `transaction_date` | DATE | The date the transaction was executed. |
| `amfi_code` | TEXT (FK) | Foreign key mapping to the purchased/sold fund. |
| `transaction_type` | TEXT | Standardized type: 'SIP', 'Lumpsum', 'Redemption', or 'Other'. |
| `amount_inr` | REAL | The transaction value in Indian Rupees (must be > 0). |
| `state` | TEXT | Indian state of the investor. |
| `city` | TEXT | City of the investor. |
| `city_tier` | TEXT | Classification of the city (Tier 1, Tier 2, etc.). |
| `age_group` | TEXT | Demographic age bracket of the investor. |
| `gender` | TEXT | Gender of the investor. |
| `annual_income_lakh` | REAL | Investor's declared annual income in Lakhs INR. |
| `payment_mode` | TEXT | Method of payment (UPI, Net Banking, etc.). |
| `kyc_status` | TEXT | Current KYC verification status (e.g., Verified, Pending). |

---

## 4. Fact Table: `fact_performance`
**Source:** `07_scheme_performance.csv` (Cleaned)
**Description:** Key performance indicators and risk metrics for each scheme.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `amfi_code` | TEXT (FK) | Foreign key mapping to `dim_fund`. |
| `return_1y` | REAL | 1-Year annualized return percentage. |
| `return_3y` | REAL | 3-Year annualized return percentage. |
| `return_5y` | REAL | 5-Year annualized return percentage. |
| `sharpe_ratio` | REAL | Risk-adjusted return metric. |
| `flag_negative_sharpe` | BOOLEAN | 1 if Sharpe Ratio is negative, 0 if positive. |
| `expense_ratio` | REAL | Cleaned expense ratio (validated between 0.1% and 2.5%). |