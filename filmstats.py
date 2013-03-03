import imdb
import oscarstats
from pylab import *
import re
import sys
import numpy
#kommentar von alex
#und kommentar von Martin
z= imdb.IMDb(accesSystem='http')

run_controller =  sys.argv[1]
if run_controller == 'get_data':
	b = zeros((250, 4))
	movie_list = z.get_top250_movies()
	for i in range(len(movie_list)):
		print 'Nummer in der BestenListe: ' + str(i+1)
		b[i-1, 0] = i
		current_movie_name = movie_list[i]
		print 'Filmname: ' +  str(current_movie_name)
		current_movie_id = movie_list[i].movieID
		rating = oscarstats.get_rating(current_movie_id)
		print rating
		b[i-1, 1] = rating
		current_movie = z.get_movie(current_movie_id)
		laufzeit = current_movie['runtimes']
		laufzeit = laufzeit[0]
		laufzeit = re.findall(r'\d+', laufzeit)
		laufzeit = laufzeit[0]
		b[i-1,2] = laufzeit
		print 'Die Laufzeit betraegt: ' + laufzeit + ' Minuten'
		current_no_of_oscars = oscarstats.get_no_oscars(current_movie_id)	
		print 'Anzahl der Oscars: ' +  str(current_no_of_oscars)
		b[i-1, 3] = current_no_of_oscars
		savetxt("results.csv", b, delimiter=",")
		
		####Plotting for debbuging####
		figure()
		
		subplot(121, title = 'Number of Oscars over runtime')
    		plot(b[:,2], b[:,3], 'o' )
    		xlabel('Movie runtime [min]')
    		ylabel('Number of Oscars')
    		grid(True)
    		legend(['Number of Oscars'], 'upper right')
		
		subplot(122, title = 'Rating over runtime')
    		plot(b[:,2], b[:,1], 'o' )
    		xlabel('Movie runtime [min]')
    		ylabel('IMDb user rating')
    		grid(True)
    		legend(['IMDb user rating'], 'upper right')
		savefig('results_overview_runtime_preview.png', dpi=(800/8))

if run_controller == 'post':
	resultsMatrix = loadtxt('results.csv', delimiter=',',  skiprows=0)
	figure()
	subplot(121, title = 'Number of Oscars over runtime')
    	plot(b[:,2], b[:,3], 'o' )
    	xlabel('Movie runtime [min]')
    	ylabel('Number of Oscars')
    	grid(True)
    	legend(['Number of Oscars'], 'upper right')
		
	subplot(122, title = 'Rating over runtime')
    	plot(b[:,2], b[:,1], 'o' )
    	xlabel('Movie runtime [min]')
    	ylabel('IMDb user rating')
    	grid(True)
    	legend(['IMDb user rating'], 'upper right')
	savefig('results_overview.png', dpi=(800/8))
	show()

else:
	print 'run option are get_data, postprocess, ...'
