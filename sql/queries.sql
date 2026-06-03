-- 1. Top 5 Funds by 1-Year Return
SELECT d.scheme_name, p.return_1y
FROM fact_performance p
JOIN dim_fund d ON p.amfi_code = d.amfi_code
ORDER BY p.return_1y DESC LIMIT 5;

-- 2. Average NAV per month (Last 12 months)
SELECT strftime('%Y-%m', date) as month, AVG(nav) as avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month DESC LIMIT 12;

-- 3. Total SIP Inflow by Year (YoY Growth proxy)
SELECT strftime('%Y', transaction_date) as year, SUM(amount_inr) as total_sip_inflow
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- 4. Transactions by State
SELECT state, COUNT(*) as txn_count, SUM(amount_inr) as total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with expense_ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

-- 6. Count of funds by Risk Category
SELECT risk_category, COUNT(*) as fund_count
FROM dim_fund
GROUP BY risk_category
ORDER BY fund_count DESC;

-- 7. Average 3-Year Return by Fund Category
SELECT d.category, AVG(p.return_3y) as avg_3y_return
FROM fact_performance p
JOIN dim_fund d ON p.amfi_code = d.amfi_code
GROUP BY d.category;

-- 8. Top 3 Cities by Total Investment Amount
SELECT city, SUM(amount_inr) as total_investment
FROM fact_transactions
GROUP BY city
ORDER BY total_investment DESC LIMIT 3;

-- 9. Funds with Negative Sharpe Ratio
SELECT d.scheme_name, p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund d ON p.amfi_code = d.amfi_code
WHERE p.flag_negative_sharpe = 1;

-- 10. Total Amount by Transaction Type
SELECT transaction_type, SUM(amount_inr) as total_amount
FROM fact_transactions
GROUP BY transaction_type;