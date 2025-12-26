# Marketing Data Analysis & ETL Pipeline - Q3/2020

[cite_start]This project provides an end-to-end solution for processing, standardizing, and analyzing Marketing and Sales data for the third quarter of 2020[cite: 1, 12]. [cite_start]It transforms inconsistent raw data into a structured format ready for executive reporting and strategic decision-making[cite: 3, 13].

---

## 🛠 Tech Stack
* **Language:** Python
* **Libraries:** `Pandas` (Data manipulation), `NumPy` (Numerical processing), `Regex` (Text standardization)
* **Data Source:** Multi-sheet Excel database (`MKT`, `Sales`, `Vận đơn`)

---

## 📋 Data Processing Pipeline

[cite_start]The raw database (Q3/2020) contained significant formatting and consistency issues that required technical intervention before analysis[cite: 3, 4].

### 1. Key Data Issues & Technical Solutions
| ID | [cite_start]Issue [cite: 4] | [cite_start]Cause & Impact [cite: 4] | [cite_start]Technical Fix [cite: 4] |
| :--- | :--- | :--- | :--- |
| **1** | **Sales Data Loss** | [cite_start]Null values in "Call Date" caused data to drop from ~9,600 to ~200 rows[cite: 4]. | Switched filtering logic to the `lead_date` column to retain 100% of leads. |
| **2** | **Year Error** | [cite_start]"Close Date" contained 2023 data instead of the reporting year 2020[cite: 4]. | Implemented `fix_year_logic` to automatically map 2023 entries back to 2020. |
| **3** | **Naming/Encoding** | [cite_start]Column names contained Vietnamese accents and special characters[cite: 4]. | Used **Regex** to strip accents, convert to lowercase, and replace spaces with underscores. |
| **4** | **Data Typing** | [cite_start]Currency and quantity columns contained non-numeric text strings[cite: 4]. | Applied **Type Casting** (`pd.to_numeric`) with `errors='coerce'`, filling gaps with 0. |
| **5** | **Order Status** | [cite_start]Success metrics were scattered across "Status" and "Level" columns[cite: 4]. | Created an `is_successful` flag for entries marked "dat hang" or "Level 8". |

### 2. Feature Engineering
[cite_start]The pipeline calculates essential performance metrics derived from raw attributes[cite: 8]:
* [cite_start]**ROAS (Return on Ad Spend):** [cite: 9]
    $$ROAS = \frac{\text{Revenue}}{\text{Marketing Cost}}$$
* [cite_start]**Lead-to-Order Conversion Rate:** [cite: 10]
    $$\text{Conversion Rate} = \frac{\text{Total Orders}}{\text{Marketing Leads}}$$
* [cite_start]**Average Order Value (AOV):** [cite: 11]
    $$AOV = \frac{\text{Total Revenue}}{\text{Total Orders}}$$

---

## 📈 Performance Insights (Q3/2020)

[cite_start]Based on the standardized data, several operational challenges were identified[cite: 27, 28]:

* [cite_start]**Tracking Failures:** High marketing costs recorded without corresponding engagement metrics (Impressions, Clicks), indicating broken tracking pixels[cite: 29].
* [cite_start]**Lead Quality Variance:** Conversion rates reached 100% for CVS campaigns but dropped to 0% for "Google/Discovery" and "FB/Mess"[cite: 30, 31].
* [cite_start]**CPA Instability:** Cost per Lead (CPA) fluctuated wildly between 22,745 and 490,000[cite: 32].

---

## 🚀 Strategic Roadmap for Q4/2020

[cite_start]To improve performance, the following actions are recommended[cite: 34]:

* [cite_start]**Technical Audit:** Re-configure GTM and Pixel tracking to ensure 100% visibility on Top-Funnel metrics[cite: 35, 37].
* [cite_start]**Budget Optimization:** Shift spending toward high-ROAS channels like **Google/PerMax**[cite: 38, 40].
* [cite_start]**Sales Refinement:** Analyze the intake process for "FB/Mess" leads to determine if the issue lies in lead quality or sales handling[cite: 41, 43].
* [cite_start]**CPA Thresholds:** Scale down campaigns exceeding the target CPA to maintain profitability[cite: 44, 46].

---

## 📂 Project Structure
```text
├── data/
│   └── Database-Q3_2020.xlsx       # Raw source file
├── process_data.ipynb              # ETL script (Cleaning & Transformation)
├── Processed_MKT_Q3.csv            # Cleaned Marketing metrics
├── Processed_Sales_Q3.csv          # Standardized Sales/Lead data
└── Processed_VanDon_Q3.csv         # Cleaned Shipping & Revenue data