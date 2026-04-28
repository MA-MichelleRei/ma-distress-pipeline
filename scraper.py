import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_ma_business(company_name):
    print(f"--- Searching MA Records for: {company_name} ---")
    
    # This is the 'Search' URL for the MA Secretary of State
    search_url = "https://corp.sec.state.ma.us/corpweb/CorpSearch/CorpSearch.aspx"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        # We start a 'Session' to keep our Human Mask active
        session = requests.Session()
        response = session.get(search_url, headers=headers)
        
        if response.status_code == 200:
            print("✅ Ready to Search.")
            
            # For now, we will simulate finding results to keep it simple
            # Later, we will teach it to read the actual HTML table
            results = [
                {"Name": company_name.upper(), "Status": "Inactive", "Type": "LLC", "Priority": 85},
                {"Name": f"{company_name.upper()} HOLDINGS", "Status": "Active", "Type": "Corp", "Priority": 20}
            ]
            
            df = pd.DataFrame(results)
            print("\nFound these records:")
            print(df)
            
            # Save these results to your computer
            df.to_csv("search_results.csv", index=False)
            print("\n💾 Results saved to search_results.csv! Check the sidebar.")
            
        else:
            print(f"❌ Could not reach search page. Status: {response.status_code}")

    except Exception as e:
        print(f"❌ Error during search: {e}")


if __name__ == "__main__":
    # You can change this name to any business you want to check!
    search_ma_business("Red Apple")
