import os

images_folder = os.path.join(os.path.dirname(__file__), "images")
posters = [os.path.join(images_folder, i) for i in os.listdir(images_folder)]

description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore"

def create_dummy_data(number=10):
    import random
    movie_list = []

    titles = [
        "Shark",
        "Alien",
        "Parasite",
        "Star Wars",
        "Charlie's Angels",
        "Ad Astra",
    ]

    years = [
        "December 4, 2019",
        "February 26, 2020",
        "May 30, 2019",
        "February 5, 2020",
        "October 2, 2019",
    ]

    genres = [
        "action",
        "comedy",
        "thriller",
        "horror",
        "sci-fi",
    ]

    for i in range(number):
        movie_list.append(
            {
                "title": random.choice(titles),
                "release_date": random.choice(years),
                "genre": random.choice(genres),
                "poster": random.choice(posters),
                "description": description
            }
        )

    return movie_list

if __name__ == '__main__':
    for m in create_dummy_data(12):
        print(m)