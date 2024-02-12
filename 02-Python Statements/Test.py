
st = 'Print only the words that start with s in this sentence'
words = st.split(" ")
for word in words:
    if word[0] == "s":
        print(word)


x = list(range(0, 11, 2))
#print(x)


y = [num for num in list(range(0, 51)) if num % 3 == 0]
#print(y)


st = "Print every word in this sentence that has an even number of letters"
words = st.split(" ")
for word in words:
    if len(word) % 2 == 0:
        print(f"{word} is even!")



x = list(range(0, 101))
for num in x:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)



st = "Create a list of the first letters of evey word in this string"
z = [word[0] for word in st.split(" ")]
print(z)
