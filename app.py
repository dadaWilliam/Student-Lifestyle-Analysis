# Student Lifestyle Analysis App - Reactive Version
# This app analyzes the relationship between student lifestyle factors and academic performance

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from preswald import connect, get_df, text, table, slider, plotly, query

# Initialize connection and load data
connect()  # Initialize connection to preswald.toml data sources
df = get_df("lifestyle_csv")  # Load the student lifestyle dataset

# Title and Introduction
text("# Student Lifestyle and Academic Performance Analysis")
text("This dashboard explores how lifestyle factors impact students' academic performance (GPA).")

# Dataset Overview
text("## Dataset Overview")
text(f"Total number of records: {len(df)}")
table(df.head(10), title="Sample Data (First 10 Records)")

# Make sure Grades is numeric
df["Grades"] = pd.to_numeric(df["Grades"], errors="coerce")

# Basic Filtering Section
text("## Filter by Grade")

# First, define the slider
min_grade = slider("Minimum Grade", 
                  min_val=float(df["Grades"].min()), 
                  max_val=float(df["Grades"].max()), 
                  default=6.0)

# Then immediately use that value to filter the data
filtered_df = df[df["Grades"] >= min_grade]

# Then display the filtered data
table(filtered_df, title=f"Students with Grades ≥ {min_grade}")

# Display summary statistics about the filtered data
text(f"### Summary for Students with Grades ≥ {min_grade}")
text(f"Number of students: {len(filtered_df)}")
text(f"Average study hours: {filtered_df['Study_Hours_Per_Day'].mean():.2f}")
text(f"Average sleep hours: {filtered_df['Sleep_Hours_Per_Day'].mean():.2f}")

# Visualization for the filtered data
text("### Study Hours vs. Grades")
fig_scatter = px.scatter(
    filtered_df,
    x="Study_Hours_Per_Day",
    y="Grades",
    color="Stress_Level",
    hover_data=["Sleep_Hours_Per_Day", "Gender"],
    title=f"Study Hours vs. Grades (Grade ≥ {min_grade})"
)
plotly(fig_scatter)

# Sleep Analysis Section
text("## Sleep Hours Analysis")

# Create a slider for sleep hours
min_sleep = slider("Minimum Sleep Hours", 
                  min_val=float(df["Sleep_Hours_Per_Day"].min()), 
                  max_val=float(df["Sleep_Hours_Per_Day"].max()), 
                  default=7.0)

# Immediately filter based on sleep hours
sleep_filtered = df[df["Sleep_Hours_Per_Day"] >= min_sleep]

# Display table of filtered data
table(sleep_filtered, title=f"Students with Sleep Hours ≥ {min_sleep}")

# Summary statistics
text(f"### Summary for Students with Sleep Hours ≥ {min_sleep}")
text(f"Number of students: {len(sleep_filtered)}")
text(f"Average grade: {sleep_filtered['Grades'].mean():.2f}")

# Sleep hours visualization
sleep_fig = px.scatter(
    sleep_filtered,
    x="Sleep_Hours_Per_Day",
    y="Grades",
    color="Stress_Level",
    hover_data=["Study_Hours_Per_Day", "Gender"],
    title=f"Sleep Hours vs. Grades (Sleep ≥ {min_sleep})"
)
plotly(sleep_fig)

# Stress Level Analysis
text("## Stress Level Analysis")

# Get unique stress levels
stress_levels = sorted(df["Stress_Level"].unique().tolist())

# Create a slider for selecting stress level by index
stress_index = slider("Stress Level Index", 
                     min_val=0, 
                     max_val=len(stress_levels)-1, 
                     default=0)

# Get the selected stress level
selected_stress = stress_levels[stress_index]

# Filter by selected stress level
stress_filtered = df[df["Stress_Level"] == selected_stress]

# Display filtered data
text(f"### Data for '{selected_stress}' Stress Level")
table(stress_filtered, title=f"Students with {selected_stress} Stress Level")

# Create summary statistics
text(f"### Summary for {selected_stress} Stress Level")
text(f"Number of students: {len(stress_filtered)}")
text(f"Average grade: {stress_filtered['Grades'].mean():.2f}")
text(f"Average study hours: {stress_filtered['Study_Hours_Per_Day'].mean():.2f}")
text(f"Average sleep hours: {stress_filtered['Sleep_Hours_Per_Day'].mean():.2f}")

# Create visualization
stress_fig = px.histogram(
    stress_filtered,
    x="Grades",
    nbins=20,
    title=f"Grade Distribution for {selected_stress} Stress Level"
)
plotly(stress_fig)

# Physical Activity Analysis
text("## Physical Activity Analysis")

# Create slider for physical activity
min_activity = slider("Minimum Physical Activity Hours", 
                     min_val=float(df["Physical_Activity_Hours_Per_Day"].min()), 
                     max_val=float(df["Physical_Activity_Hours_Per_Day"].max()), 
                     default=1.0)

# Filter by physical activity
activity_filtered = df[df["Physical_Activity_Hours_Per_Day"] >= min_activity]

# Display filtered data
table(activity_filtered, title=f"Students with Physical Activity ≥ {min_activity} hours")

# Create visualization
activity_fig = px.scatter(
    activity_filtered,
    x="Physical_Activity_Hours_Per_Day",
    y="Grades",
    color="Stress_Level",
    hover_data=["Study_Hours_Per_Day", "Sleep_Hours_Per_Day", "Gender"],
    title=f"Physical Activity vs. Grades (Activity ≥ {min_activity} hours)"
)
plotly(activity_fig)

# Correlation Analysis (numeric columns only)
text("## Correlation Analysis")

# Select only numeric columns for correlation
numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
numeric_df = df[numeric_columns]

# Calculate correlation
correlation = numeric_df.corr()["Grades"].sort_values(ascending=False)
correlation_df = pd.DataFrame({
    "Factor": correlation.index, 
    "Correlation with Grades": correlation.values
})

# Display correlation table
table(correlation_df, title="Correlation with Grades")

# Create bar chart
corr_fig = px.bar(
    correlation_df, 
    x="Factor", 
    y="Correlation with Grades",
    title="Factors Correlated with Academic Performance",
    color="Correlation with Grades",
    color_continuous_scale="RdBu_r"
)
plotly(corr_fig)

# SQL Query Example
text("## SQL Query Example")
text("Finding students with grades above average for each stress level:")

# Execute SQL query
sql_results = query("""
SELECT 
    Stress_Level,
    Student_ID,
    Gender,
    Grades,
    Study_Hours_Per_Day,
    Sleep_Hours_Per_Day
FROM lifestyle_csv
WHERE Grades > (
    SELECT AVG(Grades) 
    FROM lifestyle_csv t2 
    WHERE t2.Stress_Level = lifestyle_csv.Stress_Level
)
ORDER BY Stress_Level, Grades DESC
""", "lifestyle_csv")

# Display results
table(sql_results, title="Students with Above-Average Grades for Their Stress Level")

# Conclusion
text("## Key Insights and Conclusions")
text("This dashboard allows you to explore the relationships between lifestyle factors and academic performance.")
text("Try adjusting the sliders to see how different filters affect the data and visualizations.")
