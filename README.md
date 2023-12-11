# OpenCV-References
Just doing some ![Kenny](https://github.com/AusafMo/OpenCV-References/assets/75237046/0484b5e6-e77c-4779-aa84-ecfb94737419)

### Math and Algorithms Behind Some Functions :

1) Filters and Blurrs (similar to most algorithms): [Computerphile](https://www.youtube.com/watch?v=C_zFhWdM4ic&list=PLzH6n4zXuckoRdljSlM2k35BufTYXNNeF&index=1&pp=iAQB)

2) Edge Basics: [First Principle of Computer Vision](https://www.youtube.com/watch?v=G8yp6f9V_6c&list=PL2zRqk16wsdqXEMpHrc4Qnb5rA1Cylrhx&index=2&pp=iAQB)

3) Gradients in more detail: [First Principle of Computer Vision](https://www.youtube.com/watch?v=lOEBsQodtEQ&pp=ygUqY29tcHV0ZXIgdmlzaW9uIGZpcnN0IHByaW5jaXBsZXMgZ3JhZGllbnRz)

4) Edge Detection, Sobel Operator: [Computerphile](https://www.youtube.com/watch?v=uihBwtPIBxM&list=PLzH6n4zXuckoRdljSlM2k35BufTYXNNeF&index=2&pp=iAQB)

5) Canny Edge Detection: [Computerphile](https://www.youtube.com/watch?v=sRFM5IEqR2w&list=PLzH6n4zXuckoRdljSlM2k35BufTYXNNeF&index=3&pp=iAQB) or [First Principles of Computer Vision](https://www.youtube.com/watch?v=hUC1uoigH6s)


6) Contour Algorithm (Suzuki Contour Tracing Algorithm): [AI Learner](https://theailearner.com/2019/11/19/suzukis-contour-tracing-algorithm-opencv-python/ ) or [StackOverflow](https://stackoverflow.com/questions/10427474/what-is-the-algorithm-that-opencv-uses-for-finding-contours)


### About the Haar-Cascade Classifier Code for Gender Recognition

1) Well, it turns out, in a classic fashion, I  didn't realize that haar cascade is a BINARY Classifier as someone pointed out on [StackOverflow](https://stackoverflow.com/questions/27966447/gender-recognition-haarcascade), they suggested some alternatives like making two classifiers for male and female, and then comparing them to return the result. <br>
And I am not doing that, not only it's not up to the use case requirements I have, but also sounds like a lot of (unnecessary?) work for a basic haar-cascade and I've got tea to make. <br>
Instead, I'd rather train a ResNet or other pre-trained models (in another repo probably dedicated to this task). <br>
 I revised the basics though, that's a plus (ig 🙃). <br>

2) The dataset I used and will be using in the future is available on [Kaggle](https://www.kaggle.com/datasets/maciejgronczynski/biggest-genderface-recognition-dataset).

3) What parameters mean in face_detect.py's haar_cascade.detecMultiscale() method : [StackOverflow](https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters)
