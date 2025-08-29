def file_processor():
    """
    A program that reads a file, modifies its content, and writes to a new file
    with comprehensive error handling.
    """
    print("📁 FILE PROCESSOR PROGRAM")
    print("=" * 50)
    
    while True:
        try:
            # Get input filename from user
            input_filename = input("\nEnter the filename to read (or 'quit' to exit): ").strip()
            
            if input_filename.lower() == 'quit':
                print("👋 Goodbye!")
                break
            
            if not input_filename:
                print("❌ Please enter a filename!")
                continue
            
            # Read the file
            print(f"\n📖 Attempting to read: {input_filename}")
            with open(input_filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            print("✅ File read successfully!")
            
            # Process the content (modify as needed)
            modified_content = process_content(content)
            
            # Get output filename
            output_filename = get_output_filename(input_filename)
            
            # Write to new file
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            
            print(f"✅ Modified content written to: {output_filename}")
            print(f"📊 Original file size: {len(content)} characters")
            print(f"📊 New file size: {len(modified_content)} characters")
            
            # Ask if user wants to see a preview
            show_preview(content, modified_content)
            
        except FileNotFoundError:
            print(f"❌ Error: The file '{input_filename}' was not found.")
            print("   Please check the filename and try again.")
        except PermissionError:
            print(f"❌ Error: Permission denied to read '{input_filename}'.")
            print("   Check file permissions or try a different file.")
        except UnicodeDecodeError:
            print(f"❌ Error: Could not decode the file '{input_filename}'.")
            print("   The file may be binary or use a different encoding.")
        except IsADirectoryError:
            print(f"❌ Error: '{input_filename}' is a directory, not a file.")
        except OSError as e:
            print(f"❌ Operating System Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
        finally:
            print("-" * 50)

def process_content(content):
    """
    Modify the file content according to specific rules.
    Customize this function based on your needs.
    """
    # Example modifications:
    modified = content
    
    # 1. Convert to uppercase
    modified = modified.upper()
    
    # 2. Add line numbers
    lines = modified.split('\n')
    numbered_lines = [f"{i+1:3d}: {line}" for i, line in enumerate(lines)]
    modified = '\n'.join(numbered_lines)
    
    # 3. Add header and footer
    header = "=" * 50 + "\nMODIFIED FILE CONTENT\n" + "=" * 50 + "\n\n"
    footer = "\n\n" + "=" * 50 + "\nEND OF FILE\n" + "=" * 50
    
    return header + modified + footer

def get_output_filename(input_filename):
    """
    Generate output filename based on input filename
    """
    if '.' in input_filename:
        name, ext = input_filename.rsplit('.', 1)
        return f"{name}_modified.{ext}"
    else:
        return f"{input_filename}_modified.txt"

def show_preview(original, modified):
    """
    Show a preview of the changes
    """
    preview = input("\nWould you like to see a preview? (yes/no): ").lower()
    if preview in ['yes', 'y']:
        print("\n" + "🔍 PREVIEW - ORIGINAL (first 3 lines):")
        print("-" * 30)
        for line in original.split('\n')[:3]:
            print(line[:100] + "..." if len(line) > 100 else line)
        
        print("\n🔍 PREVIEW - MODIFIED (first 3 lines):")
        print("-" * 30)
        for line in modified.split('\n')[:3]:
            print(line[:100] + "..." if len(line) > 100 else line)

# Run the program
if __name__ == "__main__":
    file_processor()
