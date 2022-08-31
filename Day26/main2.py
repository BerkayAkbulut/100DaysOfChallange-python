# LIST COMPREHENSION EXAMPLES #
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Coding Exercises No1
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)
# Coding Exercises No2
zero_with_no_remainder = [number for number in numbers if number % 2 == 0]
print(zero_with_no_remainder)
# Coding Exercises No3
with open(file="file1.txt", mode='r') as txt1:
    text1 = txt1.readlines()
    text1 = [int(number.strip()) for number in text1]
with open(file="file2.txt", mode='r') as txt2:
    text2 = txt2.readlines()
    text2 = [int(number.strip()) for number in text2]

same_values = [index for index in text1 if index in text2]
print(same_values)

# DICT COMPREHENSION EXAMPLES #
# Coding Exercises No1:
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

new_dic = {word: len(word) for word in sentence.split()}
print(new_dic)
# Coding Exercises No2:
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp_c * 9 / 5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
