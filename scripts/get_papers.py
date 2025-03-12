import argparse
import pandas as pd
from pubmed_paper_fetcher.fetch_papers import fetch_papers, extract_relevant_data

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file name", default="papers.csv")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    papers = fetch_papers(args.query)
    df = extract_relevant_data(papers)

    # Save DataFrame to CSV
    df.to_csv(args.file, index=False)
    print(f"Results saved to {args.file}")

if __name__ == "__main__":
    main()
