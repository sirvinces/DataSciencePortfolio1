# My first Python project in GitHub 
def greet_user(): 
  name = input("Enter your name: ").strip().title()
    
    focus = input("What is your concentration (e.g., Public Health, Analytics)? ")
    
    print(f"\nHello, {name}! Welcome to Data Science.")
    print(f"Using data science to improve {focus} is an excellent path.")
    
    tool = input("\nWhich do you prefer to use: Python or R? ").strip().upper()
    
    if tool == "R":
        print("Ah, you must enjoy making visualizations with ggplot2!")
    elif tool == "PYTHON":
        print("Python is fantastic for everything from pandas to building software.")
    else:
        print(f"{tool.title()} is a great tool to have in your skillset too!")
  
if __name__ == "__main__": 
  greet_user()
