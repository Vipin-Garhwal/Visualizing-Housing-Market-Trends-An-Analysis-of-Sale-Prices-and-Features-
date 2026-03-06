# Data Visualizations for Housing Market Trends Analysis

**Project:** Visualizing Housing Market Trends: An Analysis of Sale Prices and Features  
**Client:** ABC Company  
**Tool:** Tableau  
**Author:** Vipin  
**Date:** 2026-03-05

## Overview

This document summarizes the core Tableau visualizations created to analyze housing market data and uncover insights into sales prices and house features. The goal is to aid ABC Company's strategic decisions by visualizing data patterns across renovation history, age distribution, and key attributes such as bathrooms, bedrooms, and floors.

---

## 1. Overall Data Overview

**Visualization:** KPI Dashboard  
**Type:** Summary with Metrics

**Features:**
- **Total Housing Records:** Count of data entries after cleaning/transformation.
- **Average Sales Price:** Key indicator of general market pricing.
- **Total Basement Area (sq ft):** Sum of basement space across all houses.

**Use:**  
Gives a foundational snapshot of the dataset for stakeholders, highlighting the volume, overall pricing, and property size distribution.

> _Add screenshot of Tableau dashboard here (e.g., ![Overall Data KPIs](image1))_  
> _Sample Tableau Sheet: "Data Overview"_

---

## 2. Total Sales by Years Since Renovation

**Visualization:** Histogram or Bar Chart  
**X-axis:** Years Since Last Renovation  
**Y-axis:** Number of Sales / Total Sales Value  
**Color/Bar Groups:** Sales price ranges (e.g., low, medium, high)

**Use:**  
Shows how recency of renovations relates to sales value and buyer interest. Reveals trends in premium pricing for recently renovated homes.

> _Add screenshot here (e.g., ![Sales by Years Since Renovation](image2))_  
> _Sample Tableau Sheet: "Renovation Sales Histogram"_

---

## 3. Distribution of House Age by Renovation Status

**Visualization:** Pie Chart  
**Slices:**  
- Age Groups (e.g., 0-10, 11-20, 21-40, 41+ years)  
- **Renovation Status:** Sliced to show renovated vs. non-renovated for each age group.

**Use:**  
Visualizes the age profile of the housing inventory and the proportion of homes renovated over time.

> _Add screenshot here (e.g., ![House Age by Renovation Status Pie](image3))_  
> _Sample Tableau Sheet: "Age & Renovation Pie"_

---

## 4. House Age Distribution by Bathrooms, Bedrooms, and Floors

**Visualization:** Grouped Bar Chart  
**Groups:** House Age Bins (e.g., 0-10, 11-20, etc.)  
**Bars within Groups:**  
- Number of Bathrooms
- Number of Bedrooms
- Number of Floors

**Use:**  
Explores how property features are distributed across different age segments, revealing patterns in home design evolution and buyer preferences.

> _Add screenshot here (e.g., ![Age Distribution by Features](image4))_  
> _Sample Tableau Sheet: "Age vs. Bathrooms/Bedrooms/Floors Grouped Bar"_

---

## Notes

- Dashboard interactivity can be enabled for date ranges, renovation status filters, etc.
- Add actual Tableau dashboard screenshots when available.
- All datasets and Tableau workbook files (`.twb` or `.twbx`) should be stored under `/data/` or `/notebooks/` folders.
- For full code and dataset, see respective directories.

---

## How to Use

1. Upload this Markdown file to the **results/** folder (or as a README in the visualizations section).
2. Update the images and links with your actual Tableau dashboard exports and screenshots.
3. Reference this document in your main project README for an organized summary of visual insights.

---

**References:**  
- Data source: ABC Company Housing Dataset (see `/data/`)  
- Tableau documentation: [https://www.tableau.com/learn](https://www.tableau.com/learn)

---

*This document serves as a living guide for your Tableau analysis. Update with screenshots, links, and insights as your project progresses!*
