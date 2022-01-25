punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(x):
    x = x.lower()
    new_str = ''
    for i in x:
        if i in punctuation_chars:
            continue
        new_str += i
    return new_str


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(word):
    count = 0
    word = strip_punctuation(word)
    word = word.lower().split()
    for item in word:
        if item in positive_words:
            count = count + 1
    return count


negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(word):
    count = 0
    word = strip_punctuation(word)
    word = word.lower().split()
    for item in word:
        if item in negative_words:
            count = count + 1
    return count


outfile = open('resulting_data.csv', 'w')

outfile.write('Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score')
outfile.write('\n')

file_ref = open('project_twitter_data.csv', 'r')
lines = file_ref.readlines()[1:]

for line in lines:
    positive_score = get_pos(line)  # using our pre-defined function
    negative_score = get_neg(line)
    net_score = positive_score - negative_score
    my_line = line.split(",")
    # print(my_line)
    retweets = int(my_line[1])
    n_reply = int(my_line[2])
    file_line = "{},{},{},{},{}".format(retweets, n_reply, positive_score, negative_score, net_score)
    outfile.write(file_line)
    outfile.write("\n")
outfile.close()