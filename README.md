**Retail Sales Dashboard** (Python + Streamlit)

Overview:
----------
This project is a simple, browser-based dashboard built using Python.
It helps analyze retail sales data and visualize key business insights.

Key Features:
-------------
- Top 5 products by revenue
- Top 5 customers by spending
- Monthly revenue trends
- Revenue by city/location
- Revenue by product category

Technologies Used:
------------------
- Python
- Pandas (for data processing)
- Streamlit (for the dashboard GUI)
- Plotly (for interactive charts)
- SQL (for data querying and analysis logic)

Project Structure:
------------------
Retail-Sales-Project/
├── retail_dashboard.py                 # Python dashboard script
├── Retail_Sales_Analysis.sql           # SQL table + query file
├── Retail_Sales_Project_Description.txt # Technical explanation
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── sales.csv

How to Run:
-----------
1. Install the required libraries:
   pip install pandas matplotlib seaborn plotly streamlit

2. Run the dashboard:
   streamlit run retail_dashboard.py

3. Open your browser at:
   http://localhost:8501

About:
------
This project demonstrates a typical business data workflow:
- Importing and cleaning data
- Calculating key metrics
- Building a visual dashboard without Power BI

Author:
-------
Priyanshu Pandey
GitHub: https://github.com/Priyanshu2787
LinkedIn: https://www.linkedin.com/in/priyanshu-pandey2787/
