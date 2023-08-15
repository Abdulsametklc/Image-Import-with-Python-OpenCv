import cv2 #opencv kütüphanesini içe aktarır

# Resmi belirtilen dosya yolundan yükle ("C:\OPENCV\messi5.jpg") ve 0 ile siyah-beyaz formatta oku
img = cv2.imread("C:\OPENCV\messi5.jpg", 0) #resmimizi dosyamızdan okurken kullanıyoruz.

#gYüklenen resmi görselleştir
cv2.imshow("Ilk Resim",img) # parametre olarak verdiğiniz bir mat nesnesini resim tipine dönüştürerek bir pencere içerisinde ekranda gösterir

#Kullanıcın bir tuşa basmasını bekler ve basılan tuşun ASCII değerini alır.
k = cv2.waitKey(0) & 0xFF

#Eğer tuş 'ESC' (ASCII: 27) ise tüm pencereleri kapat
if k == 27: #wsc
    cv2.destroyAllWindows()
    
#Eğer tuş 's' ise (ASCII: 115), görüntüyü "messi_gray.png" adıyla kaydet ve pencereleri kapat.   
elif k == ord('s'): #ord ASCII değerini döndüren bir fonksiyondur.
    cv2.imwrite("messi_gray.png",img)
    cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    