class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry

    def __str__(self):
        return f"Company Name: {self.name}, Industry: {self.industry}"


'''Încapsulare: Clasa Company încapsulează datele referitoare la o companie, cum ar fi numele și industria,
utilizând constructorul __init__.
   Abstracție: Clasa Company oferă o interfață abstractă pentru a reprezenta o companie în codul Python,
ascunzând detalii specifice cum ar fi implementarea proprietăților și metodelor interne.
   Polimorfism: Prin implementarea metodei speciale __str__, clasa Company oferă o reprezentare sub formă de string a obiectului său, 
permițând utilizarea funcției print cu obiecte de tip Company.
    '''
