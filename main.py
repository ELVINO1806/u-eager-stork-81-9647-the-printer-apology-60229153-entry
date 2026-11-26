
import os

TEXT = "I'm sorry. I only ever jam on the document you needed five minutes ago. It's a gift, really."

# The joke lands here: the printer owns up to jamming only the one document that actually mattered, five minutes before the deadline.
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
