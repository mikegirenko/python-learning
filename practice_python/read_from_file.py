"""

Given a .txt file that has a list of a bunch of names, count how many of each
name there are in the file, and print out the results to the screen. I have
a .txt file for you, if you want to use it!

Extra:
Instead of using the .txt file from above (or instead of, if you want the
challenge), take this .txt file, and count how many of each “category” of
each image there are. This text file is actually a list of files
corresponding to the SUN database scene recognition database, and lists the
file directory hierarchy for the images. Once you take a look at the first
line or two of the file, it will be clear which part represents the scene
category. To do this, you’re going to have to remember a bit about string
parsing in Python 3. I talked a little bit about it in this post.

"""

file_with_names = "names_list.txt"


def read_file(file_name):
    with open(file_name, 'r') as file_object:
        all_records = file_object.readlines()
    file_object.close()
    return all_records


print("Total number of names is", len(str(read_file(file_with_names))))


def count_unique_records():
    unique_records = set()
    all_records = read_file(file_with_names)
    for record in all_records:
        unique_records.add(record)
    return len(unique_records)


print("Number of unique names is", count_unique_records())


file_with_images = "images_list.txt"

print("Total number of images is", len(str(read_file(file_with_images))))


def count_unique_categories():
    just_categories = []
    all_images = read_file(file_with_images)
    for image in all_images:
        just_categories.append(image.split('/')[2])

    unique_categories = set()
    for item in just_categories:
        unique_categories.add(item)
    return len(unique_categories)


print("Number of unique categories is", count_unique_categories())
