'''Create the CSV file with the following
Doyle McCarty, 27
Jodi Mills, 25
Nicholas Rose, 32
Kian Goddard, 36
Zuha Hanania, 26'''

fileName = "csvChallenge.csv"
READ = "r"
WRITE = "w"

csvChallenge = open(fileName,WRITE)
csvChallenge.write("Doyle McCarty, 27\n")
csvChallenge.write("Jodi Mills, 25\n")
csvChallenge.write("Nicholas Rose, 32\n")
csvChallenge.write("Kian Goddard, 36\n")
csvChallenge.write("Zuha Hanania, 26")
csvChallenge.close()

print("The CSV file has been written successfully!")