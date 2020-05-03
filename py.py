import scholarly

author = 'Steven A. Cholewiak'
print("Search author: ", author)
result = next(scholarly.search_author(author)).fill()
print(result)
print()


# Print the titles of the author's publications
print([pub.bib['title'] for pub in result.publications])

# Take a closer look at the first publication
pub = result.publications[0].fill()
print(pub)

# Which papers cited that publication?
print([citation.bib['title'] for citation in pub.get_citedby()])

keyword = 'Haptics'
print("Search keyword: ", keyword)
print(next(scholarly.search_keyword(keyword)))
print()


search = 'Perception of physical stability and center of mass of 3D objects'
print("Search: ", search)
search_query = scholarly.search_pubs_query(search)
print(next(search_query))
print()
