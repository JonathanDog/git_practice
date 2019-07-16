destinations = ["Paris, France" , 'Shanghai, China', "Los Angeles, USA", 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
	destination_index = destinations.index(destination)
	return destination_index

def get_traveler_location(traveler):
	traveler_destination = traveler[1]
	traveler_destination_index = get_destination_index(traveler_destination)
	return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

attractions = [[], [], [], [], []]



def add_attraction(destination,attraction):
	try: 
		destination_index = get_destination_index(destination)
		
	except SyntaxError:
		print("Destination doesn't exist")
		return
	attractions[destination_index].append(attraction)
	




add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


def find_attractions(destination, interests):
	destination_index = get_destination_index(destination)
	attractions_in_city = attractions[destination_index]
	attractions_with_interest = []
	for i in attractions_in_city:
		possible_attractions = i
		attraction_tags = i[1]
		
		for a in interests:
			
			if a in attraction_tags:
				attractions_with_interest.append(possible_attractions[0])
				
	return attractions_with_interest	


la_art = find_attractions("Los Angeles, USA",['art'])

print(la_art)

def get_attractions_for_traveler(traveler):
	traveler_destination = traveler[1]
	traveler_interests = traveler[2]   
	traveler_attractions = find_attractions(traveler_destination, traveler_interests)
	interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler[1] +": "
	for i in range(len(traveler_attractions)):
		interests_string += traveler_attractions[i]
	interests_string += "."
	return interests_string 

print (get_attractions_for_traveler(['Joe Savino', "Shanghai, China", ['garden']]))