
"""
    Checks as defined in article: https://www.polygon.com/2018/8/7/17660344/animal-crossing-letter-system-game-design-explained
    Takes a string and returns the calculated scoring
    >100 Is considered to be good
    <50 Is considered to be bad
"""
import logging
from trigrams import generate_trigrams

logging.basicConfig(level="DEBUG")
logger = logging.getLogger("ACNL")



def score_message(message: str) -> int:
    score = 0
    score += checkPunctuation(message)
    score += check_trigrams(message)
    score += check_capital(message)
    score += check_for_repetition(message)
    score += check_space_ratio(message)
    score += check_length(message)
    score += check_spaces(message)
    logger.info("Final score: %s " % score)
    return score

# A
def checkPunctuation(message: str) -> int:
    score = 0
    # Check for use of punctuation
    # Check for capitals
    logger.info("Checking punctuation for string: %s" % message)
    # Find all punctuation indices
    punc_ids = [id for id, punc in enumerate(message) if not (punc.isalnum() or punc == " ")]
    logger.info("Found punctuation at indices: %s" % punc_ids)
    for id in punc_ids:
        # Ignore final character
        if id < len(message)-1:
            # Check the 3 characters after the punctuation for a capital
            found_cap = False
            for i in range(3):
                if len(message) <= id+i:
                    # End of string
                    break
                else:
                    if message[id+i].isupper():
                        found_cap = True
                        break;
            logger.info("%s capital after char %s at index %s" % ("Found" if found_cap else "Did not find", message[id], id))
            if found_cap:
                score += 10
            else:
                score -= 10
            logger.info("New score: %s" % score)
    # Check final character for punctuation
    if len(message) > 0 and message[-1:] in ["?", ".", "!"]:
        logger.info("Final character is punctuation")
        score += 20

    logger.info("Returned score: %s" % score)
    return score
    

#B
def check_trigrams(message: str) -> int:
    logger.info("Checking for words starting with trigrams")
    trigrams = generate_trigrams()
    words = message.split(" ")
    logger.info("Words: %s" % words)
    tri_words = [word for word in words if len(word) >= 3 and word[:3] in trigrams]
    logger.info("Tri-words: %s" % tri_words)
    score = len(tri_words) * 3
    logger.info("Returned score: %s" % score)
    return score

#C
def check_capital(message: str) -> int:
    logger.info("Checking first letter for capital")
    score = 0
    for id, char in enumerate(message):
        if char != " ":
            logger.info("First non-space character is %s at index %s. It %s uppercase" % (char, id, "is" if char.isupper() else "is not" ))
            if char.isupper():
                score += 20
            else:
                score -= 10
            break
    logger.info("Returned score: %s" % score)
    return score

#D
def check_for_repetition(message: str) -> int:
    logger.info("Checking for repeated characters")
    # Check for 3 or more consecutive letters
    for id, char in enumerate(message):
        # Only check alphabetic chars
        if char.isalpha():
            # Go go beyond end of string
            if id < len(message)-2:
                # If pattern found, subtract 50 points and end check
                if char == message[id+1] and char == message[id+2]:
                    logger.info("Found repeated character %s at index %s-%s" % (char, id, id+2))
                    logger.info("Returned score: -50")
                    return -50
    logger.info("Score not affected")
    return 0

#E
def check_space_ratio(message: str) -> int:
    logger.info("Checking ratio of characters to spaces")
    score = 0
    # Count spaces
    space_count = message.count(" ")
    logger.info("Space count: %s/%s" % (space_count, len(message)))
    
    ratio = space_count*100 / len(message)
    logger.info("Space ratio: %s%%" % ratio)
    if ratio < 20 or space_count == len(message):
        score -= 20
    else:
        score += 20
    logger.info("Returned score: %s" % score)
    return score

#F
def check_length(message: str) -> int:
    logger.info("Checking for blocks of 75 chars without punctuation")
    score = 0
    if len(message) > 75:
        # Get all indices of punctuation
        punc_ids = [id for id, punc in enumerate(message) if not (punc.isalnum() or punc == " ")]
        logger.info("Found punctuation at indices: %s" % punc_ids)
        if len(punc_ids) == 0:
            score -= 150
            logger.info("No punctuation present.  New score: %s" % score)
        for id, punc_id in enumerate(punc_ids):
            # Only check if there is another to compare
            if id < len(punc_ids)-1:
                # Subtract next index from current and check for a gap of 75+
                if punc_ids[id+1] - punc_id >= 75:
                    logger.info("No punctuation between chars %s and %s. \"%s\"" % (punc_id, punc_ids[id+1], message[punc_id:punc_ids[id+1]]))
                    score -= 150
                    break
            elif len(message) - punc_id >= 75:
                logger.info("No punctuation between chars %s and %s. \"%s\"" % (punc_id, len(message), message[punc_id:]))
                score -= 150
    else:
        logger.info("Message is < 75 chars long. No change to score")
    logger.info("Returned score: %s" % score)
    return score

#G
def check_spaces(message: str) -> int:
    logger.info("Checking for presence of space in each 32 char block")
    score = 0
    id = 0
    while id < len(message):
        space_count = 0
        if id+31 < len(message):
            # 32 char block within the string
            space_count = message[id:id+32].count(" ")
            logger.info("Found %s space in substring %s" % (space_count, message[id:id+32]))
            id +=32
        else:
            # <32 char block at the end of string
            space_count = message[id:].count(" ")
            logger.info("Found %s space in substring %s" % (space_count, message[id:]))
            id = len(message)
        if space_count <= 0:
            score -= 20
            logger.info("No spaces. New score: %s" % score)
        else:
            score += 20
            logger.info("Space found. New score: %s" % score)
    logger.info("Returned score: %s" % score)
    return score

# score = score_message("rEEEEEEEEEEEEEEEEEEEEEEEEEE"\
#                       "EEEEEEEEEEEEEEEEEEEEEEEEEEE"\
#                       "EEEEEEEEEEEEEEEEEEEEEEEEEEE"\
#                       "EEEEEEEEEEEEEEEEEEEEEEEEEEE"\
#                       "EEEEEEEEEEEEEEEEEEEEEEEEEEE"\
#                       "EEEEEEEEEEEEEEEEEEEEEEEEEEE")

# score = score_message("A.A.A.A.A.A.A.A.A.A.A.A.A.A.A"\
#                       ". A.A.A.A.A.A.A.A.A.A.A.A.A.A."\
#                       " A. A.A.A.A.A.A.A.A.A.A.A.A.A."\
#                       "A.A. A.A.A.A.A.A.A.A.A.A.A.A. "\
#                       "A.A.A. A.A.A.A.A.A.A.A.A.A.A. "\
#                       "A.A.A.A. A.A.A.A.A.A.A.A.A.A. ")
# logger.info("Final score: %s" % score)