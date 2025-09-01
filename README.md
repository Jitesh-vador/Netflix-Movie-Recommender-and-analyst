Netflix Interactive Recommendation System
An interactive movie and TV show recommendation system that uses a content-based machine learning model to suggest similar titles. This project features a two-part web interface: a recommendation engine with dynamic filtering and a dashboard for data analysis of the Netflix dataset.

The entire backend model is built with Python, Pandas, and Scikit-learn, while the frontend is a self-contained HTML/JavaScript application using Plotly.js for visualizations.

Dashboard Preview
Below are images of the interactive dashboard, showing the two main sections of the application.
<img width="1884" height="944" alt="image" src="https://github.com/user-attachments/assets/629523c3-d1a4-4ef7-b73b-c2660fbb1a5e" />


Recommendation Engine
Shows the main UI with genre/rating filters and the grid of selectable movie/TV show titles.
<img width="1884" height="944" alt="image" src="https://github.com/user-attachments/assets/2d682a3c-da75-43d1-84aa-635e74d2e600" />


Analysis Dashboard
Shows the data analysis tab with charts for content distribution, top directors, and top countries.
<img width="1319" height="607" alt="image" src="https://github.com/user-attachments/assets/9b28d67d-6914-4ea8-83e0-7656ba85de86" />
<img width="768" height="545" alt="image" src="https://github.com/user-attachments/assets/0957af0c-8dfe-4b03-84d8-b2507c2361cf" />


Features
Interactive Recommendation UI: A Netflix-themed interface where users can filter content by type (Movie/TV Show), genre, and rating.

Content-Based ML Model: Recommendations are powered by a Scikit-learn model that analyzes movie descriptions, genres, cast, and directors to find titles with the highest content similarity.

Detailed Information Modal: Clicking on any title opens a pop-up with detailed information, including a plot summary, cast, director, and a list of 5 similar titles recommended by the model.

Data Analysis Dashboard: A separate tab visualizes key insights from the dataset, including:

The distribution of Movies vs. TV Shows.

The top 10 directors with the most content on the platform.

The top 10 countries producing content.

How It Works
This project is built on a two-step process:

Data Processing & Model Training (data_processor.py)
This Python script is the backend engine. It runs once to:

Load the netflix_titles.csv dataset.

Clean and preprocess the data using Pandas.

Construct a feature matrix using TfidfVectorizer from Scikit-learn.

Build a cosine_similarity matrix to compare all titles.

Package all necessary data (title details, similarity matrix, analysis data) into a single netflix_data.json file.

Frontend Interface & Server (index.html & server.py)

The index.html file is a single-page application that reads the netflix_data.json file.

It uses JavaScript to dynamically filter titles, calculate recommendations based on the pre-computed model, and render the interactive charts with Plotly.js.

The server.py script launches a simple local web server to host the index.html file, allowing it to fetch the JSON data without running into browser security restrictions.

How to Run This Project Locally
Prerequisites: Ensure you have Python 3 and the following libraries installed:

pip install pandas scikit-learn

Process the Data: First, run the data processing script to build the model and create the JSON file. Make sure netflix_titles.csv is in your project folder.

python data_processor.py

Start the Server: Once netflix_data.json has been created, start the local web server.

python server.py
