# Theodoro Bertol Dev (Abeelha) #
# || Day 3 of #100DaysOfCode || #


print("\nWelcome to the little lost bee minigame!.\nOh no! you are lost! Your mission is to find your hive!")

tree_river = input("\nYou find yourself hungry and lost in the woods,\n in your surroundings you can see a big tree and a river, which way will you go?\n Tree or River: ")
low_tree_river = tree_river.lower()

if low_tree_river == "tree":
    print("\nOh no! you thought that tree was your hive's, but its actualy from hornets!")
    print(r"""
                                                         .
                                              .         ;  
                 .              .              ;%     ;;   
                   ,           ,                :;%  %;   
                    :         ;                   :;%;'     .,   
           ,.        %;     %;            ;        %;'    ,;
             ;       ;%;  %%;        ,     %;    ;%;    ,%'
              %;       %;%;      ,  ;       %;  ;%;   ,%;' 
               ;%;      %;        ;%;        % ;%;  ,%;'
                `%;.     ;%;     %;'         `;%%;.%;'
                 `:;%.    ;%%. %@;        %; ;@%;%'
                    `:%;.  :;bd%;          %;@%;'
                      `@%:.  :;%.         ;@@%;'   
                        `@%.  `;@%.      ;@@%;         
                          `@%%. `@%%    ;@@%;        
                            ;@%. :@%%  %@@%;       
                              %@bd%%%bd%%:;     
                                #@%%%%%:;;
                                %@@%%%::;
                                %@@@%(o);  . '         
                                %@@@o%;:(.,'         
                            `.. %@@@o%::;         
                               `)@@@o%::;         
                                %@@(o)::;        
                               .%@@@@%::;         
                               ;%@@@@%::;.          
                              ;%@@@@%%:;;;. 
                          ...;%@@@@@%%:;;;;,..          
""")
    print("\nYou died, game over")
elif low_tree_river == "river":
    print("\nGood choice! you find a tasty flower by the river, that means you can get some pollen and restore your stamina to keep going!")
    print(r"""
                                                    ....
                                       ,;;'''';;,                    ,;;;;,
                             ,        ;;'      `;;,               .,;;;'   ;
                          ,;;;       ;;          `;;,';;;,.     ,%;;'     '
                        ,;;,;;       ;;         ,;`;;;, `;::.  %%;'
                       ;;;,;;;       `'       ,;;; ;;,;;, `::,%%;'
                       ;;;,;;;,          .,%%%%%'% ;;;;,;;   %;;;
             ,%,.      `;;;,;;;,    .,%%%%%%%%%'%; ;;;;;,;;  %;;;
            ;,`%%%%%%%%%%`;;,;;'%%%%%%%%%%%%%'%%'  `;;;;;,;, %;;;
            ;;;,`%%%%%%%%%%%,; ..`%%%%%%%%;'%%%'    `;;;;,;; %%;;
             `;;;;;,`%%%%%,;;/, .. `"'''',%%%%%      `;;;;;; %%;;,
                `;;;;;;;,;;/////,.    ,;%%%%%%%        `;;;;,`%%;;
                       ;;;/%%%%,%///;;;';%%%%%%,          `;;;%%;;,
                      ;;;/%%%,%%%%%/;;;';;'%%%%%,             `%%;;
                     .;;/%%,%%%%%//;;'  ;;;'%%%%%,             %%;;,
                     ;;//%,%%%%//;;;'   `;;;;'%%%%             `%;;;
                     ;;//%,%//;;;;'      `;;;;'%%%              %;;;,
                     `;;//,/;;;'          `;;;'%%'              `%;;;
                       `;;;;'               `;'%'                `;;;;
                                              '      .,,,.        `;;;;
                                                  ,;;;;;;;;;;,     `;;;;
                                                 ;;;'    ;;;,;;,    `;;;;
                                                 ;;;      ;;;;,;;.   `;;;;
                                                  `;;      ;;;;;,;;   ;;;;
                                                    `'      `;;;;,;;  ;;;;
                                                               `;;,;, ;;;;
                                                                  ;;, ;;;;
                                                                    ';;;;;
                                                                     ;;;;;
                                                                    .;;;;'
                                                                   .;;;;'
                                                                  ;;;;;'
                                                                 ,;;;;'

          """)
    noise_sound = input("\nNow you can hear a loud noise, will you follow it or ignore it?\nFollow / Ignore: ")
    low_noise_sound = noise_sound.lower()
    print(r"""
                                  ...vvvv)))))).
       /~~\               ,,,c(((((((((((((((((/
      /~~c \.         .vv)))))))))))))))))))\``
          G_G__   ,,(((KKKK//////////////'
        ,Z~__ '@,gW@@AKXX~MW,gmmmz==m_.
       iP,dW@!,A@@@@@@@@@@@@@@@A` ,W@@A\c
       ]b_.__zf !P~@@@@@*P~b.~+=m@@@*~ g@Ws.
          ~`    ,2W2m. '\[ ['~~c'M7 _gW@@A`'s
            v=XX)====Y-  [ [    \c/*@@@*~ g@@i
           /v~           !.!.     '\c7+sg@@@@@s.
          //              'c'c       '\c7*X7~~~~
         ]/                 ~=Xm_       '~=(Gm_.
          """)
    if low_noise_sound == "follow":
        print("\nOh no! the loud noise was actualy a Human with a chainsaw!!!")
        print(r"""
                                   __)),
                                //_ _)
                                ( '\ '
                                 \_-/
                             ,---/  '---.
                            /     - -    \
                           /  \_. _|__,/  \
                          /  )\        )\_ \
                         / _/  (   '  ) /  /
                        / |     (_____) | /
                       /,'      /     \/ /,
                     _/(_      (   ._, )-'
                    `--,/      |____|__|
                               |    )  |
                               |   /   |
                               |  / \  |
                              / `|  | _)
                              |  |  |  |
                              |  /  \  |
                              | |    \ |
                              | \    | \_
                             /__(    '-._`,
              """)
        print("\nThe human killed you, Game over")
    elif low_noise_sound == "ignore":
        pollen_Y_N = input("\nNow you can see a bee on the ground, she's weak and need some pollen, you stil got some from the flower from before\n give the pollen to her?\nYes / No: ")
        low_pollen_Y_N = pollen_Y_N.lower()
        if pollen_Y_N == "no":
            print("\nThe weak bee was a worker from your hive, but she died, now you dont know how to get back to the hive, because you didnt help her...")
            print(r"""
              \     /
          \    X ^ X    /
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )%%%%%%%(  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(%%%%%%%)\  \     )
    (__/___/ (%%%%%%%) \___\__)
            /(       )\
          /   (%%%%%)   \
               (%%%)
                 !)
                  """)
            print("\nYou died... Game over!")
        elif low_pollen_Y_N == "yes":
            print("\nGood choice! the weak bee was a worker from your hive, you not just helped her, but now she took you back to the hive!")
            print(r"""
     ^^      .-=-=-=-.  ^^
 ^^        (`-=-=-=-=-`)         ^^
         (`-=-=-=-=-=-=-`)  ^^         ^^
   ^^   (`-=-=-=-=-=-=-=-`)   ^^                            ^^
       ( `-=-=-=-(@)-=-=-` )      ^^
       (`-=-=-=-=-=-=-=-=-`)  ^^
       (`-=-=-=-=-=-=-=-=-`)              ^^
       (`-=-=-=-=-=-=-=-=-`)                      ^^
       (`-=-=-=-=-=-=-=-=-`)  ^^
        (`-=-=-=-=-=-=-=-`)          ^^
         (`-=-=-=-=-=-=-`)  ^^                 ^^
           (`-=-=-=-=-`)
            `-=-=-=-=-`
                  """)
            print("\nYou found the way back to the hive! well done! you won! GGWP")

