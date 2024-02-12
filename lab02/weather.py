#What is the difference between the highest and the lowest temperature values predicted for the 10 day forecast?
import statistics

def main():
    dif = 78 - 50
    
    tem = [68, 71, 67, 65, 61, 61, 61, 64, 68, 61]
    aveTem = statistics.mean(tem)
    highest = (79 - 32) * 5 / 9

    print ("Difference is " + str(dif))
    print ("AVerage tem at noon is " + str(aveTem))
    print ("To C: " + str(highest))

main()
 