import requests
import pandas as pd
from typing import List, Dict
from xml.etree import ElementTree as ET

# PubMed API URLs
PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_papers(query: str) -> List[Dict]:
    """Fetch papers from PubMed using Entrez API."""
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": 10,  # Fetch up to 10 papers
        "retmode": "json"
    }

    search_response = requests.get(PUBMED_SEARCH_URL, params=search_params)
    if search_response.status_code != 200:
        raise Exception(f"Failed to search PubMed: {search_response.status_code}")

    search_data = search_response.json()
    pubmed_ids = search_data.get("esearchresult", {}).get("idlist", [])

    if not pubmed_ids:
        raise Exception("No papers found for the given query.")

    return fetch_full_paper_details(pubmed_ids)

def fetch_full_paper_details(pubmed_ids: List[str]) -> List[Dict]:
    """Fetch detailed paper information including authors from PubMed."""
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"  # Fetch full structured XML response
    }

    fetch_response = requests.get(PUBMED_FETCH_URL, params=fetch_params)
    if fetch_response.status_code != 200:
        raise Exception(f"Failed to fetch paper details: {fetch_response.status_code}")

    return parse_paper_details(fetch_response.text)

def parse_paper_details(xml_data: str) -> List[Dict]:
    """Parse XML response and extract required fields."""
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text
        pub_date = article.find(".//PubDate/Year")
        publication_date = pub_date.text if pub_date is not None else "Unknown"

        # Extract author details
        authors, companies, corresponding_email = extract_author_info(article)

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": publication_date,
            "Non-academic Author(s)": ", ".join(authors) if authors else "N/A",
            "Company Affiliation(s)": ", ".join(companies) if companies else "N/A",
            "Corresponding Author Email": corresponding_email if corresponding_email else "N/A"
        })

    return papers

def extract_author_info(article) -> (List[str], List[str], str):
    """Extract author names, company affiliations, and corresponding author email."""
    authors = []
    companies = []
    corresponding_email = ""

    for author in article.findall(".//Author"):
        last_name = author.find("LastName")
        fore_name = author.find("ForeName")
        full_name = f"{fore_name.text} {last_name.text}" if last_name is not None and fore_name is not None else "Unknown"

        affiliation = author.find("Affiliation")
        aff_text = affiliation.text if affiliation is not None else ""

        if any(keyword in aff_text.lower() for keyword in ["pharma", "biotech", "inc.", "ltd", "gmbh"]):
            companies.append(aff_text)
            authors.append(full_name)

        if "corresponding" in aff_text.lower():
            email = author.find("Email")
            corresponding_email = email.text if email is not None else ""

    return authors, companies, corresponding_email

def extract_relevant_data(papers: List[Dict]) -> pd.DataFrame:
    """Extract relevant information and return as a DataFrame."""
    return pd.DataFrame(papers)


# poetry run get-papers-list "cancer treatment" -f finalresults.csv 