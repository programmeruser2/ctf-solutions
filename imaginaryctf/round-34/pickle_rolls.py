d = bytes.fromhex('80047d284b2a4b754b124b374b264b674b154b5f4b284b724b1e4b5f4b054b704b194b334b224b5f4b074b634b2c4b7d4b114b5f4b134b684b104b6d4b0f4b304b0a4b334b244b344b204b724b254b6e4b1a4b724b234b644b1b4b6e636f730a72656d6f76650a635f5f6d61696e5f5f0a5f5f66696c655f5f0a8552304b084b6b4b034b664b0b4b354b0e4b724b1c4b334b214b334b294b304b044b7b4b184b374b144b334b2b4b354b1f4b344b0d4b664b174b6e4b014b634b004b694b0c4b5f4b274b334b1d4b374b024b744b064b314b094b314b164b317530636261736536340a6236346465636f64650a566148523063484d364c7939336433637565573931644856695a53356a62323076643246305932672f646a316b55586330647a6c585a31686a55513d3d0a85522e')
with open('pickled', 'wb') as f:
    f.write(d)
import os
os.system('fickling --trace pickled')
# Popped {42: 117, 18: 55, 38: 103, 21: 95, 40: 114, 30: 95, 5: 112, 25: 51, 34: 95, 7: 99, 44: 125, 17: 95, 19: 104, 16: 109, 15: 48, 10: 51, 36: 52, 32: 114, 37: 110, 26: 114, 35: 100, 27: 110, 8: 107, 3: 102, 11: 53, 14: 114, 28: 51, 33: 51, 41: 48, 4: 123, 24: 55, 20: 51, 43: 53, 31: 52, 13: 102, 23: 110, 1: 99, 0: 105, 12: 95, 39: 51, 29: 55, 2: 116, 6: 49, 9: 49, 22: 49}
dictionary = {42: 117, 18: 55, 38: 103, 21: 95, 40: 114, 30: 95, 5: 112, 25: 51, 34: 95, 7: 99, 44: 125, 17: 95, 19: 104, 16: 109, 15: 48, 10: 51, 36: 52, 32: 114, 37: 110, 26: 114, 35: 100, 27: 110, 8: 107, 3: 102, 11: 53, 14: 114, 28: 51, 33: 51, 41: 48, 4: 123, 24: 55, 20: 51, 43: 53, 31: 52, 13: 102, 23: 110, 1: 99, 0: 105, 12: 95, 39: 51, 29: 55, 2: 116, 6: 49, 9: 49, 22: 49}
s = bytearray(max(dictionary.keys())+1)
for key, val in dictionary.items():
    s[key] = val
print(s)
