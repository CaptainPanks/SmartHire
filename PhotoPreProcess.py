from transform import four_point_transform
import cv2, imutils
import imgEnhance

def preProcess():
    image = cv2.imread("test.png")
    ratio = image.shape[0] / 800.0
    image = imutils.resize(image, height=800)

    grayImage  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gaussImage = cv2.GaussianBlur(grayImage, (5, 5), 0)
    edgedImage = cv2.Canny(gaussImage, 75, 200)

    cnts = cv2.findContours(edgedImage.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    return  screenCnt, ratio, image


def PreProcessing():
    screenCnt, ratio, image = preProcess()

    warped = four_point_transform(image, screenCnt.reshape(4, 2) * ratio)

    enhancer = imgEnhance.Enhancer()
    enhancedImg = enhancer.gamma(warped,1.63)

    cv2.imwrite('1.png',warped)

#    cv2.imshow("org", imutils.resize(image, height=800))
#    cv2.imshow("gamma", imutils.resize(enhancedImg, height=800))
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

PreProcessing()

