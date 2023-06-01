def cfg_website_nav():
    #creating base url
    base_url = "https://codefirstgirls.com/"
    #adding current url to be able to modify base url
    current_url = base_url

    #introducing while True loop, later add options to exit it
    while True:
        #adding inputs from assessement example
        print("You are currently on the URL", current_url)
        print("Where are you clicking?")

        #creating logic for suggested options
        if current_url == base_url:
            options = ["Courses", "Opportunities"]
        elif current_url == base_url + "courses":
            options = ["CFGDegree", "Back"]
        elif current_url == base_url + "opportunities":
            options = ["CFGDegree", "Back"]
        elif current_url == base_url + "courses/cfgdegree":
            options = ["Back"]
        else:
            options = ["Back"]

        print("Options:", ', '.join(options))

        #adding choice input options and making it case insensitive
        choice = input().lower()

        if choice == "courses" and current_url == base_url:
            current_url = base_url + "courses"
        elif choice == "cfgdegree" and current_url == base_url + "courses":
            current_url = base_url + "courses/cfgdegree"
        elif choice == "back":
            if current_url == base_url:
                print("Cannot go back further. Choose one of the suggested options or enter: exit.")
            elif current_url == base_url + "courses/cfgdegree":
                current_url = base_url + "courses"
            else:
                current_url = base_url
        elif choice == "opportunities" and current_url == base_url:
            current_url = base_url + "opportunities"
        elif choice == "exit":
            print("Exiting program.")
            break
        else:
            print("Please choose one of the suggested options.")


# run the program
cfg_website_nav()


"""Task 3. B: Time complexity in this case would be o(1) - the logic is limited and does not depend on the size of the
input, so time complexity will remain constant.
Space complexity in this case would be 0(1) as well as the space used by program remains constant regardless of the
number of times user chooses their options, the amount of memory used doesn't depend on the input size, the program does
 not create additional data structures or variables."""
