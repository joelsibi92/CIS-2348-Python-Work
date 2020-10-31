class Artist:
    def __init__(self, name='None', birth_year=0, death_year=0):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        if (self.death_year == -1):
            print('Artist:', self.name, end=',')
            print(' born', self.birth_year)
        else:
            print('Artist:', self.name, '(', end='')
            print(self.birth_year, end='-')
            print(self.death_year, end=')\n')
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)

    # TODO: Define print_info() method. If death_year is -1, only print birth_year


class Artwork:
    def __init__(self, title='None', year_created='0', artist=''):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        print('Title: {}, {}'.format(self.title, self.year_created))
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)

    # TODO: Define print_info() method


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
    user_artist.print_info()
    new_artwork.print_info()
