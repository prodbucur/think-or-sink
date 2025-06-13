questions = [
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Lisbon", "option_3"],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "option_2"],
    ["Who wrote 'Hamlet'?", "Charles Dickens", "Mark Twain", "William Shakespeare", "Leo Tolstoy", "option_3"],
    ["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", "option_2"],
    ["What gas do plants absorb from the atmosphere?", "Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen", "option_3"],
    ["Who painted the Mona Lisa?", "Pablo Picasso", "Vincent Van Gogh", "Leonardo da Vinci", "Claude Monet", "option_3"],
    ["Which country hosted the 2016 Summer Olympics?", "China", "Brazil", "UK", "Russia", "option_2"],
    ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Quartz", "option_3"],
    ["How many continents are there?", "5", "6", "7", "8", "option_3"],
    ["Which element has the chemical symbol 'O'?", "Oxygen", "Gold", "Osmium", "Oxide", "option_1"],
    ["Which language has the most native speakers worldwide?", "English", "Mandarin Chinese", "Spanish", "Hindi", "option_2"],
    ["What is the square root of 144?", "10", "11", "12", "13", "option_3"]
]

reward = 0

for question in questions:
    print(question[0])
    print("1:", question[1])
    print("2:", question[2])
    print("3:", question[3])
    print("4:", question[4])
    
    answer = input("Please select the correct option (1-4): ")
    
    if answer == question[-1].split('_')[1]:
        print("Correct!\n")
        reward += 1
    else:
        print(f"Wrong! The correct answer is option {question[-1].split('_')[1]}: {question[int(question[-1].split('_')[1])]}\n")
        break

earned= str(reward * 100000000)
j=3
for i in range(int(len(earned)/3)):
    if len(earned)<=j:
        break
    earned = earned[:-j]+","+earned[-j:]
    j+= 4

print(f"Gamer Over! Your total reward is {earned} points.\n")
print("Thank you for playing!")