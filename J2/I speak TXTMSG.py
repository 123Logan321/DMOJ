shortTerm = None
Form = ['CU',':-)',':-(',';-)',':-P','(~.~)','TA','CCC','CUZ','TY','YW','TTYL']
Match = ['see you',"I'm happy","I'm unhappy","wink","stick out my tongue","sleepy",
         "totally awesome","Canadian Computing Competition","because","thank-you","you're welcome","talk to you later"]
while shortTerm != 'TTYL':
    shortTerm = input()
    if shortTerm in Form:
        for i in range(len(Form)):
            if Form[i] == shortTerm:
                print (Match[i])
    else:
        print(shortTerm)