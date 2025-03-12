# pubmed-paper-fetcher
A command-line tool to fetch research papers from PubMed based on user queries and filter papers with at least one author affiliated with a pharmaceutical or biotech company. The results are saved as a CSV file.
## Features
•	Fetches papers from the PubMed API based on a search query.<br/>
•	Identifies non-academic authors affiliated with pharmaceutical or biotech companies. <br/>
•	Exports results as a CSV file with details such as PubmedID, Title, Publication Date, Author Details, and Company Affiliation.<br/>
•	Supports command-line options (--debug, --file).<br/>
•	Uses Poetry for dependency management.<br/>
•	Includes unit tests for robustness.<br/>
## Installation
1.	Clone the Repository
```bash
git clone https://github.com/dineshreddie/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```
2.	Install Dependencies (Using Poetry)
```bash
poetry install
```
## Usage
### Basic Command
Run the script with a search query:
```bash
poetry run get-papers-list "cancer treatment"
```
This fetches papers related to "cancer treatment" and prints the output.
### Save Results to a CSV File
```bash
poetry run get-papers-list "diabetes research" --file results.csv
```
This saves the output in results.csv.
## Project Structure
```
pubmed_paper_fetcher/<br/>
│── pubmed_paper_fetcher/<br/>
│   │── __init__.py<br/>
│   │── fetch_papers.py  # Fetches data from PubMed<br/>
│   │── filters.py        # Identifies non-academic authors<br/>
│   │── utils.py          # Helper functions<br/>
│── scripts/<br/>
│   │── get_papers_list.py # CLI script<br/>
│── tests/<br/>
│   │── test_fetch_papers.py # Unit tests<br/>
│── README.md<br/>
│── pyproject.toml<br/>
│── poetry.lock<br/>
```
## Development
### Run Tests
```bash
pytest tests/
```
## Deployment
To publish this package to TestPyPI, use:
```bash
poetry build
poetry publish -r testpypi
```
## Technologies Used
•	Python 3.8+<br/>
•	Poetry (Dependency Management)<br/>
•	Requests (API Calls)<br/>
•	Pandas (Data Processing)<br/>
•	Argparse (CLI Argument Parsing)<br/>
