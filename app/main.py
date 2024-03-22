from database import Database
from company import Company


class Website:
    def __init__(self):
        # Inițializăm un obiect de tip Database pentru a gestiona baza de date
        self.db = Database()

    def create_company(self, name, industry):
        # Adăugăm o companie nouă în baza de date
        new_company = Company(name, industry)
        self.db.add_company(new_company)

    def get_company_info(self, name):
        # Obținem informații despre o companie în funcție de nume
        return self.db.get_company_by_name(name)


if __name__ == "__main__":
    website = Website()

    # Lista cu companiile de adăugat
    companies_to_add = [
        ("Company ABC", "IT Services"),
        ("Company AAB", "Finance"),
        ("Company QRS", "Healthcare"),
        ("Company DEF", "Retail"),
        ("Company GHI", "Manufacturing"),
        ("Company JKL", "Education"),
        ("Company VEV", "Consulting"),
        ("Company TUV", "Hospitality"),
        ("Company WXY", "Technology"),
        ("Company PQR", "Automotive")
    ]

    # Adăugăm companiile folosind metoda add_multiple_companies
    website.db.add_multiple_companies(companies_to_add)

    # Afișăm informațiile despre toate companiile adăugate
    for name, _ in companies_to_add:
        company_info = website.get_company_info(name)
        print(company_info)

    # Închidem conexiunea cu baza de date la finalul utilizării
    website.db.close_connection()

'''Încapsulare: Clasa Website încapsulează funcționalitățile legate de gestionarea companiilor și 
comunicarea cu baza de date, oferind metode pentru adăugarea și obținerea informațiilor despre companii.
   Abstracție: Clasa Website abstractizează detaliile specifice ale modului în care sunt gestionate companiile 
și interactiunea cu baza de date, permițând utilizatorului să folosească această funcționalitate fără a cunoaște detaliile interne.
   Polimorfism: Metodele din clasa Website sunt definite într-un mod flexibil, permițând adăugarea 
și obținerea informațiilor despre companii într-un mod transparent pentru utilizator.

'''