def read_and_modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            content = file.read()
            print("Original content of the file:")
            print(content)
        
       
        modified_content = content.upper()  
      
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError as e:
        print(f"Error: An IO error occurred. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the input and output file names
input_filename = input("Enter the name of the input file: ")
output_filename = input("Enter the name of the output file: ")

# Call the function
read_and_modify_file(input_filename, output_filename)
