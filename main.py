import RPi.GPIO as GPIO
import time

option = input('enter optie:\n'
               '[1] voorbeeld digits\n'
               '[2] zelf invullen\n')
if int(option) == 1:
    tekst = 'HO1_'
    change_clock = input('verander kloksnelheid? (y/n)')
    if change_clock.lower() == 'y':
        clk_speed = input('verversing: ')
        print(f"vers iedere {clk_speed} sec")
    elif change_clock.lower() == 'n':
        clk_speed = 0.005
elif int(option) == 2:
    tekst = input(" ↓↓↓↓ vul zelf de digits in. (lege plekken met '_' underscore invullen)"
                  "\n>")
    change_clock = input('verander kloksnelheid? (y/n)')
    if change_clock.lower() == 'y':
        clk_speed = input('verversing: ')
        print(f"vers iedere {clk_speed} sec")
    elif change_clock.lower() == 'n':
        clk_speed = 0.005

bits = {
    '1': '01100000',
    '2': '11011010',
    '3': '11110010',
    '4': '01100110',
    '5': '10110110',
    '6': '10111110',
    '7': '11100000',
    '8': '11111110',
    '9': '11110110',
    '0': '11111100',
    '.': '00000001',
    '_': '00000000',
    'o': '00111010',
    'O': '11111100',
    'P': '11001110',
    'S': '10110110',
    'J': '01111000',
    'H': '01101110',
    'h': '00101110',
    'Y': '01110110',
    'U': '01111100',
    'C': '10011100',
    'b': '00111110',
    'd': '01111010',
    'E': '10011110',
    'F': '10001110',
    'L': '00011100',
    'A': '11101110',
    'T': '10001100',
    'G': '10111100',
    '-': '00000010'
}

a = 17
b = 18
c = 19
d = 20
e = 21
f = 22
g = 23
h = 6

D1 = 26
D2 = 27
D3 = 16
D4 = 25


def main():
    if len(tekst) == 4:
        GPIO.setmode(GPIO.BCM)  # zet pin mode

        GPIO.setup(a, GPIO.OUT)
        GPIO.setup(b, GPIO.OUT)
        GPIO.setup(c, GPIO.OUT)
        GPIO.setup(d, GPIO.OUT)
        GPIO.setup(e, GPIO.OUT)
        GPIO.setup(f, GPIO.OUT)
        GPIO.setup(g, GPIO.OUT)
        GPIO.setup(h, GPIO.OUT)

        GPIO.setup(D1, GPIO.OUT)
        GPIO.setup(D2, GPIO.OUT)
        GPIO.setup(D3, GPIO.OUT)
        GPIO.setup(D4, GPIO.OUT)

        digit_list = (D1, D2, D3, D4)

        running = True
        try:
            while running:
                d_bytes = {}
                for idx, char in enumerate(tekst):
                    d_bytes[idx] = bits[char]

                for idx, digit in enumerate(digit_list):
                    GPIO.output(digit, 0)
                    GPIO.output(a, int(d_bytes[idx][0]))
                    GPIO.output(b, int(d_bytes[idx][1]))
                    GPIO.output(c, int(d_bytes[idx][2]))
                    GPIO.output(d, int(d_bytes[idx][3]))
                    GPIO.output(e, int(d_bytes[idx][4]))
                    GPIO.output(f, int(d_bytes[idx][5]))
                    GPIO.output(g, int(d_bytes[idx][6]))
                    GPIO.output(h, int(d_bytes[idx][7]))

                    time.sleep(float(clk_speed))

                    GPIO.output(a, 0)
                    GPIO.output(b, 0)
                    GPIO.output(c, 0)
                    GPIO.output(d, 0)
                    GPIO.output(e, 0)
                    GPIO.output(f, 0)
                    GPIO.output(g, 0)
                    GPIO.output(h, 0)

                    GPIO.output(digit, 1)
        except KeyboardInterrupt:
            print(' Interrupted ')
            GPIO.cleanup()
            exit(0)

    else:
        print('Je tekst voldoet niet aan 4 tekens.\nzorg dat de tekst niet langer of korter is dan 4 tekens')
        exit(0)
    GPIO.cleanup()


if __name__ == '__main__':
    main()
