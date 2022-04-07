key_loc="chair"
locations=["bed","table","kitchen","chair","second floor"]
for loc in locations:
    if key_loc == loc:
        print("Key is found at",loc)
        break
    else:
        print("Key is not found at", loc)