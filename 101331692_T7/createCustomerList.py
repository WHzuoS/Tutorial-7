import displayCustomer

def createRecord():
    customerInfo = []
   
    name = input("Please enter the full name of the customer: ")
    customerInfo.append(name)
    
    status = input("Please enter the membership status of the customer (G,S,B): ")
    customerInfo.append(status.upper())
    
    order_cost = float(input("Please enter the original cost of the order: "))
    customerInfo.append(order_cost)
    
    return customerInfo

def main():
    customersList = []
    num_info = int(input("Please quantify the amount of customer records which will be recorded: "))
    
    for i in range(num_info):
        customersList.append(createRecord())
    
    print('\n')
    
    displayCustomer.printList(customersList)

if __name__ == "__main__":
    main()