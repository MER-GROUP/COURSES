class Song:
	def __init__(self, artist, song):
		self.artist = artist
		self.song = song
		self.tags = []
		
	def add_tags(self, *args):
		self.tags.extend(args)
		
song1 = Song('Red', 'Alert')
song1.add_tags('Max', 'Payne')
print(song1.tags)

song2 = Song('Red222', 'Alert222')
song2.add_tags('Max222', 'Payne222')
print(song2.tags)