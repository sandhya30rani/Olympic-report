olympics_data = []
def add_record():
    print("Enter details for the new Olympic record:")
    olympic_name = input("Olympic Game: ")
    country = input("Country: ")
    year = int(input("Year: "))
    number_of_medals = int(input("Number of medals won: "))
    
    
    olympics_data.append({
        'olympic_name': olympic_name,
        'country': country,
        'year': year,
        'medals': []  
    })
    
    
    collect_medal_details(olympics_data[-1], number_of_medals)


def collect_medal_details(record_entry, number_of_medals):
    for i in range(number_of_medals):
        print(f"Enter details for Medal Record {i + 1}:")
        athlete = input("Athlete Name: ")
        event = input("Event Name: ")
        medal = input("Medal Type (Gold | Silver | Bronze): ")
        record_entry['medals'].append({
            'athlete': athlete,
            'event': event,
            'medal': medal
        })
        print("Record added successfully!\n")


def delete_record():
    if not olympics_data:
        print("No records available to delete.\n")
        return
    
    print("Select the record to delete:")
    for i in range(len(olympics_data)):
        record = olympics_data[i]
        print(f"{i + 1}. {record['olympic_name']} ({record['year']}) - {record['country']}")

    choice = int(input("Enter the record number to delete: "))
    if 1 <= choice <= len(olympics_data):
        removed = olympics_data.pop(choice - 1)
        print(f"Deleted record: {removed['olympic_name']} ({removed['year']})\n")
    else:
        print("Invalid choice. No record deleted.\n")
def view_all_records():
    print(f"{'Athlete':<20}{'Event':<20}{'Medal':<15}{'Year':<10}")
    print("-" * 65)
    for record in olympics_data:
        for medal in record['medals']:
            print(f"{medal['athlete']:<20}{medal['event']:<20}{medal['medal']:<15}{record['year']}")
def view_winners_names():
    if not olympics_data:
        print("No records available.\n")
        return
    
    print("List of all winners:")
    for record in olympics_data:
        for medal in record['medals']:
            print(medal['athlete'])

while True:
    print("Menu:")
    print("1. Add a New Record")
    print("2. Delete a Record")
    print("3. View All Records")
    print("4. View Last 5 Years Winners in a Game")
    print("5. Exit")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        add_record()
    elif choice == 2:
        delete_record()
    elif choice == 3:
        view_all_records()
        
        pass
    elif choice == 4:
        view_winners_names()
        pass
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
