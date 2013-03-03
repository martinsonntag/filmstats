import imdb

z = imdb.IMDb(accesSystem='http')

def get_no_oscars(id):
	t = z.get_movie_awards(id)
	t = t['data']
	t = t['awards']
	d=0
	for s in range(len(t)):
		if t[s]['award'] == 'Oscar' and t[s]['result'] == 'Won':
			d=d+1
	return d
