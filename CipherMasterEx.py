class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        self.result = ''
        shift = shift if is_encrypt else -shift
        for letter in text:
            self.index = self.alphabet.find(letter.lower(), 0)
            if self.index >= 0:
                self.index_ciphed = self.index + shift
                if self.index_ciphed > len(self.alphabet)-1:
                    self.index_ciphed = self.index_ciphed - len(self.alphabet)
                self.letter_ciphed = self.alphabet[self.index_ciphed]
                self.result += self.letter_ciphed
            else:
                self.result += letter
        return self.result


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
