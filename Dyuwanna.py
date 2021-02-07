from playsound import playsound

print('Hey Phoebe? :) ')
playsound('Question.mp3')
answer = input('So whaddya say?? ')
if 'no' in answer:
    playsound('nope.mp3')
    print(':(')
else:
    print(r'''
                    .------,
      .\/.          |______|
    _\_}{_/_       _|_Ll___|_
     / }{ \       [__________]          .\/.
      '/\'        /          \        _\_\/_/_
                 ()  o  o    ()        / /\ \
                  \ ~~~   .  /          '/\'
             _\/   \ '...'  /    \/_
              \\   {`------'}    //
               \\  /`---/',`\\  //
                \/'  o  | |\ \`//
                /'      | | \/ /\
   __,. -- ~~ ~|    o   `\|      |~ ~~ -- . __
               |                 |
               \    o            /
                `._           _.'
                   ^~- . -  ~^

    ''')
    playsound('Transition.mp3')
    playsound('Finish.mp3')




