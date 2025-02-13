def print_friends(dictionary):
    for name, friends in dictionary.items():
        print(f"{name}'s friends: ", end="")  
        for friend in friends:  
            print(friend, end=" ") 
        print()

friends_dict = {
    "Rahul": ["Nahid", "Fatima", "Mahmud"],
    "Nahid": ["Rahul", "Fatima", "Mehrin"],
    "Sabiha": ["Ishtiaq", "Nasima", "Alina"]
}
print_friends(friends_dict)
