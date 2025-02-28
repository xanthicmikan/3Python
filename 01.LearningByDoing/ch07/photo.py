import photo_module as m

while True:
    photo_name = input("Please input the name of the image you want to download: ")

    download_num = int(input("Input picture numbers: "))

    photo_list = m.get_photolist(photo_name, download_num)

    if photo_list == None:
        print("Find no picture, please change keywords.")
    else:
        if len(photo_list) < download_num:
            print("The only relevant images found are:", len(photo_list))
        else:
            print("Get all pictures's link")
        break

folder_name = m.create_folder(photo_name)

print("Start...")

m.get_photobythread(folder_name, photo_name, photo_list)

print("\nDone")
