from typing import List, Tuple

def extract_non_academic_authors(authors: List[dict]) -> Tuple[List[str], List[str], str]:
    """Identify authors affiliated with pharmaceutical/biotech companies."""
    non_academic_authors = []
    company_affiliations = []
    corresponding_email = ""

    for author in authors:
        affiliation = author.get("affiliation", "").lower()
        email = author.get("email", "")
        role = author.get("role", "").lower() if "role" in author else ""  # Handle missing "role" key

        if any(keyword in affiliation for keyword in ["pharma", "biotech", "inc.", "ltd", "gmbh"]):
            non_academic_authors.append(author.get("name", "Unknown"))
            company_affiliations.append(affiliation.title())  # Convert to title case ✅

        # Extract the first non-empty email if a corresponding author is not explicitly marked
        if "corresponding" in role:
            corresponding_email = email  # ✅ Now correctly capturing the corresponding author's email
        elif not corresponding_email and email:  # ✅ Fallback: store the first available email if none is marked "corresponding"
            corresponding_email = email  

    return non_academic_authors, company_affiliations, corresponding_email
