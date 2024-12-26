#Very early and simple prototype for calculating fuel requirements for Fleet Carrier Travel. Assumes 500ly jumps every time (although you can change jumpRange if you wish to give yourself a bit more leeway), except for the last one which is set to whatever distance is left.
#Could probably be optimised and better coded, just the result of about a hour of quick googling.

#define parameters
distance = 46000 #In LY, distance to target
dryMass = 0 #Mass taken by modules, commodities, ships and outfitting.
startingFuel = 26000 #Combined mass of the internal fuel tank and the tritium reserves in the cargo hold.
jumpRange = 488 #put it slightly below 500 to account for the fact jumps will rarely be the full 500ly. should give a slightly more realistic estimate

# Calculate the number of full jumps, and distance of clearing jump
fullJumpsCount = distance // jumpRange
clearingJumpDistance = distance % jumpRange

# Define value storage
remainingFuel = startingFuel
jumpCount = 0

# Iterate over the full chunks
for i in range(fullJumpsCount):
    fuelConsumption = round(5 + (jumpRange * (dryMass + remainingFuel + 25000)) / 200000)
    remainingFuel -= fuelConsumption
    jumpCount += 1
    print(f"Jump {jumpCount}: {fuelConsumption}t consumed, {remainingFuel}t remaining.")

# If there is any remaining distance, handle it in one last iteration
if clearingJumpDistance > 0:
    fuelConsumption = round(5 + (clearingJumpDistance * (dryMass + remainingFuel + 25000)) / 200000)
    remainingFuel -= fuelConsumption
    jumpCount += 1
    print(f"Jump {jumpCount}: {fuelConsumption}t consumed, {remainingFuel}t remaining.")

print(f"Calculation Results : ",startingFuel-remainingFuel,f"t consumed across {jumpCount} Jumps,",remainingFuel,"t left in carrier reserves.")
