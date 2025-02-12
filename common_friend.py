def print_friends(dictionary):
    for name, friends in dictionary.items():
        print(f"{name}'s friends: ", end="")  
        for friend in friends:  
            print(friend, end=" ")  
        print()  

def find_common_friends(dictionary, person1, person2):
    friends1 = set(dictionary.get(person1, []))  # Convert lists to sets
    friends2 = set(dictionary.get(person2, []))
    
    common_friends = friends1.intersection(friends2)  # Find intersection
    
    if common_friends:
        print(f"Common friends between {person1} and {person2}: {', '.join(common_friends)}")
    else:
        print(f"No common friends between {person1} and {person2}.")

friends_dict = {
    "Rahul": ["Nahid", "Fatima", "Mahmud"],
    "Nahid": ["Rahul", "Fatima", "Mehrin"],
    "Sabiha": ["Ishtiaq", "Nasima", "Alina"]
}

print_friends(friends_dict)


find_common_friends(friends_dict, "Rahul", "Nahid")
