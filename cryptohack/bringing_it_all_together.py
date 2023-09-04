from structure_of_aes import bytes2matrix, matrix2bytes
from round_keys import add_round_key
from diffusion_through_permutation import inv_shift_rows, inv_mix_columns
from confusion_through_substitution import sub_bytes, s_box, inv_s_box

N_ROUNDS = 10

key        = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'



def expand_key(master_key):
    """
    Expands and returns a list of key matrices for the given master_key.
    """

    # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    # Initialize round keys with raw key material.
    key_columns = bytes2matrix(master_key)
    iteration_size = len(master_key) // 4

    # Each iteration has exactly as many columns as the key material.
    i = 1
    while len(key_columns) < (N_ROUNDS + 1) * 4:
        # Copy previous word.
        word = list(key_columns[-1])

        # Perform schedule_core once every "row".
        if len(key_columns) % iteration_size == 0:
            # Circular shift.
            word.append(word.pop(0))
            # Map to S-BOX.
            word = [s_box[b] for b in word]
            # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
            word[0] ^= r_con[i]
            i += 1
        elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
            # Run word through S-box in the fourth iteration when using a
            # 256-bit key.
            word = [s_box[b] for b in word]

        # XOR with equivalent word from previous iteration.
        word = bytes(i^j for i, j in zip(word, key_columns[-iteration_size]))
        key_columns.append(word)

    # Group key words in 4x4 byte matrices.
    return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]


def decrypt(key, ciphertext):
    round_keys = expand_key(key) # Remember to start from the last round key and work backwards through them when decrypting

    #print(round_keys)

    for i, key in enumerate(round_keys):
        if type(key[0]) != list:
            round_keys[i] = [list(x) for x in key]

    #print(round_keys)

    # Convert ciphertext to state matrix

    statem = bytes2matrix(ciphertext)
    
    add_round_key(statem, round_keys[0])
    inv_shift_rows(statem)
    sub_bytes(statem, sbox=inv_s_box)

    # Initial add round key step
    for i in range(N_ROUNDS - 1, 0, -1):
        add_round_key(statem, round_keys[i-1])
        inv_mix_columns(statem)
        inv_shift_rows(statem)
        sub_bytes(statem, sbox=inv_s_box)

    # Run final round (skips the InvMixColumns step)
    add_round_key(statem, round_keys[0])

    # Convert state matrix to plaintext
    
    plaintext = matrix2bytes(statem)
    return plaintext

print('final flag:', decrypt(key, ciphertext))

