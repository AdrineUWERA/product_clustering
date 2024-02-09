# Nike's Products Clustering
## Description

The Nike's products Clustering App is a web application that clusters Nike's products based on their product description similarity using machine learning algorithms. The app preprocesses the product description, applies a clustering algorithm, and displays the clustered Nike's products on the web page. It provides users with an organized view of Nike's products in same category, making it easier to navigate and explore different products in the category. 

## Features

- Clustering: The app cluster the Nike's products based on their product description.
- Display: The app displays the clustered Nike's products on the web page, allowing users to explore related products conveniently.

## Packages Used

This project has used some packages which have to be installed to run this web app locally present in `requirements.txt` file. 

## Installation

To run the project locally, there is a need to have Visual Studio Code (vs code) installed on your PC:

- **[vs code](https://code.visualstudio.com/download)**: It is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux, and macOS.

## Usage

1. Clone the project 

``` bash
git clone https://github.com/AdrineUWERA/product_clustering.git

```

2. Open the project with vs code

``` bash
cd product_clustering
code .
```

3. Install the required dependencies

``` bash
pip install -r requirements.txt
```


4. Run the project

``` bash
streamlit run app.py
```

5. Use the link printed in the terminal to visualise the app. (Usually `http://localhost:8501`)

## Important Notes
- The app is designed to cluster specifically with only for the already fetched articles

## Authors and Acknowledgment

- Adrine Uwera 

## License
[MIT](https://choosealicense.com/licenses/mit/)
