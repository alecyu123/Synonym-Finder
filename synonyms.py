### Part 1

# Subpart A

def cosine_similarity(vec1, vec2):
  udotv = 0
  sum1 = 0
  sum2 = 0
  for k in vec1:
    if k in vec2:
      udotv += vec1[k] * vec2[k]
    sum1 += vec1[k]**2
  for k in vec2:
    sum2 += vec2[k]**2

  return udotv / (sum1 * sum2)**(1 / 2)


# Subpart B
def build_semantic_descriptors(sentences):
  d = {}
  n = 1
  sentences1 = sentences[:]
  while n == 1:
    if sentences == []:
      break
    for word in sentences[0]:
      if word not in d:
        d[word] = {}
    sentences.pop(0)

  while n == 1:
    if sentences1 == []:
      break
    for word in set(sentences1[0]):
      for word2 in set(sentences1[0]):
        if word2 != word:
          if word2 not in d[word]:
            d[word][word2] = 1
          else:
            d[word][word2] += 1
    sentences1.pop(0)

  return d

# Subpart C
def build_semantic_descriptors_from_files(filenames):
  big_ls = []
  for name in filenames:
    f = open(name, "r", encoding="latin1")
    str = f.read().lower()
    str = str.replace('!', '.')
    str = str.replace('?', '.')
    ls = str.split('.')

    for i in range(len(ls)):
      subls = ls[i].replace('-', ' ')
      subls = subls.replace('--', ' ')
      subls = subls.replace(';', ' ')
      subls = subls.replace(';', ' ')
      subls = subls.replace(',', ' ')
      subls = subls.split()
      ls[i] = subls

    big_ls += ls

  dict = build_semantic_descriptors(big_ls)

  return dict

# Subpart D
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
  max = -2
  if word not in semantic_descriptors:
    return choices[0]
  for choice in choices:
    if choice in semantic_descriptors:
      v1 = semantic_descriptors[word]
      v2 = semantic_descriptors[choice]
      similarity = similarity_fn(v1, v2)
    else:
      similarity = -1

    if similarity > max:
      best_choice = choice
      max = similarity

  return best_choice

# semantic_descriptor = build_semantic_descriptors_from_files(["War and Peace.txt", "Swann's Way.txt"])

# Subpart E

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
  score = 0
  f = open(filename, 'r')
  ls = f.readlines()
  for i in range(len(ls)):
    line = ls[i].replace('\n', '')
    line = line.split()
    print([line[2:]])
    word = most_similar_word(line[0], line[2:], semantic_descriptors, similarity_fn)
    if word == line[1]:
      score += 1

  return score*100/len(ls)

# print(run_similarity_test('test.txt', semantic_descriptor, cosine_similarity))















