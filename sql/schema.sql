-- 1. Dimension Table: Fund Master Data
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date DATE,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

-- 2. Fact Table: Daily NAV History
CREATE TABLE IF NOT EXISTS fact_nav (
    amfi_code TEXT,
    date DATE,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund (amfi_code)
);

-- 3. Fact Table: Investor Transactions
CREATE TABLE IF NOT EXISTS fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund (amfi_code)
);

-- 4. Fact Table: Scheme Performance Metrics
CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code TEXT,
    -- We use generic return columns based on standard MF metrics
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    sharpe_ratio REAL,
    flag_negative_sharpe BOOLEAN,
    expense_ratio REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund (amfi_code)
);