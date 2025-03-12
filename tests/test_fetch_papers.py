import unittest
from pubmed_paper_fetcher.filters import extract_non_academic_authors

class TestFilters(unittest.TestCase):
    def test_non_academic_authors(self):
        authors = [
            {"name": "Dr. John Doe", "affiliation": "XYZ Pharma Inc.", "email": "john@xyzpharma.com", "role": "corresponding author"},
            {"name": "Dr. Alice Smith", "affiliation": "Harvard University", "email": "alice@harvard.edu"},
        ]
        non_academic_authors, company_affiliations, email = extract_non_academic_authors(authors)

        self.assertIn("Dr. John Doe", non_academic_authors)
        self.assertIn("XYZ Pharma Inc.".lower(), [c.lower() for c in company_affiliations])
        self.assertEqual(email, "john@xyzpharma.com")  # ✅ This should now pass

if __name__ == "__main__":
    unittest.main()
