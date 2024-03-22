import sqlite3
from company import Company


class Database:
    def __init__(self, db_name='companies.db'):
        # Inițializăm conexiunea cu baza de date SQLite
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # Cream tabela companies dacă nu există deja
        self.create_table()

    def create_table(self):
        # Creăm tabela companies cu coloanele id, name și industry
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS companies
                           (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            industry TEXT NOT NULL)''')
        self.connection.commit()

    def add_company(self, company):
        # Adăugăm o companie nouă în baza de date
        self.cursor.execute('''INSERT INTO companies (name, industry) 
                           VALUES (?, ?)''', (company.name, company.industry))
        self.connection.commit()

    def get_company_by_name(self, name):
        # Obținem informații despre o companie în funcție de nume
        self.cursor.execute('''SELECT * FROM companies WHERE name = ?''', (name,))
        company_data = self.cursor.fetchone()
        if company_data:
            return Company(company_data[1], company_data[2])  # Returnăm un obiect Company
        else:
            return None

    def close_connection(self):
        # Închidem conexiunea cu baza de date
        self.connection.close()

    def add_multiple_companies(self, companies):
        # Adăugăm mai multe companii în baza de date
        self.cursor.executemany('''INSERT INTO companies (name, industry) 
                                VALUES (?, ?)''', companies)
        self.connection.commit()


'''Încapsulare: Clasa Database încapsulează interacțiunea cu baza de date SQLite,
oferind metode pentru adăugarea și obținerea datelor legate de companii.
   Abstracție: Clasa Database abstractizează detaliile specifice ale lucrului cu baza de date,
ascunzând implementarea specifică a interogărilor SQL și a conexiunii la baza de date.
   Polimorfism: Metodele din clasa Database sunt definite într-un mod flexibil, 
   permițând utilizarea lor pentru a interacționa cu diferite tipuri de date, cum ar fi obiecte de tip Company.
'''
