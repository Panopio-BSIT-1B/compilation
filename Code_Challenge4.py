print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions for Your Recommendation")

# user inputs
Genre = input("What Genre Do You prefer? (romance, sports, action): ")
Duration = input("How long do you prefer? (short, medium, long): ")
Year_decade = input("In What Year Do you prefer? (2000s, 2010s, 2020s): ")

# Romance recommendations
if Genre == "romance":
    if Duration == "short":
        if Year_decade == "2000s":
            print("We Recommend You NANA")
        elif Year_decade == "2010s":
            print("We Recommend You HI SCORE GIRL")
        elif Year_decade == "2020s":
            print("We Recommend You A HOME FAR AWAY")
        else:
            print("INVALID decade")
    elif Duration == "medium":
        if Year_decade == "2000s":
            print("We Recommend You BECK")
        elif Year_decade == "2010s":
            print("We Recommend You HOUSE OF THE SUN")
        elif Year_decade == "2020s":
            print("We Recommend You SEASONS OF BLOSSOM")
        else:
            print("INVALID decade")
    elif Duration == "long":
        if Year_decade == "2000s":
            print("We Recommend You HONEY AND CLOVER")
        elif Year_decade == "2010s":
            print("We Recommend You KASE-SAN AND...")
        elif Year_decade == "2020s":
            print("We Recommend You UNTIL I MEET MY HUSBAND")
        else:
            print("INVALID decade")
    else:
        print("INVALID duration")

# Sports recommendations
elif Genre == "sports":
    if Duration == "short" and Year_decade == "2000s":
        print("We Recommend You: SLAM DUNK")
    elif Duration == "medium" and Year_decade == "2010s":
        print("We Recommend You: HAIKYUU!!")
    elif Duration == "long" and Year_decade == "2020s":
        print("We Recommend You: BLUE LOCK")
    else:
        print("No sports manga found for that choice.")

# Action recommendations
elif Genre == "action":
    if Duration == "short" and Year_decade == "2000s":
        print("We Recommend You: CLAYMORE")
    elif Duration == "medium" and Year_decade == "2010s":
        print("We Recommend You: MY HERO ACADEMIA")
    elif Duration == "long" and Year_decade == "2000s":
        print("We Recommend You: NARUTO")
    else:
        print("No action manga found for that choice.")

else:
    print("INVALID ")