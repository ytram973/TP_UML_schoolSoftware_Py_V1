

class Address:

	def __init__(self, road: str, city: str, zip_code: int):
		self.road = road
		self.city = city
		self.zip_code = zip_code

	def __str__(self):
		return f"{self.road} {self.city} {self.zip_code}"

# mon_adresse = Address("123 Rue de la Paix", "Paris", 75000)
#
# print(mon_adresse)
