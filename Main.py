import cv2.cv2 as cv
from Functions import Functions

def main():

#przykładowy obraz:
    img = 'lenna.bmp'

    print('Co chcesz zrobić?')
    print('1. Wyświetl oryginalny obraz')
    print('2. Negatyw')
    print('3. Konwersja do odcieni szarości')
    print('4. Normalizacja histogramu')
    print('5. Skalowanie')
    print('6. Progowanie')
    print('7.Filtry - rozmycie')
    print('8. Filtry - rozmycie Gaussa')
    print('9. Filtr medianowy')
    print('10. Zmiana przestrzeni kolorów z RGB na GRAY')
    print('11. Zmiana przestrzeni kolorów z RGB na HSV')
    print('12. Rotacja')
    print('13. Zmiana jasności')

    __in = int(input("Podaj liczbę: "))

    if __in == 1:
        Functions.show('original image', cv.imread(img))
    elif __in == 2:
        Functions.show('negative', Functions.negative(img))
    elif __in == 3:
        Functions.show('grayed out', Functions.grayedOut(img))
    elif __in == 4:
        Functions.show('histogram equalizing', Functions.equalizeHistogram(img))
    elif __in == 5:
        __scale = float(input('Podaj skalę: '))
        Functions.show('scaling', Functions.scaling(img, __scale))
    elif __in == 6:
        Functions.show('thresh binary', Functions.threshBinary(img))
    elif __in == 7:
        Functions.show('blurring', Functions.imageBlurring(img, 5))
    elif __in == 8:
        Functions.show('Gaussian blurring', Functions.GaussianBlurring(img, 5))
    elif __in == 9:
        Functions.show('median blurring', Functions.medianBlur(img, 5))
    elif __in == 10:
        Functions.show('changing colorspace BGR2GRAY', Functions.changingColorSpace_BGR2GRAY(img))
    elif __in == 11:
        Functions.show('changing colorspace BGR2HSV', Functions.changingColorSpace_BGR2HSV(img))
    elif __in == 12:
        __angle = int(input('Podaj kąt <0,360>: '))
        Functions.show('rotation 90', Functions.rotation(img, __angle))
    elif __in == 13:
        isBrighter = bool(input("Jaśniej(True) czy ciemniej(False)? "))
        Functions.show('brighter', Functions.brightnessChanging(img, isBrighter))



if __name__ == "__main__":

    main()