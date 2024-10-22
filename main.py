from encoder import *

if __name__ == "__main__":
  expected_encode = "45678888"
  expected_decode = "12345555"

  assert encode("12345555") == expected_encode, "Encoder error"
  assert decode("45678888") == expected_decode, "Decoder error"
  