import webbrowser
import time

break_count = 0

name = input("What's yo name? ")
study_time = int(input("How many minutes per study session? "))*60
break_time = int(input("How many minutes per break? "))*60
total_breaks = int(input("How many rounds of study? "))

print("Sup, " + name + ", your study session started at " + time.ctime() +
      "\n\n Whale??\n\n ¯\_(ツ)_/¯ GET THE BUTTS TO IT THEN")

while(break_count < total_breaks):
    time.sleep(study_time)
    webbrowser.open("https://www.youtube.com/watch?v=rRzxEiBLQCA")
    print("Break #"+ str(break_count+1) + " happened at " + time.ctime())
    time.sleep(break_time)


    print("Time to get back to work " + name + "!!!!")
    break_count += 1
    
print("Study session concluded! Congrats on getting through your "
      + str(total_breaks) + " breaks <3")

