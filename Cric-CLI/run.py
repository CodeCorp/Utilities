import time, scores, os
while True:
	time.sleep(30)
	os.system('cls' if os.name == 'nt' else 'clear')
	scores.main()
	print ("Press Ctrl+C to terminate the script, else it'll refresh in 30 seconds with the updated scores")
