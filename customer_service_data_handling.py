#Task 1: Customer Service Ticket Tracker

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
ticket_number = 1

def open_ticket(name,issue):
   global ticket_number
   service_tickets[f'Ticket00{ticket_number}'] = {"Customer": name, "Issue": issue, "Status": "open"}
   ticket_number += 1
   print(f'Ticket for {name} succsefully opened.')

def update_ticket(name):
    for ticket, items in service_tickets.items():
        if items['Customer'] == name:
            found = True
            current_ticket = ticket
        else:
            found = False
    if found:
        option = input('''\n\t\tWhat would you like to update?
                       1. Update Issue
                       2. Update Status
                       3. Cancel''')
        if option == '1':
            issue = input("What would you like to make the new issue?")
            service_tickets[current_ticket]['Issue'] = issue
        elif option == '2':
            change = input(f'The status of this ticket is currently {service_tickets[current_ticket]['Status']}, would you like to change this? (y/n)')
            if change == 'y':
                if service_tickets[current_ticket]['Status'] == 'open':
                    service_tickets[current_ticket]['Status'] = 'closed'
                else:
                    service_tickets[current_ticket]['Status'] = 'open'
    else:
        print('Ticket not Found.')

def display_tickets(filter='none'):
    print('\nHere are all of the tickets:' if filter == 'none' else f'Here are all of the {filter} tickets:')
    for ticket, items in service_tickets.items():
        if items['Status'] == filter or filter == 'none':
            print(f'''\n\t\t{ticket}:
                Customer Name: {items['Customer']}
                Issue: {items['Issue']}
                {f'Status: {items['Status']}' if filter == 'none' else ''}''')

def main():
    while True:
        option = input('''\n\t\tWhat would you Like to do?
                    1. Open a ticket
                    2. Update a ticket
                    3. Display tickets\n''')
        if option == '1':
            name = input('What is the name of the customer?')
            issue = input(f"What is {name}'s issue?")
            open_ticket(name,issue)
        elif option == '2':
            name = input("Who's ticket are you trying to access?")
            update_ticket(name)
        elif option == '3':
            filter = input('''\n\t\tWould You like to Filter the tickets?
                           1. Filter by opened
                           2. Filtered by closed
                           3. Dont filter''')
            if filter == '1':
                display_tickets('open')
            elif filter == '2':
                display_tickets('closed')
            else:
                display_tickets()
            
        else:
            print('That is not a valid option, please try again.')


if __name__ == '__main__':
    main()