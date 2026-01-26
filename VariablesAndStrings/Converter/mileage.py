print("How many kilometer have you cycled today: ")
kms = input()
#input takes the input as the string values, need to be a float

miles = float(kms)/1.60934
miles = round(miles,2)
print(f"Your {kms}km ride was {miles}mi")
