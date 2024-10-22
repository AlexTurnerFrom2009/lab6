# Wade Rogers

def encode(password):
  encoded = ""
  for digit in password:
    encoded += str(int(digit)+3)[-1]
  return encoded

