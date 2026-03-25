from loader import load_file
from splitter import splitter
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def display_chunks(chunks):
    print("-"*60)
    for i, chunk in enumerate(chunks):
        print(f"\n ------ Chunk {i+1} ------")
        print(f"Characters: {len(chunk.page_content)}")
        print(f"Content: {chunk.page_content}")
        print(f"Metadata: {chunk.metadata}")
        print("-"*60)

def main():
    print("="*60)
    print("       Welcome to the Document Loader and Splitter!")
    print("="*60)

    # Get the file path from the user
    file_path = input("Please enter the path to your document (PDF or TXT): ").strip()

    # Load the document
    documents = load_file(file_path)

    # Show raw document information
    print("\nRaw Document Information:")
    for i, doc in enumerate(documents):
        print(f"\nDocument {i+1}:")
        print(f"Characters: {len(doc.page_content)}")
        print(f"Content: {doc.page_content[:200]}...")  # Show first 200 chars
        print(f"Metadata: {doc.metadata}")
    
    # Split the document into chunks
    print("\n ----- Splitting the document into chunks -----")
    chunk_size = int(input("Enter chunk size (default 1000): ") or 1000)
    chunk_overlap = int(input("Enter chunk overlap (default 200): ") or 200)
    chunks = splitter(documents, chunk_size, chunk_overlap)

    # Display the chunks
    show = input("\nDo you want to display the chunks? (y/n): ").strip().lower()
    if show == 'y':
        display_chunks(chunks)
    else:
        # Just show the first and last chunk
        print("\nFirst Chunk:")
        print(f"Content: {chunks[0].page_content[:200]}")

        print("\nLast Chunk:")
        print(f"Content: {chunks[-1].page_content[:200]}")
    
if __name__ == "__main__":
    main()
