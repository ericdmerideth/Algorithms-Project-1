"""
Algorithms Project 1
Eric Merideth - Jake Speets -
"""


import e_d_crypt
import k_gen
import d_sig

def main():
    '''Main driver'''
    # Generate RSA keys
    k_gen.generateKeys(1000, 10000)  # Generates RSA keys, where p and q are prime numbers in range 1,000 - 10,000
    print('RSA keys have been generated.')

    new_n = k_gen.n_perm
    new_e = k_gen.e_perm
    new_d = k_gen.d_perm
    sigs = []
    e_sigs = []
    e_msg = []
    msg_count = 0

    prog_exit = False
    while (prog_exit == False):
        # User type selection

        print ('Please select your user type:')
        print ('\t1. A public user')
        print ('\t2. The owner of the keys')
        print ('\t3. Exit program')
        u_sel = input("\nEnter your choice: ")

        # A public user
        if (u_sel == '1'):
            pub = True

            while (pub == True):
                # List of options for public user to do
                print ('\nAs a public user, what would you like to do?')
                print ('\t1. Send an encrypted message')
                print ('\t2. Authenticate a digital signature')
                print ('\t3. Exit')
                p_sel = input("\nEnter your choice: ")

                # Send an encrypted message
                if (p_sel == '1'):
                    message = input('\nEnter a message: ')
                    msg_count += 1
                    e_msg.append(e_d_crypt.encrypt_string(message, new_e, new_n))
                    print ('Message encrypted and sent.')

                # Authenticate a digital signature
                elif (p_sel == '2'):
                    if not sigs: # If no signatures in the signature array
                        print ('There are no signatures to authenticate')

                    else: # If there are signatures to be read
                        auth_exit = False
                        a_choices = [] # Signatures the public user may choose from
                        while (auth_exit == False):

                            # Displays all available signatures
                            print ('\nThe following messages are available:')
                            for i in range(0, len(sigs), 1):
                                print (i + 1, '. ', sigs[i])
                                a_choices.append(i + 1)

                            # Prompts for choice
                            a_sel = input("\nEnter your choice: ")
                            a_sel = int(a_sel)

                            if (int(a_sel) > 0 & int(a_sel) <= len(sigs)): # See if the choice was a valid number

                                auth_check = d_sig.authenticate(e_sigs[int(a_sel) - 1], k_gen.n_perm, k_gen.e_perm)
                                test_sig = e_sigs[int(a_sel) - 1]
                                test_encryption = list()

                                # Appends all digits to a new array for easier passing
                                for i in test_sig:
                                    test_encryption.append(e_d_crypt.encrypt_recursive(i, k_gen.e_perm, k_gen.n_perm))

                                 # If the digital signature can authenticate the encrypted signature with the provided n and e, it is valid
                                if (auth_check == test_encryption):
                                    print ('Signature is valid.')

                                else:
                                    print ('Signature is invalid.')

                            auth_exit = True

                # Return to main menu
                elif (p_sel == '3'):
                    k_own = True
                    print ('\n')

        # The owner of the keys
        elif (u_sel == '2'):
            k_own = True

            # List of options for owner to do
            while (k_own == True):
                print ('\nAs the owner of the keys, what would you like to do?')
                print ('\t1. Decrypt a received message')
                print ('\t2. Digitally sign a message')
                print ('\t3. Exit')
                o_sel = input("\nEnter your choice: ")

                # Decrypt a received message
                if (o_sel == '1'):
                    if not e_msg: # If no messages in the encrypted messages array
                        print ('There are no messages to decrypt')

                    else:
                        # Makes sure user enters a valid choice
                        decrypt_exit = False
                        decrypt_choices = []
                        while (decrypt_exit == False):

                            print ('\nThe following messages are available:')
                            # Displays all currently available encrypted messages
                            for i in range(len(e_msg)):
                                print (i + 1, '. (Length =', len(e_msg[i]), ')')
                                decrypt_choices.append(i + 1)

                            decrypt_choice = input("\nEnter your choice: ")

                            # If there was a valid choice then the message is decrypted
                            if (int(decrypt_choice) > 0 & int(decrypt_choice) <= msg_count):
                                decrypted_message = ''
                                for i in range(len(e_msg[int(decrypt_choice) - 1])):
                                    decrypted_message = e_d_crypt.decrypt_string(e_msg[int(decrypt_choice) - 1], k_gen.d_perm, k_gen.n_perm)
                                    decrypted_message = e_d_crypt.convertToChar(decrypted_message)
                                    final = "".join(decrypted_message)

                                print ('Decrypted message:', final) # Prints the decrypted string
                            decrypt_exit = True # Exits menu

                # Digitally sign a message
                elif (o_sel == '2'):
                    signed_message = input('\nEnter a message: ')
                    sigs.append(signed_message) # stores signature in signature list
                    enc_sign = (e_d_crypt.encrypt_string(signed_message, k_gen.e_perm, k_gen.n_perm)) # encrypts the signature for processing
                    e_sigs.append(d_sig.sign(enc_sign, k_gen.n_perm, k_gen.d_perm)) # signs the encrypted signature and stores in array

                    print ('Message signed and sent.')

                # Return to main menu
                elif (o_sel == '3'):
                    k_own = False
                    print ('\n')

        # Exit program
        elif (u_sel == '3'):
            prog_exit = True

        else: # Makes sure user enters a proper choice
            print('\nPlease enter a valid choice (1-3).\n')

    print ('\nThanks for Playing!')

main()