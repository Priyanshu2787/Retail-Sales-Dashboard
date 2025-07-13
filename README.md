# Retail-Sales-Dashboard
Retail Sales Insights Dashboard (Python + Streamlit)

===========================================================
📌 Project Title:
Retail Sales Insights Dashboard – Python GUI with Streamlit

===========================================================
⚙️ Project Architecture & Data Flow:

CSV Files (customers.csv, products.csv, sales.csv)
        ↓
      Pandas → Data Cleaning & Transformation
        ↓
   Business Logic → KPIs + Aggregations
        ↓
   Visualization (Plotly, Matplotlib, Seaborn)
        ↓
   Interactive Dashboard via Streamlit

===========================================================
🧠 Objective:

To build a complete data analytics solution that:
- Loads retail sales data from CSV files
- Performs data transformation using Pandas
- Extracts business insights (revenue trends, top products/customers)
- Displays interactive dashboards with Plotly
- Provides a user-friendly browser GUI via Streamlit (no Power BI needed)

===========================================================
🧾 Input Data:

1. customers.csv: 
   - customer_id, customer_name, location

2. products.csv: 
   - product_id, product_name, category, price

3. sales.csv:
   - sale_id, customer_id, product_id, quantity, sale_date

===========================================================
🧰 Python Libraries Used:

| Library         | Purpose                                       |
|-----------------|-----------------------------------------------|
| pandas          | Data loading, cleaning, merging, aggregation |
| numpy           | Numerical operations                          |
| matplotlib      | Basic plotting                                |
| seaborn         | Statistical visualizations                    |
| plotly.express  | Interactive charts (bar, line, pie)           |
| streamlit       | Python GUI to build interactive dashboards    |

===========================================================
🏗️ Core Functional Flow:

1. Load data using pandas:
   customers = pd.read_csv("customers.csv")
   products = pd.read_csv("products.csv")
   sales = pd.read_csv("sales.csv")

2. Clean and merge:
   sales['sale_date'] = pd.to_datetime(sales['sale_date'])
   df = sales.merge(customers, on='customer_id').merge(products, on='product_id')
   df['revenue'] = df['quantity'] * df['price']
   df['month'] = df['sale_date'].dt.to_period('M').astype(str)

===========================================================
📊 Business Insights Generated:

1. Top 5 Products by Revenue:
   - Group by product_name, sum revenue, sort descending

2. Top 5 Customers by Revenue:
   - Group by customer_name, sum revenue, sort descending

3. Monthly Revenue Trend:
   - Group by month, sum revenue

4. Revenue by Location:
   - Group by city, sum revenue

5. Revenue by Category:
   - Group by category, sum revenue

===========================================================
🖥️ Streamlit GUI Structure:

- Title and KPI Summary:
  st.title("Retail Sales Dashboard")
  st.metric("Total Revenue", ...)
  st.metric("Top Revenue Location", ...)

- Graphs and Visuals:
  📈 Line Chart: Monthly Revenue Trend
  📊 Bar Chart: Top Products by Revenue
  📊 Bar Chart: Top Customers by Spending
  🧁 Pie Chart: Revenue by City
  📦 Bar Chart: Revenue by Category

===========================================================
🚀 How to Run the App:

1. Install required packages:
   pip install pandas numpy matplotlib seaborn plotly streamlit

2. Save the Python script as: retail_dashboard.py

3. Run the Streamlit app:
   streamlit run retail_dashboard.py

4. The dashboard will open in your default browser at:
   http://localhost:8501

===========================================================
✅ Project Highlights:

- Real-world retail business analytics simulation
- Covers full data workflow from raw data to insight
- No-code GUI for interacting with charts and KPIs
- Built with industry-used open-source Python stack
- Easily portable and deployable

===========================================================
📦 Future Expansion Ideas:

| Feature         | Description                                   |
|-----------------|-----------------------------------------------|
| Filters         | Add dropdowns to filter by location/category  |
| Export          | Allow downloading charts as images or CSV     |
| Database        | Connect to SQL or NoSQL DB for live data      |
| Deployment      | Host with Streamlit Cloud, Docker, or Heroku  |

===========================================================

Author: [Your Name]
Project Type: Data Analyst Portfolio Project
