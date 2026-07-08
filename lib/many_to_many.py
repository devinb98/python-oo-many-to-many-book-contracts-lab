class Author:
    all = []  # tracks every Author instance
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # all contracts belonging to this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # books this author has contracts for
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # create a new contract linking this author and book
        Contract(self, book, date, royalties)

    def total_royalties(self):
        # sum of royalties across all this author's contracts
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all = []  # tracks every Book instance
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # all contracts for this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # authors who have contracts for this book
        return [contract.author for contract in self.contracts()]

class Contract:
    all = []  # tracks every Contract instance
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def contracts_by_date(self):
        # all contracts sorted by date
        return sorted(Contract.all, key=lambda contract: contract.date)
