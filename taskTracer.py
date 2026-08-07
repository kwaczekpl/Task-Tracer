import sys

def main():
    # Check if arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python program.py <name>")
        sys.exit(1)
    
    # Get the first argument
    name = sys.argv[1]
    print(f"Hello, {name}!")
    
    # Print all arguments
    print(f"Arguments: {sys.argv}")

if __name__ == "__main__":
    main()

