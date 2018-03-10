text = "X-DSPAM-Confidence:    0.8475";
index = text.find(":")
print(index)
piece = text[index+1:]
value = float(piece)
print(value)
