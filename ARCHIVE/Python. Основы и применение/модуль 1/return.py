def closest_mod_5(x):
    while True:
	    if 0 == x % 5:
	        return x
	    x += 1
    return "I don't know :("
    
print(closest_mod_5(811))