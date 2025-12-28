# Analysis Report of Non-Temporal Factors Affecting Revenue Forecasting

**Data Source:** `Database-Q3_2020.xlsx` (Quarter 3, 2020)

## 1. Executive Summary

The initial revenue forecasting model (using Random Forest Regressor) was based solely on time-series factors (lagged revenue, day of the week/month). This report analyzes other critical non-temporal factors (Marketing, Channels, Personnel) that may affect forecast accuracy and proposes methods for their integration.

If these factors are not taken into account, forecast accuracy will decrease, especially in situations involving major changes in Marketing strategy or operational performance.

---

## 2. Correlation Analysis Between Marketing Costs and Revenue

The relationship between Marketing Costs and Revenue is the most important non-temporal factor.

### 2.1. Correlation Coefficients

Correlation analysis on campaign/daily level data shows:

| Variable | Marketing Cost | Revenue | MKT Lead | Order |
| :--- | :--- | :--- | :--- | :--- |
| **Marketing Cost** | 1.00 | **0.60** | 0.61 | 0.60 |
| **Revenue** | 0.60 | 1.00 | **0.99** | **1.00** |

* **Cost - Revenue Correlation:** A correlation coefficient of **0.60** indicates a positive and relatively strong relationship between Marketing Costs and Revenue. Increasing costs tends to increase revenue.
* **Lead - Revenue Correlation:** A near-perfect correlation (**0.99 - 1.00**) between **MKT Leads**, **Orders**, and **Revenue** is evident, showing that Leads are an extremely important intermediate variable.

### 2.2. Return on Ad Spend (ROAS)

* **Average ROAS:** 4.73
* **Median ROAS:** 2.60

The large difference between the average and median ROAS (4.73 vs. 2.60) indicates that a few campaigns or days have extremely high performance, pulling the average ROAS up. This suggests that the **quality** of spending is more important than the **quantity** of spending.

---

## 3. Efficiency Analysis by Channel and Campaign

Performance differences between channels and campaigns are major non-temporal "noise" factors for a simple forecasting model.

### 3.1. Efficiency by Channel

| Channel | Marketing Cost (VND) | Revenue (VND) | ROAS | CPL (VND/Lead) | Conversion Rate (Order/Lead) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FB** | 1,314,129,481 | 3,101,689,000 | **2.36** | 154,367 | 72.18% |
| **Google** | 132,545,235 | 3,120,762,000 | **23.54** | 178,152 | 84.26% |
| **Tiktok** | 350,299 | 1,956,000 | **5.58** | 87,574 | 72.82% |

* **Google** has an outstanding ROAS (**23.54**) compared to FB (**2.36**), despite a higher CPL (Cost Per Lead). This indicates that the quality of leads from Google is significantly higher, leading to a higher Conversion Rate.
* **Tiktok** has the lowest CPL, but total costs and revenue are still very small.

### 3.2. Efficiency by Campaign

The **CVS** campaign accounts for the majority of revenue (2.42 billion VND) with a ROAS of 2.42. However, smaller campaigns like **Guu-Discovery** have a higher ROAS (3.06).

**Conclusion:** If the business decides to shift a large portion of the budget from FB to Google (or vice-versa) in the coming month, a simple time-series forecast model will not be able to capture this sudden change in performance.

---

## 4. Personnel Performance Analysis

The performance of Marketers and Sales staff is a human factor directly affecting the conversion of Leads into Revenue.

### 4.1. Marketer Performance

| Marketer | Revenue (VND) | Marketing Cost (VND) | ROAS |
| :--- | :--- | :--- | :--- |
| **NgocNgo** | 1,251,666,000 | 479,175,063 | **2.61** |
| **GiangPhan** | 510,523,600 | 234,168,267 | **2.18** |
| **DucVu** | 492,454,100 | 207,650,866 | **2.37** |

The variation in ROAS among Marketers (from 2.18 to 2.61) shows that the **campaign management quality** of each individual impacts spending efficiency. If a high-ROAS Marketer leaves or a low-ROAS Marketer is assigned a larger budget, the forecast will be skewed.

### 4.2. Sales Performance

| Sales | Total Amount (VND) | Avg. Interactions/Lead |
| :--- | :--- | :--- |
| **ThuyTran** | 2,685,044,000 | 1.00 |
| **ChiLe12** | 116,389,000 | 2.60 |
| **HuongDinh** | 114,383,000 | 4.71 |

**ThuyTran** handles the bulk of the revenue and has a very low average number of interactions (1.00), suggesting this may be the team handling direct orders or high-quality leads. The performance of the Sales team, particularly **ThuyTran**, is an extremely sensitive variable.

---

## 5. Conclusion and Recommendations for Model Improvement

Non-temporal factors that may affect the accuracy of next month's revenue forecast include:

| Factor | Impact on Forecast | Model Improvement Recommendation |
| :--- | :--- | :--- |
| **Marketing Cost** | A correlation of 0.60 indicates cost is an important explanatory variable. If next month's budget changes, the forecast will be incorrect. | **Integration:** Use the expected **Marketing Cost** for next month as an Exogenous Variable in the model. |
| **Advertising Channel** | ROAS differs greatly between channels (Google 23.54 vs. FB 2.36). Changes in budget allocation will skew the forecast. | **Integration:** Create Dummy Variables for Channels or use **Average ROAS by Channel** as a feature. |
| **Personnel Performance** | Differences in Marketer ROAS and Sales conversion performance. | **Integration:** Use **Average Marketer ROAS** or **Sales Conversion Rate** as features. |
| **Unexpected Events** | Major promotional campaigns, new product launches, or major holidays. | **Integration:** Create dummy variables for days with special events. |

To achieve more accurate forecasts, the model needs to be upgraded to rely not only on historical data but also on the **Marketing spending plan** and expected **channel allocation** for the coming month.