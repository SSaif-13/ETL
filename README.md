This is a simple ETL designed to extract, transform, and load CO2 emissions data for any country from the dataset hosted by Our World Data (https://ourworldindata.org/co2-emissions). 
By defaulm it focuses on Canada but it can easily be modified to analyze emissions data for any other country.

Features
Extraction: Fetch the full dataset of global CO₂ emissions directly from the source.
Transformation: Filter and clean the data for a specific country, removing any missing entries.
Loading: Save the processed data as a CSV file for further analysis.

Prerequisites
Ensure you have the following installed:
Python 3.x
pandas library
requests library

Acknowledgements
Thanks to Our World in Data for providing the dataset and enabling global climate research.
