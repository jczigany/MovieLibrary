import os

images_folder = os.path.join(os.path.dirname(__file__), "images")
posters = [os.path.join(images_folder, i) for i in os.listdir(images_folder)]

description = "lkíadlakas al al alaadl  laaÉ  WRII  LK lF  L"

def create_dummy_data(number = 10):
    import random

    movie_list = []

    titles = [
        "Shark",
        "Alien",
        "Terminator",
        "Star Wars",
        "Star Trek"
    ]

    years = [
        1970,
        1980,
        1990,
        2000
    ]

    genres = [
        "action",
        "comedy",
        "thriller",
        "horror",
        "sci-fi"
    ]

    for i in range(number):
        movie_list.append(
            {
                "Title:" : random.choice(titles),
                "Year:" : random.choice(years),
                "genre:" : random.choice(genres),
                "poster:" : random.choice(posters),
                "description:" : description
            }
        )

    return movie_list

if __name__ == '__main__':
    for m in create_dummy_data(12):
        print(m)