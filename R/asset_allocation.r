# Create a sample dataset
data <- data.frame(
  Index_Return = c(0.60, 0.65, 0.70, 0.75, 0.80),
  StockA_Return = c(0.60, 0.62, 0.65, 0.68, 0.70),
  StockB_Return = c(0.60, 0.63, 0.67, 0.70, 0.73),
  StockC_Return = c(0.60, 0.61, 0.63, 0.66, 0.70)
)

# Fit linear regression model
model <- lm(Index_Return ~ StockA_Return + StockB_Return + StockC_Return, data = data)

# Retrieve the coefficients (weights)
weights <- coef(model)[-1]
print(weights)
