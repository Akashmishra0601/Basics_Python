while True:

    print("\n youtube manager: ")
    print("1. List a faverite videos ")
    print("2 . ADd a youtube video")
    print("3. Upadte a youtube vedio")
    print("4 . delete a youtube vedio")
    print("5 . exit the app")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            list_all_videos(videos)
        case '2':
            add_videos(videos)