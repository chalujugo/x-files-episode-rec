import random
import time

def xfiles(filename, season):
    eps = []
    file = open("episodes/" + filename, "r")
    content = file.read()
    lines = content.split("\n")
    for i in range(len(lines)):
        ep = lines[i][lines[i].find('"')+1:lines[i].rfind('"')]
        eps.append(ep)
    return eps


def get_eps():
    one = xfiles("season1.txt", "Season 1")
    two = xfiles("season2.txt", "Season 2")
    three = xfiles("season3.txt", "Season 3")
    four = xfiles("season4.txt", "Season 4")
    five = xfiles("season5.txt", "Season 5")
    six = xfiles("season6.txt", "Season 6")
    seven = xfiles("season7.txt", "Season 7")
    episodes = {"Season 1":one,"Season 2": two, "Season 3": three, "Season 4": four, "Season 5": five, "Season 6": six, "Season 7": seven} 
    return episodes

def print_eps(season_number, episodes):
    season = "Season " + str(season_number)
    print()
    print(season.upper())
    for value in episodes[season]:
        print(value)
    print()
        
def choose_ep(episodes):
    all_eps = []
    eps = []
    for key in episodes:
        all_eps.append(episodes[key])
    for i in range(len(all_eps)):
        for j in range(len(all_eps)):
            eps.append(all_eps[i][j])
    episode_rec = random.choice(eps)
    print(episode_rec)

#========================#
# for MSR episodes
#========================#

def msr(filename,season):
    msr_eps = []
    file = open("episodes/" + filename, "r")
    content = file.read()
    lines = content.split("\n")
    for i in range(len(lines)-1):
        lines[i].split()
        if lines[i][:3] == "MSR":
            ep = lines[i][lines[i].find('"')+1:lines[i].rfind('"')]
            msr_eps.append(ep)
    return msr_eps

def is_msr():
    one = msr("season1.txt", "Season 1")
    two = msr("season2.txt", "Season 2")
    three = msr("season3.txt", "Season 3")
    four = msr("season4.txt", "Season 4")
    five = msr("season5.txt", "Season 5")
    six = msr("season6.txt", "Season 6")
    seven = msr("season7.txt", "Season 7")
    msr_episodes = {"Season 1":one,"Season 2": two, "Season 3": three, "Season 4": four, "Season 5": five, "Season 6": six, "Season 7": seven} 
    return msr_episodes

def print_msr(msr_episodes):
    for key in msr_episodes:
        print(key,": ")
        print("| ",end="")
        for item in msr_episodes[key]:
            print(item," | ", end="")
        print()
        print()

def get_random_msr(msr_episodes):
    all_msr = []
    final_msr_list = []
    for key in msr_episodes:
        all_msr.append(msr_episodes[key])
    for i in range(len(all_msr)):
        for j in range(len((all_msr)[i])):
            final_msr_list.append(all_msr[i][j])
    msr_recommendation = random.choice(final_msr_list)
    print(msr_recommendation)

#========================#
# for fun episodes
#========================#

def funny(filename, season):
    funny_eps = []
    file = open("episodes/" + filename, "r")
    content = file.read()
    lines = content.split("\n")
    for i in range(len(lines)-1):
        lines[i].split()
        if lines[i][4:9] == "FUNNY" or lines[i][:5] == "FUNNY":
            ep = lines[i][lines[i].find('"')+1:lines[i].rfind('"')]
            funny_eps.append(ep)
    return funny_eps    

def is_funny():
    one = funny("season1.txt", "Season 1")
    two = funny("season2.txt", "Season 2")
    three = funny("season3.txt", "Season 3")
    four = funny("season4.txt", "Season 4")
    five = funny("season5.txt", "Season 5")
    six = funny("season6.txt", "Season 6")
    seven = funny("season7.txt", "Season 7")
    funny_episodes = {"Season 1":one,"Season 2": two, "Season 3": three, "Season 4": four, "Season 5": five, "Season 6": six, "Season 7": seven} 
    return funny_episodes

def print_funny(funny_episodes):
    for key in funny_episodes:
        print(key,": ")
        for item in funny_episodes[key]:
            print(item)
        print()
    print()

def get_random_funny(funny_episodes):
    all_funny = []
    final_funny_list = []
    for key in funny_episodes:
        all_funny.append(funny_episodes[key])
    for i in range(len(all_funny)):
        for j in range(len((all_funny)[i])):
            final_funny_list.append(all_funny[i][j])
    funny_recommendation = random.choice(final_funny_list)
    print(funny_recommendation)

#========================#
# for mytharc episodes
#========================#

def mytharc(filename,season):
    myth_eps = []
    file = open("episodes/" + filename, "r")
    content = file.read()
    lines = content.split("\n")
    for i in range(len(lines)-1):
        if "double-dagger" in lines[i]:
            ep = lines[i][lines[i].find('"')+1:lines[i].rfind('"')]
            myth_eps.append(ep)
    return myth_eps

def is_myth():
    one = mytharc("season1.txt", "Season 1")
    two = mytharc("season2.txt", "Season 2")
    three = mytharc("season3.txt", "Season 3")
    four = mytharc("season4.txt", "Season 4")
    five = mytharc("season5.txt", "Season 5")
    six = mytharc("season6.txt", "Season 6")
    seven = mytharc("season7.txt", "Season 7")
    myth_episodes = {"Season 1":one,"Season 2": two, "Season 3": three, "Season 4": four, "Season 5": five, "Season 6": six, "Season 7": seven} 
    return myth_episodes

def print_myth(myth_episodes):
    for key in myth_episodes:
        print(key,": ")
        print("| ",end="")
        for item in myth_episodes[key]:
            print(item," | ", end="")
        print()
        print()

def get_random_mytharc(myth_episodes):
    all_myth = []
    final_mytharc_list = []
    for key in myth_episodes:
        all_myth.append(myth_episodes[key])
    for i in range(len(all_myth)):
        for j in range(len((all_myth)[i])):
            final_mytharc_list.append(all_myth[i][j])
    myth_recommendation = random.choice(final_mytharc_list)
    print(myth_recommendation)

def main():
    print(" ============================")
    print()
    print("   X FILES EPISODE SELECTOR  ")
    print()
    print(" ============================")
    print()
    episodes = get_eps()
    msr_episodes = is_msr()
    funny_episodes = is_funny()
    mytharc_episodes = is_myth()
    selection = 1
    while selection > -1:
        print("|  1. Print episodes")
        print("|  2. Suggest random episode")
        print("|  3. All MSR episodes")
        print("|  4. Suggest an MSR episode")
        print("|  5. Print all fun episodes")
        print("|  6. Suggest a fun episode")
        print("|  7. Print all mytharc episodes")
        print("|  8. Suggest a mytharc episode")
        print("|  0. Exit")
        print()
        selection = int(input(">>>>> Select one: "))
        if selection == 1:
            print()
            print("   ==============")
            print("    1. Season 1")
            print("    2. Season 2")
            print("    3. Season 3")
            print("    4. Season 4")
            print("    5. Season 5")
            print("    6. Season 6")
            print("    7. Season 7")
            print("   ===============")
            season = int(input("   Select a season: "))
            print_eps(season, episodes)
        elif selection == 2:
            print()
            print("Try watching:")
            choose_ep(episodes)
            print()
        elif selection == 3:
            print()
            print("ALL MSR EPISODES:")
            print_msr(msr_episodes)
            print()
        elif selection == 4:
            print()
            print("Try watching:")
            get_random_msr(msr_episodes)
            print()
        elif selection == 5:
            print()
            print("ALL FUN EPISODES:")
            print_funny(funny_episodes)
            print()
        elif selection == 6:
            print()
            print("Try watching:")
            get_random_funny(funny_episodes)
            print()
        elif selection == 7:
            print()
            print("ALL MYTHARC EPISODES:")
            print_myth(mytharc_episodes)
            print()
        elif selection == 8:
            print()
            print("Try watching:")
            get_random_mytharc(mytharc_episodes)
            print()
    
        elif selection == 0:
            print()
            print("THE TRUTH IS OUT THERE")
            print()
            time.sleep(1)
            exit()
        else:
            print("Please enter a valid number")
            selection = int(input(">>>>> Select one: "))

main()
    
