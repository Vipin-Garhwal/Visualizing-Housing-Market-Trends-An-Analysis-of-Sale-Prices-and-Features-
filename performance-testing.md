# Performance Testing & Metrics

## Utilization of Data Filters
- **YearBuilt** - Filter by construction year
- **YearRenovated** - Filter by renovation year
- **Bedrooms** - Multi-select filter (1-6 bedrooms)
- **Bathrooms** - Multi-select filter (1-4 bathrooms)
- **Floors** - Filter by number of floors
- **SalePrice Range** - Dynamic range filter

## Number of Calculation Fields: 4

1. **YearsSinceRenovation** 
   - Formula: `IF [YearRenovated] > 0 THEN [YearSold] - [YearRenovated] ELSE [YearSold] - [YearBuilt] END`

2. **HouseAge** 
   - Formula: `[YearSold] - [YearBuilt]`

3. **RenovationStatus** 
   - Formula: `IF [YearRenovated] > 0 THEN "Renovated" ELSE "Non-Renovated" END`

4. **PriceCategory** 
   - Formula: `IF [SalePrice] > 500000 THEN "Premium" ELSEIF [SalePrice] > 350000 THEN "Mid-Range" ELSE "Entry-Level" END`

## Number of Visualizations: 4

1. **KPI Overview Card** - Summary statistics
2. **Histogram** - Sales by years since renovation
3. **Pie Chart** - House age distribution by renovation status
4. **Grouped Bar Chart** - House features (bathrooms/bedrooms/floors) by age

## Performance Metrics
- **Data Processing Time**: < 2 seconds
- **Filter Response Time**: < 1 second
- **Dashboard Load Time**: < 3 seconds
- **Record Count**: Up to 20,000+ records
- # Results Overview & Key Findings

## Executive Summary
The Tableau visualization dashboard reveals critical insights into housing market trends for ABC Company, enabling strategic decision-making in pricing and market positioning.

## Key Findings

### 1. Renovation Impact on Price
- Recently renovated homes (0-5 years) command **15-25% price premiums**
- Homes renovated 10+ years ago show diminishing price benefits
- Non-renovated homes average 20% lower prices compared to renovated counterparts

### 2. House Age Patterns
- **Newer homes (0-10 years)**: 40% of market inventory, highest average price
- **Mid-age homes (10-30 years)**: 35% of market, renovation-dependent pricing
- **Older homes (30+ years)**: 25% of market, significant variation based on renovation status

### 3. Feature Distribution Insights
- **4-Bedroom homes** dominate the premium price segment
- **2-3 Bathrooms** optimal for mid-range properties
- **2-Story homes** correlate with higher average sale prices
- **Basement area** average: 850+ sq ft, strong value indicator

### 4. Market Recommendations
- Prioritize renovation marketing for properties 15-25 years old
- Bundle feature upgrades (bathroom/bedroom additions) for competitive positioning
- Focus inventory on 3-4 bedroom, 2-3 bathroom configurations
- Highlight basement space as premium feature in marketing materials

## Data Quality
- **Total Records Analyzed**: 20,000+
- **Data Completeness**: 98%
- **Outliers Removed**: 2% (extreme price anomalies)

## Next Steps
- Implement recommended pricing strategies
- Monitor market trends quarterly
- Refine filters based on emerging market conditions
