# NFL-Game_Predictor
NFL Game (win/ loss) prediction model

# README

Initial commit

readme_text = """
# Data Processing and Analysis Summary

## Initial Data Aggregation and Compilation
- Aggregated multiple data files related to different aspects of the game.
- Joined datasets by team and week, keeping all unique columns.
    - Joined Offensive regular season data together, joined Defensive post season data together, joined Offensive regular season data together, joined Offensive post season data together

## Data Cleaning
- Identified and handled null values.
- Replaced specific null values with zeros.
- Standardized team names and aligned data across files.

## Exploratory Data Analysis (EDA)
- Analyzed distributions and relationships between features.
- Calculated and evaluated correlation matrices.
- Tested the significance of correlations and identified multicollinearity.
- Visualized data using heatmaps and other plots.

## Preprocessing
- Standardized numerical features.
- Encoded categorical features.
- Dropped highly correlated features.
- Evaluated the need for normalization and standardization.

## Principal Component Analysis (PCA)
- Applied PCA to reduce dimensionality.
- Transformed data into a compact representation with 20 principal components.

# Modeling

## Model Building and Comparison
- Comparison of models to narrow down which models to work with
- Created top 4 individual models
- Tuned individual models
- Created Stacking Classifier
- Tuned Stacking Classifier

# Testing

## Testing on holdout data and additional unseen data
- Stacking Classifier provided best results in trainging so that was used as final model to test on holdout and unseen data
- Saved model
- Loaded model and checked for save/ load integrity by running unseen data through loaded model and verifying results

# Further Testing

## Evaluating model with post season (playoff) data
- Created new environment where saved model was loaded
- Made predictions using model on post season data

## Conclusion
- Model did not perform as accurately as with the training, holdout and validation/unseen data
- Further finetuning/ hyperparameter tuning will need to be done. Possibly more in depth EDA to better screen for features/ PCA to use in post season environment

## Next Steps
- Potential continuation with model building, further hyperparameter optimizations, feature interpretation, and validation strategy.

---

This document provides a high-level overview of the data processing and analysis performed. Detailed code, visualizations, and explanations are available in the accompanying Python code file.
"""
