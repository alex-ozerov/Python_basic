class BookReview:
    def __init__(self, text):
        self.text = text


class Book:
    def __init__(self, name, author, age, fan):
        self.name = name
        self.author = author
        self.age = age
        self.fan = fan
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        reviews_texts = []
        for review in self.reviews:
            reviews_texts.append(review.text)
        reviews_texts = '\n'.join(reviews_texts)
        return f'Book {self.name}, author {self.author}, age {self.age}, fan {self.fan}\nReviews:\n{reviews_texts}'


book1 = Book('Robinson Crusoe', 'Daniel Defo', '1719', 'adventure')
book2 = Book('Treasure island', 'Robert Louis Stevenson', '1883', 'adventure')
book1.add_review(BookReview("The famous novel by the English writer Daniel Defoe "
                            "The Life and the Amazing Adventures of the Sailor Robinson Crusoe"
                            "was first published almost 300 years ago, becoming a literary sensation."
                            "But even now, after many, many decades, the fascinating adventures of a sailor "
                            "who found himself as a result of a shipwreck on a desert island and courageously "
                            "endure all the difficulties of that difficult life, continue to captivate readers."))
book2.add_review(BookReview("For about a century and a half, children have been reading the novel "
                            "Treasure Island by the English writer Robert Louis Stevenson, and the "
                            "mysterious island with pirate treasures excites the imagination of boys and girls. "
                            "Interestingly, the novel was originally conceived for children. "
                            "It quickly gained popularity around the world and has been translated "
                            "into many languages. Desperate treasure seekers and insidious pirates can also be "
                            "seen on the screen: many films and cartoons have been filmed based on the book. "
                            "For middle school age."))
print(book1)
print(book2)