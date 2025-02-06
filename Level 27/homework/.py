# ფუნქცია: რაოდენობის დათვლა
# შექმენი ფუნქცია count_items(item_list, item), რომელიც მიიღებს ორ პარამეტრს:
# item_list - ელემენტების სია.
# item - ელემენტი, რომლის დათვლაც გსურს სიაში.
# ფუნქციამ უნდა დააბრუნოს, რამდენჯერ გვხვდება ეს ელემენტი სიაში.

# def count_items(item_list, item):
#     sum = 0
#     for i in item_list:
#         if i == item:
#             sum += 1
#     return sum
# print(count_items([1,2,3,4,1,1,5,12,2,1,4],1 ))



#2
# ფუნქცია: ჯამის გამოთვლა
# შექმენი ფუნქცია sum_of_list(num_list), რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სიაში არსებული ყველა რიცხვის ჯამს.
# ფუნქცია უნდა გამოიყენოს for ციკლი.

# def sum_of_list(num_list):
#     sum = 0
#     for i in num_list:
#         sum += i
#     return sum
# print(sum_of_list([1,2,3,4,5]))




#3
# ფუნქცია: საშუალო მნიშვნელობის გამოთვლა
# შექმენი ფუნქცია average_of_list(num_list), რომელიც იღებს რიცხვების სიას და აბრუნებს ამ რიცხვების საშუალო მნიშვნელობას.
# გამოიყენე სიის ჯამის გამოთვლა და ელემენტების რაოდენობის გაყოფა.

# def average_of_list(num_list):
#     sum_sum = sum(num_list)
#     length = len(num_list)
#     if sum_sum == 0:
#         return None
#     average = sum_sum / length
#     return average
# print(average_of_list([1,2,3,4,5,6,7,8,9,12]))



#5
# ფუნქცია: სიის გადაბრუნება
# შექმენი ფუნქცია reverse_list(items), რომელიც დააბრუნებს გადაბრუნებულ სიას (სიის ბოლო ელემენტი პირველზე იქნება, პირველი კი ბოლო).
# def reverse_list(items):
#     reversed_list = items[::-1]
#     return reversed_list
# print(reverse_list([1,2,3,4,5]))