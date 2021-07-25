#Import required libraries
import random

def main():

    #Set goat numbers that are already claimed
    blacklist = [85, 54, 87, 69, 97, 80, 88, 63, 73, 67, 79, 81, 82, 49, 77, 99, 92, 93]

    #Set list of winners' ETH addresses
    winners = [ 
    '0x1Fdf397dd1E6596cED2f8E630cE222cBa9e5eE1f', 
    '0x91D586EA567DDC69EB90d0b4203C865Ddf278ADF', 
    '0x41604b59B6e4a21cD1863E1969F330177a217AFe',
    '0x8205eCc26495Ff55e1D6D84F59bd82C2dddd646D',
    '0x63be4b068aab6a114bf52ef4cec18a90ce9dca60', 
    '0x1a049909125C3665dbb635B0C7B299A66C356DEc', 
    '0x99a8f1682ca7d1ca2674be8218c2054095270684', 
    '0x0Bc6bCdda2356b42fFD79bB9914f3aF5d1aad07e', 
    '0x86f5badc9fB2Db49303D69aD0358b467cFd393E0', 
    '0xFE274ff2846a414e690606c2ed2CCC4Ad6bB9C53', 
    '0xE5b510bCEd75D90470AE44B098E195a42ed2a508', 
    '0x64905298c0e49751231fb9576903936744061e9c', 
    '0xa30eb1520cfa84f31f2021621d5ae27857d5bbf6', 
    '0x41bf572ad11733ce1e0aa146535b2b4509a14081']

    newnumbers = [] #Set list of numbers chosen

    for winner in winners:
      while True:
        num = random.randint(50, 99) #Generate random number from 50 to 99
        if num not in newnumbers and num not in blacklist: #Check if number is a duplicate and if it is in the blacklist
          print(f'{winner}: {num}') #Print the winners' ETH addresses and goat numbers to console
          newnumbers.append(num) #Add number to chosen numbers list
          break #Break loop

if __name__ == '__main__':
    main()
