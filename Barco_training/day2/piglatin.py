import sys

def to_piglatin(w, add_hyphen=False):

    has_point = False
    if w[-1] == ".":
        w = w[:-1]
        has_point = True

    vowel_or_silent = ["a", "e", "i", "o", "u"]
    if w[0].lower() in vowel_or_silent:
        if add_hyphen:
            result = w + "-" + "ay"
        else:
            result = w + "ay"
    else:
        consonant_cluster = w[0]
        i = 1
        while w[i] not in vowel_or_silent:
            consonant_cluster += w[i]
            i += 1
        if add_hyphen:
            result = w[i:] + "-" + consonant_cluster + "ay"
        else:
            result = w[i:] + consonant_cluster + "ay"

    if has_point:
        result += "."

    return result

def from_piglatin(w):
    parts = w.split("-")
    return parts[1][:-2] + parts[0]

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "ERROR: You should specify an input and output file!"
        exit(-1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    f_input = open(inputfile)
    f_output = open(outputfile, "w")

    for line in f_input:
        piglatin_line = ""
        for word in line.split():
            piglatin_line += to_piglatin(word, True) + " "
        piglatin_line += "\n"
        f_output.write(piglatin_line)

    f_output.close()
    f_input.close()
