class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        self.result = ''
        for letter in original_text:
            self.index = self.alphabet.find(letter.lower(), 0)
            if self.index >= 0:
                self.index_ciphed = self.index + shift
                if self.index_ciphed > len(self.alphabet)-1:
                    self.index_ciphed = self.index_ciphed - len(self.alphabet)
                self.letter_ciphed = self.alphabet[self.index_ciphed]
                # if letter.isupper():
                #     self.letter_ciphed = self.letter_ciphed.upper()
                self.result += self.letter_ciphed
            else:
                self.result += letter
        return self.result

    def decipher(self, cipher_text, shift):
        return self.cipher(cipher_text, -shift)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
