from .data import (ikinyarwanda, ibihekane,ibyungo, patterns)
import re
def tokenize(word):
  tokens = []
  tokens = re.compile("\s|a|u|i|e|u|o|â|ê|î|ô|û|[0-9]|[-!$%^&*()_+|~=`\{\}\[\]:\";'<>?,.\/]").split(word)
  for token in patterns:
    if token in word:
      tokens.append(token)
  return [token.strip() for token in tokens if token.strip()]

def detector(syllable):
  if syllable in ikinyarwanda : 
    return True
  return False

def isKinyarwanda(word):
  # print(ikinyarwanda)
  consonants = tokenize(str(word.lower()))
  count = 0.0;
  total = 0.0;
  for consonant in consonants:
    if len(consonant.strip()) > 1 and consonant.strip() not in ibihekane and consonant.strip() not in ibyungo:
      return False
    if len(consonant.strip()) <= 1:
      total += 1
      if detector(consonant.strip()):
        count += 1
  return count == total
