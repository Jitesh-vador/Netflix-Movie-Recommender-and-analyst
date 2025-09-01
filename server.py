import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

print("--- Starting Netflix Data Processing and Model Building ---")

# --- Step 1: Load and Clean the Dataset ---
try:
    df = pd.read_csv('netflix_titles.csv')
    print("Dataset 'netflix_titles.csv' loaded successfully.")
except FileNotFoundError:
    print("[ERROR] 'netflix_titles.csv' not found. Please make sure the file is in the same directory.")
    exit()

# Handle missing values using the recommended syntax to avoid warnings
df['director'] = df['director'].fillna('No Director')
df['cast'] = df['cast'].fillna('No Cast')
df['country'] = df['country'].fillna('No Country')
df.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)

# --- NEW: Sample the data to speed up processing ---
# We'll take a random sample of 2000 titles to make the model build much faster.
# This is great for development and for the final web app's performance.
print(f"Original dataset size: {len(df)} titles.")
df = df.sample(n=2000, random_state=42).reset_index(drop=True)
print(f"Working with a sample of: {len(df)} titles to ensure fast performance.")


# --- Step 2: Feature Engineering for the Recommendation Model ---
# We will create a 'soup' of features for each title to feed into the model
df['features'] = df['listed_in'] + ' ' + df['description'] + ' ' + df['director'] + ' ' + df['cast']
print("Feature engineering complete. Combined features into a single string for each title.")

# --- Step 3: Build the Content-Based Recommendation Model ---
# Use TF-IDF to convert the text features into a matrix of word importance
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['features'])

# Calculate the cosine similarity between all titles
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("TF-IDF matrix and Cosine Similarity model built successfully.")

# Create a mapping from title to index for easy lookups
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# --- Step 4: Prepare Data for the Analysis Section ---
print("Preparing data for the analysis dashboard...")
# Analysis 1: Content Type Distribution (Movie vs. TV Show)
content_type = df['type'].value_counts().reset_index()
content_type.columns = ['type', 'count']

# Analysis 2: Top 10 Directors
top_directors = df[df['director'] != 'No Director']['director'].value_counts().nlargest(10).reset_index()
top_directors.columns = ['director', 'count']

# Analysis 3: Top 10 Countries with the most content
top_countries = df[df['country'] != 'No Country']['country'].value_counts().nlargest(10).reset_index()
top_countries.columns = ['country', 'count']

# --- Step 5: Consolidate and Export All Data to JSON ---
# We need to export all the necessary data so our HTML/JS file can use it.
# The main dataframe contains all the details for each title.
# The similarity matrix is needed for the recommendation logic.
# The analysis data will be used to create the graphs.

# Convert the cosine similarity matrix to a list of lists for JSON compatibility
cosine_sim_list = cosine_sim.tolist()

# Convert all dataframes to dictionary format
all_titles_dict = df.to_dict(orient='records')
content_type_dict = content_type.to_dict(orient='records')
top_directors_dict = top_directors.to_dict(orient='records')
top_countries_dict = top_countries.to_dict(orient='records')
indices_dict = indices.to_dict()

# Combine everything into a single dictionary
export_data = {
    'titles': all_titles_dict,
    'similarity_matrix': cosine_sim_list,
    'indices': indices_dict,
    'analysis': {
        'content_type': content_type_dict,
        'top_directors': top_directors_dict,
        'top_countries': top_countries_dict
    }
}

# Save the consolidated data to a JSON file
with open('netflix_data.json', 'w') as f:
    json.dump(export_data, f)

print("\n[SUCCESS] All data has been processed and saved to 'netflix_data.json'.")
print("You are now ready for the next step.")

