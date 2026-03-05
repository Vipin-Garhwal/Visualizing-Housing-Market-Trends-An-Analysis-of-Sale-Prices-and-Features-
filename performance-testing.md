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