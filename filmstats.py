import imdb
import oscarstats
from pylab import *
import re
import sys
import numpy

z= imdb.IMDb(accesSystem='http')

run_controller =  sys.argv[1]
if run_controller == 'get_data':
	b = zeros((250, 3))
	movie_list = z.get_top250_movies()
	for i in range(len(movie_list)):
		print 'Nummer in der BestenListe: ' + str(i+1)
		b[i-1, 0] = i
		current_movie_name = movie_list[i]
		print 'Filmname: ' +  str(current_movie_name)
		current_movie_id = movie_list[i].movieID
		current_movie = z.get_movie(current_movie_id)
		laufzeit = current_movie['runtimes']
		laufzeit = laufzeit[0]
		laufzeit = re.findall(r'\d+', laufzeit)
		laufzeit = laufzeit[0]
		b[i-1, 1] = laufzeit
		print 'Die Laufzeit betraegt: ' + laufzeit + ' Minuten'
		current_no_of_oscars = oscarstats.get_no_oscars(current_movie_id)	
		print 'Anzahl der Oscars: ' +  str(current_no_of_oscars)
		b[i-1, 2] = current_no_of_oscars
		savetxt("results.csv", b, delimiter=",")
		####Plotting####


		figure()
    		plot(b[:,1], b[:,2], 'o' )
    		xlabel('Movie runtime [min]')
    		ylabel('Number of Oscars')
    		grid(True)
    		legend(['Number of Oscars'], 'upper right')
		savefig('results_overview_runtime_preview.png', dpi=(800/8))

if run_controller == 'post':
	resultsMatrix = loadtxt('results.csv', delimiter=',',  skiprows=0)
	figure()
    	plot(resultsMatrix[:,1], resultsMatrix[:,2], 'o' )
    	xlabel('Movie runtime [min]')
    	ylabel('Number of Oscars')
    	grid(True)
    	legend(['Number of Oscars'], 'upper right')
	savefig('results_overview.png', dpi=(800/8))
	show()

else:
	print 'run option are get_data, postprocess, ...'
