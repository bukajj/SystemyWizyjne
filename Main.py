from Functions import show
from Functions import negative
from Functions import grayedOut
from Functions import equalizeHistogram

def main():

#przykładowy obraz:
    img = 'lenna.bmp'
    show('Lenna', img)
    negative(img)
    grayedOut(img)
    equalizeHistogram(img)


if __name__ == "__main__":
    main()