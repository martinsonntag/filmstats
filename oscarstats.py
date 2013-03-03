import imdb

z = imdb.IMDb(accesSystem='http')

def get_no_oscars(id):
	t = z.get_movie_awards(id)
	t = t['data']
	if len(t.keys()) == 0:
		d = 0
	else:
		t = t['awards']
		d=0
		for s in range(len(t)):
			if t[s]['award'] == 'Oscar' and t[s]['result'] == 'Won' and t[s]['assigner'] == 'Academy Awards, USA' :
				d=d+1
	return d
