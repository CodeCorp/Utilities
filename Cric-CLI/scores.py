import urllib2
import ast
import os
#from gi.repository import Notify
#Notify.init("CricScore")

def main():
	try:
		content = urllib2.urlopen("http://cricscore-api.appspot.com/csa").read()
		list=ast.literal_eval(content)
		scores={}

		for x in list:
			try:
				score = urllib2.urlopen("http://cricscore-api.appspot.com/csa?id="+str(x['id'])).read()
			except:
				print "Make sure you are connected to a working Internet connection."
			scorelist=ast.literal_eval(score)[0]
			x1=scorelist["si"]
			x2=scorelist["de"]
			scores[x1]=x2

		final=""
		for key in scores:
			final = final + key + " : \n" + str(scores[key]) + '\n\n\n'
		
		print final

		try:
			os.system('notify-send -t 10000 "CricScores" "' + final + '" ')
		except:
			print "Currently desktop notifications aren't available on your OS"

	except:
		print "Make sure you are connected to a working Internet connection."

if __name__ == '__main__':
	main()
