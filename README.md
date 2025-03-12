# pubmed-paper-fetcher
A command-line tool to fetch research papers from PubMed based on user queries and filter papers with at least one author affiliated with a pharmaceutical or biotech company. The results are saved as a CSV file.
## Features
•	Fetches papers from the PubMed API based on a search query.
•	Identifies non-academic authors affiliated with pharmaceutical or biotech companies. 
•	Exports results as a CSV file with details such as PubmedID, Title, Publication Date, Author Details, and Company Affiliation.
•	Supports command-line options (--debug, --file).
•	Uses Poetry for dependency management.
•	Includes unit tests for robustness.
## Installation
1.	Clone the Repository
git clone https://github.com/dineshreddie/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
2.	Install Dependencies (Using Poetry)
poetry install
## Usage
### Basic Command
Run the script with a search query:
poetry run get-papers-list "cancer treatment"
This fetches papers related to "cancer treatment" and prints the output.
### Save Results to a CSV File
poetry run get-papers-list "diabetes research" --file results.csv
This saves the output in results.csv.
## Project Structure
pubmed_paper_fetcher/
│── pubmed_paper_fetcher/
│   │── __init__.py
│   │── fetch_papers.py  # Fetches data from PubMed
│   │── filters.py        # Identifies non-academic authors
│   │── utils.py          # Helper functions
│── scripts/
│   │── get_papers_list.py # CLI script
│── tests/
│   │── test_fetch_papers.py # Unit tests
│── README.md
│── pyproject.toml
│── poetry.lock
## Deployment
To publish this package to TestPyPI, use:
poetry build
poetry publish -r testpypi
## Technologies Used
•	Python 3.8+
•	Poetry (Dependency Management)
•	Requests (API Calls)
•	Pandas (Data Processing)
•	Argparse (CLI Argument Parsing)
