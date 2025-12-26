# Marketing Data Analysis & ETL Pipeline - Q3/2020

This project provides an end-to-end solution for processing, standardizing, and analyzing Marketing and Sales data for the third quarter of 2020. It transforms inconsistent raw data into a structured format ready for executive reporting and strategic decision-making.

---

## 🛠 Tech Stack
* **Language:** Python
* **Libraries:** `Pandas` (Data manipulation), `NumPy` (Numerical processing), `Regex` (Text standardization)
* **Data Source:** Multi-sheet Excel database (`MKT`, `Sales`, `Vận đơn`)

---

## 📋 Data Processing Pipeline

The raw database (Q3/2020) contained significant formatting and consistency issues that required technical intervention before analysis.

### 1. Key Data Issues & Technical Solutions
| ID | Issue | Cause & Impact | Technical Fix |
| :--- | :--- | :--- | :--- |
| **1** | **Sales Data Loss** | Null values in "Call Date" caused data to drop from ~9,600 to ~200 rows. | Switched filtering logic to the `lead_date` column to retain 100% of leads. |
| **2** | **Year Error** | "Close Date" contained 2023 data instead of the reporting year 2020. | Implemented `fix_year_logic` to automatically map 2023 entries back to 2020. |
| **3** | **Naming/Encoding** | Column names contained Vietnamese accents and special characters. | Used **Regex** to strip accents, convert to lowercase, and replace spaces with underscores. |
| **4** | **Data Typing** | Currency and quantity columns contained non-numeric text strings. | Applied **Type Casting** (`pd.to_numeric`) with `errors='coerce'`, filling gaps with 0. |
| **5** | **Order Status** | Success metrics were scattered across "Status" and "Level" columns. | Created an `is_successful` flag for entries marked "dat hang" or "Level 8". |

### 2. Feature Engineering
The pipeline calculates essential performance metrics derived from raw attributes:
* **ROAS (Return on Ad Spend):**
    $$ROAS = \frac{\text{Revenue}}{\text{Marketing Cost}}$$
* **Lead-to-Order Conversion Rate:**
    $$\text{Conversion Rate} = \frac{\text{Total Orders}}{\text{Marketing Leads}}$$
* **Average Order Value (AOV):**
    $$AOV = \frac{\text{Total Revenue}}{\text{Total Orders}}$$

---

## 📈 Performance Insights (Q3/2020)

Based on the standardized data, several operational challenges were identified:

* **Tracking Failures:** High marketing costs recorded without corresponding engagement metrics (Impressions, Clicks), indicating broken tracking pixels.
* **Lead Quality Variance:** Conversion rates reached 100% for CVS campaigns but dropped to 0% for "Google/Discovery" and "FB/Mess".
* **CPA Instability:** Cost per Lead (CPA) fluctuated wildly between 22,745 and 490,000.

---

## 🚀 Strategic Roadmap for Q4/2020

To improve performance, the following actions are recommended:

* **Technical Audit:** Re-configure GTM and Pixel tracking to ensure 100% visibility on Top-Funnel metrics.
* **Budget Optimization:** Shift spending toward high-ROAS channels like **Google/PerMax**.
* **Sales Refinement:** Analyze the intake process for "FB/Mess" leads to determine if the issue lies in lead quality or sales handling.
* **CPA Thresholds:** Scale down campaigns exceeding the target CPA to maintain profitability.

---

## 📂 Project Structure
```text
├── data/
│   └── Database-Q3_2020.xlsx       # Raw source file
├── process_data.ipynb              # ETL script (Cleaning & Transformation)
├── Processed_MKT_Q3.csv            # Cleaned Marketing metrics
├── Processed_Sales_Q3.csv          # Standardized Sales/Lead data
└── Processed_VanDon_Q3.csv         # Cleaned Shipping & Revenue data