class Chase:
    def __init__(self):
        self.name = 'Chase Horton'

        self.favoriteMovies = ['The Godfather', 'The Shawshank Redemption', 'LOTR', 'Any Stanley Kubrick film']

        self.hobbies = ['Coding in python and JS','Dancing', 'Biking', 'Playing Chess']

        self.currentlyLearning = ['TailwindCSS','Rust']

        self.wantToLearn = ['Go', 'TypeScript', 'More PHP']

me = Chase()

for key in me.__dict__:
    print(key + ': ' + str(me.__dict__[key]))