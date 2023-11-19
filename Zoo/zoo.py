"""Project zoo"""
print("""I love animals!
Let's check out the animals...""")

camel = r"""
The camel habitat...
 ___.-''''-.
/___ @     |
',,,,.     |          _.'''''''._
     '     |         /           \
     |      \    _.-'              \
     |       '.-'                   '-.
     |                                 ',
     |                                   '',
      ',,-,                              ':;
           ',,| ;,,                    ,' ;;
              ! ; !'',,,',',,,,'!    ;    ;:
             : ;   ! !      ! !  ;   ;    :;
              ; ;   ! !     ! !    ; ;    ;,
             ; ;    ! !     ! !    ; ;
             ; ;    ! !     ! !    ; ;
             ;,,    !,!     !,!    ;,;
             /_I    L_I     L_I    /_I
Look at that!"""

rabbit = r"""
The rabbit habitat...
             ,
            /|      __
           / |   ,-~ /
          Y :|  // /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
        /  "~"  |
       Y   _,   |
      /| ;-"~ _ l
     /  l/   ,-"~ \
     \//\/ .-      \
     Y    /         Y
     l    I         !
     ]\   _\       /"\
    (" ~----( ~    Y. )
It looks fine!"""

lion = r"""
The lion habitat...

   \|\||
  -' ||||/
 /7   |||||/
/    |||||||/`-.____________
\-' |||||||||               `-._
 -|||||||||||               |` -`.
   ||||||               \   |   `\\
    |||||\  \______...---\_  \    \\
       |  \  \           | \  |    ``-.__--.
       |  |\  \         / / | |       ``---'
     _/  /_/  /      __/ / _| |
    (,__/(,__/      (,__/ (,__/

The lion is roaring!"""

deer = r"""
The deer habitat...
        ,/  \.
       |(    )|
  \`-._:,\  /.;_,-'/
   `.\_`\')(`/'_/,'
       )/`.,'\(
       |.    ,|
       :6)  (6;
        \`\ _(\
         \._'; `.___...---..________...------._
          \   |   ,'   .  .     .       .     .`:.
           \`.' .  .         .   .   .     .   . \\
            `.       .   .  \  .   .   ..::: .    ::
              \ .    .  .   ..::::::::''  ':    . ||
               \   `. :. .:'            \  '. .   ;;
                `._  \ ::: ;           _,\  :.  |/(
                   `.`::: /--....---''' \ `. :. :`\`
                    | |:':               \  `. :.\
                    | |' ;                \  (\  .\
                    | |.:                  \  \`.  :
                    |.| |                   ) /  :.|
                    | |.|                  /./   | |
                    |.| |                 / /    | |
                    | | |                /./     |.|
                    ;_;_;              ,'_/      ;_|
                   '-/_(              '--'      /,' 
Pretty good!"""

goose = r"""
The goose habitat...

                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
Beautiful!"""

bat = r"""
The bat habitat...
     ,*-~"`^"*u_                                _u*"^`"~-*,
  p!^       /  jPw                            w9j \        ^!p
w^.._      /      "\_                      _/"     \        _.^w
     *_   /          \_      _    _      _/         \     _* 
       q /           / \q   ( `--` )   p/ \          \   p
       jj5****._    /    ^\_) o  o (_/^    \    _.****6jj
                *_ /      "==) ;; (=="      \ _*
                 `/.w***,   /(    )\   ,***w.\"
                  ^ ilmk ^c/ )    ( \c^      ^
                          'V')_)(_('V'
                              `` ``
It's doing fine."""

zoo_animals = [camel, rabbit, lion, deer, goose, bat]
print("""
0 -- camel habitat
1 -- rabbit habitat
2 -- lion habitat
3 -- deer habitat
4 -- goose habitat
5 -- bat habitat""")
while True :
    animal = input("""Please enter the number of the habitat you would like to
view>""")
    if animal == "exit":
        print("See you later!")
        break
    try:
        animal_number = int(animal)
        if 0 <= animal_number <= 5:
            print(zoo_animals[animal_number])
        else:
            print(f"We dont have an animal number {animal_number}!")
    except ValueError:
        print("Try an integer!")