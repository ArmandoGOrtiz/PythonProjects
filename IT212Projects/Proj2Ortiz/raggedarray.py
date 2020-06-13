# Armando Oritz
# Project 2
# April - 24 - 2019

# Define method to read a ragged array
def read_ragged_array(the_filename):
  
    # Initialize ragged array
    ragged_array = ["Frame0"]

    # Open input file and read first line
    f = open(the_filename, "r")
    line = f.readline( )
  
    # Keep processing lines until end of file is reached.
    while line:
        fields = line.split(" ")
        row = [ ]
      
        # Append each field item to the row array
        for field in fields:
            row.append(int(field.strip( )))
      
        # When finished constructing row, append
        # to ragged_array.
        ragged_array.append(row)

        # Read next line
        line = f.readline( )
  
    # When finished reading file, return ragged array
    return ragged_array