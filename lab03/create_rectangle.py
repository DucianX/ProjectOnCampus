import sys

def main(width, length):
    for i in range(1, length + 1):
      print('*' * width)
    
if __name__ == "__main__":
   # Check if there is enough commmand-line arguments
   if len(sys.argv) != 3:
      print("Usage: python3 script.py <width> <length>")
   else:
      # Get width and length from command-line arguments
      width = int(sys.argv[1])
      length = int(sys.argv[2])
      main(width, length)
