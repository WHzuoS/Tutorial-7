def printIndividualList(customer):
    for i in range(len(customer)):
        
        if i == 1:
            if (customer[i] == 'G'):
                print(f"{customer[i-1]} has a gold discount status of 10%, order of ${customer[i+1]}",
                    f"is discounted ${round(customer[i+1]*0.10,2)} for a final total of {round(customer[i+1]*0.9,2)}")
                print('\n')
            
            elif (customer[i] == 'S'):
                print(f"{customer[i-1]} has a silver discount status of 5%, order of ${customer[i+1]}",
                    f"is discounted ${round(customer[i+1]*0.05,2)} for a final total of {round(customer[i+1]*0.95,2)}")
                print('\n')
            
            else:
                print(f"{customer[i-1]} has a bronze discount status of 2%, order of ${customer[i+1]}",
                    f"is discounted ${round(customer[i+1]*0.02,2)} for a final total of {round(customer[i+1]*0.98,2)}")
                print('\n')
                

def printList(customerList):
    for customer in customerList:
        printIndividualList(customer)
        
def main():
    customerRecords = [["Sean Benjamin", "B", 30.22], ["Yanan Mao", "G", 40.22], 
                       ["Charlie Brown", "S", 22.30], ["Snoopy Dog", "G", 69.33], 
                       ["Woodstock Bird", "S", 25.00]]
    print('\n')
    printList(customerRecords)
    
if __name__ == "__main__":
    main()