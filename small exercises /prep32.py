def get_common_movies(movies_list):
    result = movies_list[0]
    for movies in movies_list:
        result = result.intersection(movies)
    return result