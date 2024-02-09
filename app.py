import streamlit as st  
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset
df = pd.read_csv('./nike_data_2022.csv')

# Extract relevant columns
relevant = df[["images", "name", "sub_title"]]

# Set of English stopwords
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Tokenization
    words = word_tokenize(text.lower())
    # Remove stopwords and single character words
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(words)

# Preprocess descriptions
relevant['preprocessed_sub_title'] = relevant['sub_title'].apply(preprocess_text)

# Feature extraction using CountVectorizer
count_vectorizer = CountVectorizer()

# Fit and transform CountVectorizer
cv = count_vectorizer.fit_transform(relevant['preprocessed_sub_title'])

# Clustering
kmeans = KMeans(n_clusters=3, random_state=1)
clusters = kmeans.fit_predict(cv)

# Add cluster labels to the dataframe
relevant['cluster'] = clusters

# Group by cluster and get the products in each cluster
products_by_cluster = relevant.groupby('cluster')['name'].apply(list).reset_index(name='products')

# Initialize list to store products grouped by cluster
products_by_cluster = []

# Filter products for current cluster
for i in range(3):
    cluster_products = relevant[relevant['cluster'] == i]
    # Initialize list to store products in current cluster
    products = []
    for _, product in cluster_products.iterrows():
        product_info = {
            'image': product['images'],
            'name': product['name'],
            'subtitle': product['sub_title'], 
        }
        # Append product info to list of products
        products.append(product_info)
   
    # Append list of products to list of products by cluster
    products_by_cluster.append(products)

# Set page title and icon
st.set_page_config(
    page_title="Nike's Products Clustering",
    page_icon="images/nike.jpeg"
)
st.title("✔️ Nike's Products clustered ✔️")
st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)
st.markdown("""Explore clusters of Nike's products conveniently grouped based on their similarity of the image description. """)
st.markdown("<div style='padding: 10px'></div>", unsafe_allow_html=True)

# Display products grouped by cluster
for cluster_num, cluster_products in enumerate(products_by_cluster):
    st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)
    current_cluster = cluster_num + 1
    cluster_title = f'<h3 style="color:darkgreen; font-weight:bold;">Cluster {cluster_num + 1} - {len(cluster_products)} Products </h3>'
    st.markdown(cluster_title, unsafe_allow_html=True)
    
    for product in cluster_products:
        image_url = str(product['image']) 
        # Check if the image URL is valid
        if image_url.strip() and image_url.lower() != 'nan':  
            st.image(image_url.split(" | ")[0])
        st.subheader(product['name'])
        st.write(product['subtitle'])
        st.markdown("---")
    st.markdown("<div style='padding: 20px'></div>", unsafe_allow_html=True)
    
