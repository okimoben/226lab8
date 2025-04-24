
class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def __eq__(self, other):
        return isinstance(other, ArchiveItem) and self.uid == other.uid

    def is_recent(self, n):
        return self.year >= (2025 - n)


class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.author}, Pages: {self.pages}"


class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f"Article -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal}, DOI: {self.doi}"


class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return f"Podcast -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, Duration: {self.duration} mins"


def save_to_file(items, filename):
    with open(filename, 'w') as f:
        for item in items:
            if isinstance(item, Book):
                f.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                f.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                f.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")


def load_from_file(filename):
    items = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            type_ = parts[0]
            if type_ == 'Book':
                items.append(Book(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
            elif type_ == 'Article':
                items.append(Article(parts[1], parts[2], int(parts[3]), parts[4], parts[5]))
            elif type_ == 'Podcast':
                items.append(Podcast(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
    return items


items = [
    Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
    Book("B002", "Python Crash Course", 2020, "Eric Matthes", 544),
    Article("A001", "Quantum Computing", 2022, "Nature", "10.1234/qc567"),
    Article("A002", "AI Ethics", 2019, "IEEE", "10.5678/ai999"),
    Podcast("P001", "TechTalk AI", 2023, "Jane Doe", 45),
    Podcast("P002", "History Hour", 2017, "John Smith", 60)
]

save_to_file(items, "archive.txt")
loaded_items = load_from_file("archive.txt")

for item in loaded_items:
    print(item)


print("\nRecent Items (last 5 years):")
for item in loaded_items:
    if item.is_recent(5):
        print(item)

print("\nArticles with DOI starting with '10.1234':")
for item in loaded_items:
    if isinstance(item, Article) and item.doi.startswith("10.1234"):
        print(item)
