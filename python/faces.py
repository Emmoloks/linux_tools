def convert(string):
    return string.replace(":)"," 🙂 ").replace(":(", "🙁")

def main():
    prompt = input("speak your emotion:")
    print (convert(prompt))

if __name__ == "__main__":
    main()
