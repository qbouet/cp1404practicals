total_price = 0
keep_asking = 1

while keep_asking == 1:
    number_of_items = int(input("Number of items: "))
    if number_of_items < 0:
        print("Invalid number of items!")
        keep_asking = 1
    else:
        keep_asking = 0

for i in range(0, number_of_items, 1):
    price_of_item = float(input("Price of item: "))
    total_price = total_price + price_of_item

print(f"Total price for {number_of_items} items is {total_price:.2f}")

# A more complex solution:
#
# total_price = 0
# is_valid_input = False
# while not is_valid_input:
#     try:
#         number_of_items = int(input("Number of items: "))
#         if number_of_items < 0:
#             print("Number of items must be >= 0")
#         else:
#             is_valid_input = True
#     except ValueError:
#         print("Invalid (not an integer)")
#
# for i in range(0, number_of_items, 1):
#     price_of_item = float(input("Price of item: "))
#     total_price = total_price + price_of_item
#
# print(f"Total price for {number_of_items} items is {total_price:.2f}")
