import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 print [word for word in words if re.search(regex, word)]

# Answers
# All words that contain a 'v'
get_matching_words(r"v")
# All words that contain a double-"s"
get_matching_words(r"ss")
# All words that end with an "e"
get_matching_words(r"e$")
# All words that contain a b, any character, then another b
get_matching_words(r"b.b")
# All words that contain a b, any number of characters, then another b
get_matching_words(r"b.+b")
# All words that include all five vowels in order
get_matching_words(r"a.*e.*i.*o.*u")
# All words that only use the letters in "regular expression"
get_matching_words(r"\A[aegilnoprsu]*\Z")
# All words that contain a double letter
get_matching_words(r"(.)\1")
