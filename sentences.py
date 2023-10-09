import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
    "bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
    "birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"
    """
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = [noun + "s" for noun in single_nouns]

    if quantity == 1:
        return random.choice(single_nouns)
    else:
        return random.choice(plural_nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
    "drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
    "drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
    "drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
    "will drink", "will eat", "will grow", "will laugh",
    "will think", "will run", "will sleep", "will talk",
    "will walk", "will write"
    """
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_verbs_singular = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_verbs_plural = [verb[:-1] for verb in present_verbs_singular]
    future_verbs = ["will " + verb for verb in past_verbs]

    if tense == "past":
        return random.choice(past_verbs)
    elif tense == "present" and quantity == 1:
        return random.choice(present_verbs_singular)
    elif tense == "present" and quantity != 1:
        return random.choice(present_verbs_plural)
    elif tense == "future":
        return random.choice(future_verbs)
    
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at", "before",
        "behind", "below", "beyond", "by", "despite", "except", "for", "from",
        "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past",
        "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase


def make_sentence(quantity, tense):
    """Build and return a sentence with four parts:
    a determiner, a noun, a verb, and a prepositional phrase.
    The grammatical quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.

    Parameter:
        quantity: an integer that determines if the
            determiner and noun should be single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a sentence.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    return sentence


def main():
    sentences = [
        make_sentence(1, "past"),
        make_sentence(1, "present"),
        make_sentence(1, "future"),
        make_sentence(2, "past"),
        make_sentence(2, "present"),
        make_sentence(2, "future"),
    ]

    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

if __name__ == "__main__":
    main()



