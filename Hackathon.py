print("Welcome to FITMIND")
name = str(input("Enter your Name\n"))
age= int(input("Enter your age\n"))
print(age , name)
print()
ans = int(input("IS this information is correct, If yes then press 1 if no then 2\n"))
if ans!=1:
   print("Enter again")
   name = str(input("Enter your Name\n"))
   age= int(input("Enter your age\n"))
else:
   print("Good")   
Assesment= int(input("If you want to take self assesment for any neurological disorder then press 1 else 0\n"))

if Assesment==1:
    A= int(input("Persistent or sudden onset of a headache, if yes then type 1 else 0\n"))
    B= int(input("Loss of feeling or tingling, if yes then type 1 else 0\n"))
    C= int(input("Loss of sight or double vision if yes then type 1 else 0\n"))
    D= int(input("Have Memory loss, if yes then type 1 else 0\n"))

    if A!=1 and B!=1 and C!=1 and D!=1:
        print("Good News you dont have any symptoms of any neurological disorder, To maintain this you have to play some suggested games on our app")
    else:       
        print("Answer these questions to know which neorological disorder you may have and best game for exercising your mind for that particular disorder\n")
    #Amnesia
    Aans1= int(input("Any Stroke, if yes then type 1 else 0\n"))
    Aans2= int(input("Have Brain tumor, if yes then type 1 else 0\n"))
    Aans3= int(input("Long-term alcohol abuse, if yes then type 1 else 0\n"))
    Aans4= int(input("Any head injuries, if yes then type 1 else 0\n"))

    #Stroke
    Bans1= int(input("Trouble speaking and understanding what others are saying, if yes then type 1 else 0\n"))
    Bans2= int(input("Paralysis or numbness of the face, arm or leg, if yes then type 1 else 0\n"))
    Bans3= int(input("Problems seeing in one or both eyes, if yes then type 1 else 0\n"))
    Bans4= int(input(" A sudden, severe headache, which may be accompanied by vomiting, dizziness or altered consciousness, if es then type 1 else 0\n"))
    Bans5= int(input("have sudden dizziness or a loss of coordination, if yes then type 1 else 0\n"))

    #Alzheimer
    Cans1= int(input(" Loss of memory with inability to recall, if yes then type 1 else 0\n"))
    Cans2= int(input("Forget time,place,way, purpose of here, if yes then type 1 else 0\n"))
    Cans3= int(input("Alread suffering from depression, anxiety, Insormnia, if yes then type 1 else 0\n"))
    Cans4= int(input("Make poor judgement like wearing sweater in summer, if yes then type 1 else 0\n"))

    #Parkinson
    Dans1= int(input(" A tremor, or shaking, usually begins in a limb, often your hand or fingers , if yes then type 1 else 0\n"))
    Dans2= int(input("Rigid muscles. Muscle stiffness may occur in any part of your body, if yes then type 1 else 0"))
    Dans3= int(input("Your posture may become stooped, or you may have balance problems, if yes then type 1 else 0"))
    Dans4= int(input("You may have a decreased ability to perform unconscious movements, including blinking, smiling or swinging your arms when you walk, if yes then press 1 else 0"))
    Dans5= int(input("Your speech may be more of a monotone rather than have the usual inflections, if yes then type 1 else 0\n"))



    if Aans1==1 or Aans2==1  or Aans3==1 or Aans4==1:
        print("You are likely to have Amnesia and you need to consult a neurologist and play games on our app for atleast 30 min daily ")
    elif Bans1==1 or Bans3==1 or Bans2==1 and Bans4==1 or Bans5==1:
        print("You are likely to have Stroke and you need to consult a neurologist and play suggested games on our app for atleat 30 min daily")
    elif Cans1==1 or Cans2==1 and Cans3==1 or Cans4==1:
        print("You are likely to have Alzheimer and you need to consult a neurologist and play suggested games on app for atleast 30 min daily")
    elif Dans1==1 or Dans2==1 and Dans3==1 or Dans4==1 or Dans5==1:
        print("You are likely to have Parkinson and you need to consult a neurologist and play suggested games on app for atleast 30 min daily")
    else :
        print("Your mental strenght is good for now but keep exercising daily with plaing games 10 to 20 min on our app")
else:
    print("Enjoy our game")        