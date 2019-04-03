# 08 - Data Wrangling

## Introduction to Data Wrangling
1. Process of gathering your data
2. Assessing its quality and structure
3. Cleaning it before you do things like analysis, visualization, or build predictive models using machine learning.

### Gathering Data
- Depending on the source of your data, and what format it's in, the steps in gathering data vary.
- High-level gathering process: obtaining data (downloading a file from the internet, scraping a web page, querying an API, etc.) and importing that data into your programming environment (e.g., Jupyter Notebook).

### Assessing Data
- Assess data for:

  - Quality: issues with content. Low quality data is also known as dirty data.
  - Tidiness: issues with structure that prevent easy analysis. Untidy data is also known as messy data. Tidy data requirements:
    1. Each variable forms a column.
    2. Each observation forms a row.
    3. Each type of observational unit forms a table.

- Types of assessment:

  - Visual assessment: scrolling through the data in your preferred software application (Google Sheets, Excel, a text editor, etc.).
  - Programmatic assessment: using code to view specific portions and summaries of the data (pandas' head, tail, and info methods, for example).

### Cleaning Data
- Types of cleaning:
  - Manual (not recommended unless the issues are single occurrences)
  - Programmatic

- The programmatic data cleaning process:
  1. Define: convert our assessments into defined cleaning tasks. These definitions also serve as an instruction list so others (or yourself in the future) can look at your work and reproduce it.
  2. Code: convert those definitions to code and run that code.
  3. Test: test your dataset, visually or with code, to make sure your cleaning operations worked.

- Always make copies of the original pieces of data before cleaning!

### Storing Data (Optional)
- Store data, in a file or database for example, if you need to use it in the future.

### Wrangling vs. EDA
- Data wrangling is about gathering the right pieces of data, assessing your data's quality and structure, then modifying your data to make it clean. But the assessments you make and convert to cleaning operations won't make your analysis, viz, or model better, though. The goal is to just make them possible, i.e., functional.

- EDA is about exploring your data to later augment it to maximize the potential of our analyses, visualizations, and models. When exploring, simple visualizations are often used to summarize your data's main characteristics. From there you can do things like remove outliers and create new and more descriptive features from existing data, also known as feature engineering. Or detect and remove outliers so your model's fit is better.

- In practice, wrangling and EDA can and often do occur together.

### ETL (extract-transform-load)
- ETL differs from data wrangling in three main ways:

  - The users are different
  - The data is different
  - The use cases are different
