weight = 4.8
flat_charge = 20.0
ground_shipping = flat_charge
drone_shipping = 0
# ground shipping
if (weight <= 2):
  ground_shipping += weight * 1.5
  print("Ground:", ground_shipping)
elif (weight <= 6):
  ground_shipping += weight * 3
  print("Ground:", ground_shipping)
elif (weight <=10 ):
  ground_shipping += weight * 4
  print("Ground:", ground_shipping)
elif (weight > 10):
  ground_shipping += weight * 4.75
  print("Ground:", ground_shipping)

premium_rate = 125

print("Premium:", premium_rate)

# drone shipping

if (weight <= 2):
  drone_shipping = weight * 4.5
  print("Drone:", drone_shipping)
elif (weight <= 6):
  drone_shipping = weight * 9
  print("Drone:", drone_shipping)
elif (weight <=10 ):
  drone_shipping = weight * 12
  print("Drone:", drone_shipping)
elif (weight > 10):
  drone_shipping = weight * 14.25
  print("Drone", drone_shipping)

if (ground_shipping < premium_rate and ground_shipping < drone_shipping):
  print("The cheapest shipping option is ground shipping.")
elif (premium_rate < ground_shipping and premium_rate < drone_shipping):
  print("The cheapest shipping option is premium shipping.")
elif (drone_shipping < ground_shipping and drone_shipping < premium_rate):
  print("The cheapest shipping option is drone shipping")
