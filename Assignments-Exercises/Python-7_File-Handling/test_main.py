#read file
try:
    with open("sample.txt", "r") as read_file:
        contents = read_file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print("Error: 'sample.txt' not found. Please make sure the file exists.")

#write file
new_content = "This is a new file, like New Year New Me XD"

try:
    with open("newfile.txt", "w") as write_file:
        write_file.write(new_content)
    print("\nNew file created with content:")
    print(new_content)
except IOError as e:
    print(f"Error writing to file: {e}")
    
#check file
with open('newfile.txt', 'r') as file:
    print("\nChecking file:")
    newfile_contents = file.read()
    print(newfile_contents)