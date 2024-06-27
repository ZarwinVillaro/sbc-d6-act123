def main():
    n = int(input("Enter a number: "))
    num_list = list(range(1, n+1))
    print(f"list: {num_list}")
    
    while num_list:
        choice = input("Enter 'NAA' or 'WALA': ").upper()
        
        if choice == 'NAA' and num_list:
            num_list.pop(0)
        elif choice == 'WALA' and num_list:
            num_list.pop()
        else:
            print("Invalid choice or list is empty. Exiting.")
            break
        
        print(f"Updated list: {num_list}")
    
    print("List is empty. Exiting.")

if __name__ == "__main__":
    main()
