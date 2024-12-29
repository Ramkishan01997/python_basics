  # Define the file name and content
file_name = "example.txt"
content = "vbljbbi jlbljbkjl bjbjlhvb jlhv vj ooijjall pythons programs"

# Create and write to the file
with open(file_name, "w") as file:
    file.write(content)

print(f"File '{file_name}' has been created and the text has been written to it.")

with open(file_name,"r")as file:
   print(f"reading file '{file_name}'",file.read())
file.close