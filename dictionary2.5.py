movies_2022 = {
    "RRR": ["Ram Charan", "Jr NTR", "Alia Bhatt"],
    "KGF Chapter 2": ["Yash", "Sanjay Dutt", "Raveena Tandon"],
    "Brahmastra": ["Ranbir Kapoor", "Alia Bhatt", "Amitabh Bachchan"],
    "The Kashmir Files": ["Mithun Chakraborty", "Anupam Kher", "Darshan Kumaar"]
}
movies_2023 = {
    "Pathaan": ["Shah Rukh Khan", "Deepika Padukone", "John Abraham"],
    "Jawan": ["Shah Rukh Khan", "Nayanthara", "Vijay Sethupathi"],
    "Gadar 2": ["Sunny Deol", "Ameesha Patel", "Utkarsh Sharma"],
    "Oppenheimer": ["Cillian Murphy", "Emily Blunt", "Matt Damon"]
}
movies_2024 = {
    "Kalki 2898 AD": ["Prabhas", "Deepika Padukone", "Amitabh Bachchan"],
    "Fighter": ["Hrithik Roshan", "Deepika Padukone", "Anil Kapoor"],
    "Dune Part Two": ["Timothée Chalamet", "Zendaya", "Rebecca Ferguson"],
    "Pushpa 2": ["Allu Arjun", "Rashmika Mandanna", "Fahadh Faasil"]
}
movies_2025 = {
    "Avatar 3": ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver"],
    "Tiger vs Pathaan": ["Salman Khan", "Shah Rukh Khan"],
    "War 2": ["Hrithik Roshan", "Jr NTR"],
    "Mission Impossible 8": ["Tom Cruise", "Hayley Atwell"]
}
# big dictionary
all_movies = {
    2022: movies_2022,
    2023: movies_2023,
    2024: movies_2024,
    2025: movies_2025
}

print(all_movies[2024]["Pushpa 2"]) ##['Allu Arjun', 'Rashmika Mandanna', 'Fahadh Faasil']

# Count total number of movies in all years combined.
count=0
for year in all_movies:
    count += len(all_movies[year])

print("Total number of movies:", count)  ##Total number of movies: 16

#movies with Shah Rukh Khan
count =0
for name,cast in all_movies.items():
    if "Shah Rukh Khan" in cast:
        print("movies with Shah Rukh Khan: ",cast)
        count =count+1

print(f"total movies with Shah Rukh Khan is :{count}")

# check if movie exists
movie_name = "RRR"
found = False

for year in all_movies:
    if movie_name in all_movies[year]:
        print(movie_name, "found in year", year)
        found = True

if not found:
    print("Movie not found")     #RRR found in year 2022

# keys
print(all_movies.keys())   #dict_keys([2022, 2023, 2024, 2025])

# values
for movie_names in all_movies.values():
    print(movie_names)