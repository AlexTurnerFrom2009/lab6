# Wade Rogers

def encode(password1):
  encoded = ""
  for digit in password1:
    encoded += str(int(digit)+3)[-1]
  return encoded

