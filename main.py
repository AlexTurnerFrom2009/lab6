from encoder.py import encode
from decoder.py import decode

if __name__ == "__main__":
  expected_encode = "45678888"
  expected_decode = "33332295"

  assert(encode(12345555) == expected_encode, "Encoder error")
  assert(decode(00009962) == expected_decode, "Decoder error")