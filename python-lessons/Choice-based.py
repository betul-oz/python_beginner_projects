import sys
import time

def slowtext(text, delay= 0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def main():
    slowtext("Welcome! Agent, Choose your code name?")
    agent_name = input("your code name (quick): ")

    slowtext(f"{agent_name}, are you ready to take on your first solo mission as a secret agent? (yes/no)")
    response = input().lower()
    if response == "yes":
        slowtext(f"Colonel Bruce has escaped. Your mission is to capture him alive. Good luck, Agent {agent_name}.")
    elif response == "no":
        slowtext(f"Mission aborted. The world is counting on you, Agent {agent_name}. Are you sure you want to abort? (yes/no)")
        response_abort = input().lower()
        if response_abort == "yes":
            slowtext("Mission aborted. You lost the opportunity of your life...")
        else:
            slowtext(f"Good choice, Agent {agent_name} . Your mission is to capture him alive. Good luck!")
    else:
        slowtext("Invalid response. Please enter 'yes' or 'no'.")

main() 

def Plan1():
    slowtext("Inform the teams and take precautions.")
    time.sleep(2)
    slowtext("Collaborate with intelligence agencies to determine Bruce's possible location. Begin the information gathering and tracking process.")
    time.sleep(2)

def Plan2():
    slowtext("Contact your old friends and find out where Bruce is hiding using your special connections.")
    time.sleep(2)
    slowtext("Investigate secret locations, but you must avoid enemy agents.")
    time.sleep(2)

def Plan3():
    slowtext("You may waste time doing something. You may not be able to fully pay attention.")
    time.sleep(2)
    slowtext("But this plan involves more risks. If you don't catch Bruce you're fired")
    time.sleep(2)

while True:
    slowtext("\nOptions:")
    slowtext("Plan 1: Create a Crisis Desk")
    slowtext("Plan 2: Find out where Bruce is from Old Friends")
    slowtext("Plan 3: Be lazy")

    choice = input("Make your choice (Plan1-Plan2-Plan3): ")

    if choice == "Plan1":
        Plan1()
    elif choice == "Plan2":
        Plan2()
    elif choice == "Plan3":
        Plan3()
    else:
        slowtext("Invalid response. Please enter 'Plan1' , 'Plan2' or 'Plan3'.")    
        break
    

slowtext("Sending the report to the higher authorities...")

slowtext("The End")


#  i prepared this story by using Chatgpt3.5 inspired by this website 
# (https://www.turkhackteam.org/konular/bat-programlama-ile-text-tabanli-oyun-yapimi.623358/) 
