import time
import webbrowser

total_breaks = 3
break_count = 0

while (break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("http://google.com")
	break_count = break_count + 1