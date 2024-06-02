import random
import datetime
import argparse

def generate_random_phrases(num_phrases):
    adjectives = ["quick", "lazy", "happy", "sad", "bright", "dark", "calm", "angry", "big", "small"]
    nouns = ["fox", "dog", "cat", "tree", "sky", "river", "mountain", "star", "car", "house"]
    verbs = ["jumps", "runs", "flies", "dives", "sings", "cries", "laughs", "sleeps", "eats", "drinks"]

    phrases = []

    for _ in range(num_phrases):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        phrase = f"{adjective} {noun} {verb}"
        phrases.append(phrase)
    
    return phrases

def save_phrases_to_file(phrases, filename):
    with open(filename, 'w') as file:
        for phrase in phrases:
            file.write(phrase + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save random 3-word phrases.")
    parser.add_argument('-f', '--file', type=str, help="The file name to save the phrases. If not provided, the file name will be based on the current date and time.")
    args = parser.parse_args()

    # Set the random seed to the current time in milliseconds
    current_time = datetime.datetime.now().timestamp()
    seed = int(current_time * 1000)
    random.seed(seed)

    num_phrases = 100
    random_phrases = generate_random_phrases(num_phrases)
    
    if args.file:
        filename = args.file
    else:
        now = datetime.datetime.now()
        filename = now.strftime("phrases_%Y%m%d_%H%M%S.txt")
    
    save_phrases_to_file(random_phrases, filename)
    print(f"Saved {num_phrases} phrases to {filename}")


