import whois

def whois_lookup(domain_name):
    try:
        whois_info = whois.whois(domain_name)
        return whois_info
    except Exception as e:
        return f"Error: {str(e)}"

def print_whois_info(whois_info):
    if isinstance(whois_info, dict):
        print("\nWHOIS Information:")
        for key, value in whois_info.items():
            if isinstance(value, list):
                value = ", ".join(str(item) for item in value)
            print(f"{key.capitalize()}: {value}\n")
    else:
        print(whois_info)

def main():
    domain_name = input("Enter a domain name to perform a WHOIS lookup: ")
    result = whois_lookup(domain_name)
    print_whois_info(result)

if __name__ == "__main__":
    main()
