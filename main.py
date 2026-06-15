import requests

def get_company_info(company):
    url = f"https://query1.finance.yahoo.com/v1/finance/search?q={company}"

    try:
        response = requests.get(url)
        data = response.json()

        if "quotes" in data and len(data["quotes"]) > 0:
            result = data["quotes"][0]

            print("\n--- Company Information ---")
            print("Name:", result.get("shortname", "N/A"))
            print("Symbol:", result.get("symbol", "N/A"))
            print("Exchange:", result.get("exchange", "N/A"))
        else:
            print("No company information found.")

    except Exception as e:
        print("Error:", e)

def generate_report(company):
    report = f"""
Financial Research Report
========================

Company: {company}

This report was generated automatically by the
Autonomous Financial Research Agent.

Basic research completed successfully.
"""

    with open("report.txt", "w") as file:
        file.write(report)

    print("Report generated: report.txt")

def main():
    company = input("Enter company name: ")

    get_company_info(company)
    generate_report(company)

if __name__ == "__main__":
    main()