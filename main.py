import re
from expand_corpus import expand_corpus


class RegexNER:
    def __init__(self, patterns):
        # Compile the regular expressions
        self.regex_patterns = {name: re.compile(
            pattern, re.IGNORECASE) for name, pattern in patterns.items()}

    def extract_matches(self, text):
        # Search for matches and their indices for all patterns
        matches_dict = {name: [(match.group(), match.start(), match.end()) for match in re.finditer(pattern, text)]
                        for name, pattern in self.regex_patterns.items()}
        return matches_dict


# List of words for affirmatives and negatives
AFFERMATIVE_WORDS = ['yes', 'without fail', 'surely', "that's right", 'quite so', 'right-o chief', 'you got it chief', 'unwaveringly', 'you got it lieutenant', 'without a doubt', 'undisputedly', 'you got that right', 'for sure', 'yeah sure', 'without hesitation', 'great', 'you got it boss', 'beyond the shadow of a doubt', 'in the affirmative', 'just so', 'I agree', 'as you say', 'you got that straight', 'hell yes', 'fine by me', 'beyond a doubt', 'I concur', 'no problem', 'hell yeah', 'you got it commander', 'indubitably', 'undoubtedly', 'quite right', 'by your leave', 'decidedly', 'roger', 'yep', 'forsooth', 'oh yes', 'irrefutably', 'you got it major', 'aye aye sir', 'clearly', 'indisputably', 'right as a trivet', 'of course, sir', 'manifestly', 'unequivocally', 'for real', 'agreed upon', 'totally', 'inarguably', 'sure enough', 'you got it sergeant', 'without qualification', "you're right", 'right-o', 'affirmative action', 'sure thing', 'absolutely', 'yeah buddy', 'no objections', 'unswervingly', 'undividedly', 'positive', 'emphatically', 'yup', 'without doubt', 'right you are', 'totally agree', 'right as rain', 'all right', 'got it', 'aye', 'indeed', 'certainly',
                     'you bet', 'affirmative captain', 'fine', 'you got it', 'it is so', 'all righty', 'by all means', 'sure as shooting', 'unarguably', 'yeah', 'very well', 'absotively', 'plainly', 'yeah right', 'without question', 'most certainly', 'uh-huh', 'you got it captain', 'right as ninepence', 'unreservedly', 'fair enough', 'correct', 'you said it', 'definitely', 'positively', 'aye aye', 'precisely', 'beyond question', 'sure', 'without a doubt in my mind', 'agreed', 'absurdly', 'without any shadow of a doubt', 'unambiguously', 'yessir', 'you got it officer', 'for certain', 'ok', 'righty-ho', 'right on', 'you betcha', 'absolutely right', 'unmistakably', 'very true', 'most assuredly', 'indeed so', 'aye aye captain', 'unquestionably', 'unquestioningly', 'of course', 'good', 'yes', 'damn straight', 'right you are, sir', 'okay', 'without dispute', 'undeniably', 'right', 'exactly', 'conclusively', 'you got it colonel', 'affirmative', 'no doubt', 'without any doubt whatsoever', 'exactly so', 'without reservation', 'damn right', 'fine with me', 'without a shadow of a doubt', 'it is agreed', 'exactly right', 'yessiree', 'you got it general', 'absolutely positively', 'affirmative sir']


NEGATIVE_WORDS = ['dissent', 'not in a million years', 'object', 'nay', 'revoke', 'noway Jose', 'deny', 'not in a thousand years', 'not on your life', 'dissuade', 'shut out', 'not for a thousand dollars', 'gainsay', 'not in the least', 'negative', 'denied', 'not in a month of Sundays', 'not in any way', 'certainly not', 'curb', 'never in a month of Sundays', 'declined', 'nope', 'disallow', 'counter', 'not at all', 'withdraw', 'no sir', 'not', 'dismiss', 'obstruct', 'never on your bet', 'never on your nellie', 'not possible', 'invalidate', 'interdict', 'not for all the rice in China', 'repudiate', 'never on your pinta', 'forbid', 'nullify', 'never', 'disaffirm', 'debunk', 'no sire', 'defy', 'disagree', 'impede', 'not on your pinta', 'not on your watch', 'rule out', "no ma'am", 'none', 'no siree Bob', 'no', 'withhold', 'deter', 'never in a thousand years', 'inhibit', 'negate', 'not in this lifetime', 'not for all the money',
                  'not on your tintype', 'not on your bet', 'absolutely not', 'nah', 'never on your tintype', 'not really', 'never on your life', 'block', 'under no circumstances', 'not on your vida', 'controvert', 'turn down', 'say no', 'abstain', 'disapprove', 'not a chance', 'discourage', 'not likely', 'by no means', 'stave off', 'not by any means', 'rebuff', 'no way Jose', 'not for anything', 'definitely not', 'disclaim', 'not a bit', 'prohibit', 'oppose', 'refused', 'not for a billion dollars', 'exclude', 'not for all the gold in Fort Knox', 'never on your vida', 'contravene', 'not for all the money in the world', 'avoid', 'no siree', 'never on your watch', 'not for all the tea in China', 'prevent', 'no way', 'not in this world', 'antagonize', 'not on your nellie', 'not for love or money', 'not on your nelly', 'contradict', 'never in a million years', 'veto', 'reject', 'rebut', 'not for a million dollars', 'not for the world']


CUSTUM_WORDS_AND_PHRASES = {
    "PHRASE_IF": ["if", "when", "in case", "provided that", "assuming"],
    "PHRASE_SUDDEN": ["sudden", "suddenly", "suddenly_you", "abrupt", "unexpected", "immediate"],
    "PHRASE_NEXT": ["next", "then", "afterward", "subsequently", "following", "consequently"],
    "PHRASE_OFTEN": ["often", "frequently", "regularly", "repeatedly", "commonly", "habitually"],
    "PHRASE_SOMETIMES": ["sometimes", "occasionally", "at_times", "from_time_to_time", "intermittently"],
    "PHRASE_NEVER": ["never", "not", "no", "absolutely_not", "under_no_circumstances", "in_no_way"],
}


# Expand corpus
CUSTUM_WORDS_AND_PHRASES = expand_corpus(CUSTUM_WORDS_AND_PHRASES)
print(CUSTUM_WORDS_AND_PHRASES)

# Patterns dictionary
patterns = {
    "POSITIVE": r'\b(?:' + '|'.join(AFFERMATIVE_WORDS) + r')\b',
    "NEGATIVE": r'\b(?:' + '|'.join(NEGATIVE_WORDS) + r')\b',
    "DAYS": r'\b(?:([0-9]|1\d|2[0-9]|3[0-1])?(?:st|nd|rd|th)?\s*)?(mon(?:day)?|tue(?:s(?:day)?)?|wed(?:nesday)?|thu(?:rs(?:day)?)?|fri(?:day)?|sat(?:urday)?|sun(?:day)?)\b(?:\s*([0-9]|1\d|2[0-9]|3[0-1])(?:st|nd|rd|th)?)?',
    "MONTH": r'\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\b',
    "YEAR": r'\b(?:19[4-9]\d|20[0-4]\d|2050)\b',
}

for key, value in CUSTUM_WORDS_AND_PHRASES.items():
    patterns[key] = r'\b(?:' + '|'.join(value) + r')\b'


regex_ner = RegexNER(patterns)
text_example = "The team was enthusiastic about 2024 suddenly you  jan the new 2 project in monday 5th  and responded with  a resounding 'yes' when asked if they were ready to take on the challenge. Their leader, affirming their commitment, said, 'Absolutely, we are prepared to give it our best.' However, when presented with an alternative approach, some team members expressed hesitation, stating, 'No, we're not convinced that this is the right direction.' Despite the initial negativity, the team ultimately reached a consensus, agreeing to move forward with the original plan. In the end, their positive attitude prevailed, and they approached the project with a can-do spirit, proving that even in the face of initial doubts, a determined and affirmative mindset can lead to success."

# Extract matches for yes and no patterns
result = regex_ner.extract_matches(text_example)

# Print the results
for pattern_name, matches in result.items():
    print(f"Matches for '{pattern_name}': {matches}")
