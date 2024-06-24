# Substitution1

## Description

A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again. Download the message [here](https://artifacts.picoctf.net/c/181/message.txt "PicoCTF link to download enciphered flag text file").

## Hints

* Try a frequency attack

* Do the punctuation and the individual words help you make any substitutions?

## Walkthrough

If we open the enciphered flag found in the [message.txt](./message.txt "Enciphered flag text file") file we'll find the following text.

```
ZWDg (gejfw djf zacwpfx wex dqar) afx a wscx jd zjicpwxf gxzpfbws zjicxwbwbjv. Zjvwxgwavwg afx cfxgxvwxm hbwe a gxw jd zeaqqxvrxg hebze wxgw wexbf zfxawbybws, wxzevbzaq (avm rjjrqbvr) gnbqqg, avm cfjtqxi-gjqybvr atbqbws. Zeaqqxvrxg pgpaqqs zjyxf a vpitxf jd zawxrjfbxg, avm hexv gjqyxm, xaze sbxqmg a gwfbvr (zaqqxm a dqar) hebze bg gptibwwxm wj av jvqbvx gzjfbvr gxfybzx. ZWDg afx a rfxaw has wj qxafv a hbmx affas jd zjicpwxf gxzpfbws gnbqqg bv a gadx, qxraq xvybfjvixvw, avm afx ejgwxm avm cqasxm ts iavs gxzpfbws rfjpcg afjpvm wex hjfqm djf dpv avm cfazwbzx. Djf webg cfjtqxi, wex dqar bg: cbzjZWD{DF3LP3VZS_4774ZN5_4F3_Z001_4871X6DT}
```

This time we don't have a key, so we'll have to use [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis "Wikipedia page for frequency analysis"). There are many frequency analysis tools online; a good one can be found at [101 Computing](https://www.101computing.net/frequency-analysis/ "101 Computing frequency analysis tools").

Before we begin identifying which character maps to which, we start with a completely blank slate. Leaving our deciphered text looking like this, where every unknown character is represented with an asterisk.

```
**** (***** *** ******* *** ****) *** * **** ** ******** ******** ***********. *********** *** ********* **** * *** ** ********** ***** **** ***** **********, ********* (*** ********) ******, *** *******-******* *******. ********** ******* ***** * ****** ** **********, *** **** ******, **** ****** * ****** (****** * ****) ***** ** ********* ** ** ****** ******* *******. **** *** * ***** *** ** ***** * **** ***** ** ******** ******** ****** ** * ****, ***** ***********, *** *** ****** *** ****** ** **** ******** ****** ****** *** ***** *** *** *** ********. *** **** *******, *** **** **: *******{**3**3***_4774**5_4*3_*001_4871*6**}
```

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | ?        |
| B          | --><-- | ?        |
| C          | --><-- | ?        |
| D          | --><-- | ?        |
| E          | --><-- | ?        |
| F          | --><-- | ?        |
| G          | --><-- | ?        |
| H          | --><-- | ?        |
| I          | --><-- | ?        |
| J          | --><-- | ?        |
| K          | --><-- | ?        |
| L          | --><-- | ?        |
| M          | --><-- | ?        |
| N          | --><-- | ?        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | ?        |
| R          | --><-- | ?        |
| S          | --><-- | ?        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | ?        |
| W          | --><-- | ?        |
| X          | --><-- | ?        |
| Y          | --><-- | ?        |
| Z          | --><-- | ?        |

If we look at the ciphertext we can identify the flag, which will allow us to plug in our first values.

```cbzjZWD{DF3LP3VZS_4774ZN5_4F3_Z001_4871X6DT}```

We know the flag starts with ```picoCTF``` so we'll start mapping those to the characters ```cbzjZWD```.

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | ?        |
| B          | --><-- | I        |
| C          | --><-- | P        |
| D          | --><-- | F        |
| E          | --><-- | ?        |
| F          | --><-- | ?        |
| G          | --><-- | ?        |
| H          | --><-- | ?        |
| I          | --><-- | ?        |
| J          | --><-- | O        |
| K          | --><-- | ?        |
| L          | --><-- | ?        |
| M          | --><-- | ?        |
| N          | --><-- | ?        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | ?        |
| R          | --><-- | ?        |
| S          | --><-- | ?        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | ?        |
| W          | --><-- | T        |
| X          | --><-- | ?        |
| Y          | --><-- | ?        |
| Z          | --><-- | C        |

Deciphered text so far:

```
CTF* (**O*T FO* C*PT*** T** F***) *** * T*P* OF CO*P*T** **C**IT* CO*P*TITIO*. CO*T**T**T* *** P*****T** *IT* * **T OF C********* **IC* T**T T**I* C***TI*IT*, T*C**IC** (*** *OO**I**) **I***, *** P*O****-*O**I** **I*IT*. C********* ******* CO*** * ****** OF C*T**O*I**, *** **** *O****, **C* *I**** * *T*I** (C***** * F***) **IC* I* ****ITT** TO ** O**I** *CO*I** ****IC*. CTF* *** * ****T *** TO ***** * *I** ***** OF CO*P*T** **C**IT* **I*** I* * **F*, ***** ***I*O****T, *** *** *O*T** *** P***** ** **** **C**IT* **O*P* **O*** T** *O*** FO* F** *** P**CTIC*. FO* T*I* P*O****, T** F*** I*: PICOCTF{F*3**3*C*_4774C*5_4*3_C001_4871*6F*}
```

After this first step in deciphering we can already make out a couple words, for instance ```CO*P*TITIO*``` might be the word competition. In the cipher text it is the word ```zjicxwbwbjv```. Now we can map "i" to "m", "x" to "e", and "v" to "n". 

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | ?        |
| B          | --><-- | I        |
| C          | --><-- | P        |
| D          | --><-- | F        |
| E          | --><-- | ?        |
| F          | --><-- | ?        |
| G          | --><-- | ?        |
| H          | --><-- | ?        |
| I          | --><-- | M        |
| J          | --><-- | O        |
| K          | --><-- | ?        |
| L          | --><-- | ?        |
| M          | --><-- | ?        |
| N          | --><-- | ?        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | ?        |
| R          | --><-- | ?        |
| S          | --><-- | ?        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | N        |
| W          | --><-- | T        |
| X          | --><-- | E        |
| Y          | --><-- | ?        |
| Z          | --><-- | C        |

Deciphered text so far:

```
CTF* (**O*T FO* C*PT**E T*E F***) **E * T*PE OF COMP*TE* *EC**IT* COMPETITION. CONTE*T*NT* **E P*E*ENTE* *IT* * *ET OF C****EN*E* **IC* TE*T T*EI* C*E*TI*IT*, TEC*NIC** (*N* *OO**IN*) **I***, *N* P*O**EM-*O**IN* **I*IT*. C****EN*E* ******* CO*E* * N*M*E* OF C*TE*O*IE*, *N* **EN *O**E*, E*C* *IE*** * *T*IN* (C***E* * F***) **IC* I* ***MITTE* TO *N ON*INE *CO*IN* *E**ICE. CTF* **E * **E*T *** TO *E**N * *I*E ***** OF COMP*TE* *EC**IT* **I*** IN * **FE, *E*** EN*I*ONMENT, *N* **E *O*TE* *N* P***E* ** M*N* *EC**IT* **O*P* **O*N* T*E *O*** FO* F*N *N* P**CTICE. FO* T*I* P*O**EM, T*E F*** I*: PICOCTF{F*3**3NC*_4774C*5_4*3_C001_4871E6F*}
```

Every time we do this, more words will jump out at you. For instance, the first sentence contains three 3 letter words, FO*, T*E, and **E, along with one single letter word, *. These are most likely the words FOR, THE, and ARE. The single letter is most likely I or A, since those are the only 1 letter words in English.


* ```djf --> FO*``` (Possibly FOR)
* ```wex --> T*E``` (Possibly THE)
* ```afx --> **E``` (Possibly ARE)
* ```a --> *``` (Possibly I or A)

This would mean that the ciphertext letter "f" most likely maps to "R", "e" to "H", and "a" to "A".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | A        |
| B          | --><-- | I        |
| C          | --><-- | P        |
| D          | --><-- | F        |
| E          | --><-- | H        |
| F          | --><-- | R        |
| G          | --><-- | ?        |
| H          | --><-- | ?        |
| I          | --><-- | M        |
| J          | --><-- | O        |
| K          | --><-- | ?        |
| L          | --><-- | ?        |
| M          | --><-- | ?        |
| N          | --><-- | ?        |
| O          | --><-- | ?        |
| P          | --><-- | ?        |
| Q          | --><-- | ?        |
| R          | --><-- | ?        |
| S          | --><-- | ?        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | N        |
| W          | --><-- | T        |
| X          | --><-- | E        |
| Y          | --><-- | ?        |
| Z          | --><-- | C        |

Deciphered text so far:

```
CTF* (*HORT FOR CAPT*RE THE F*A*) ARE A T*PE OF COMP*TER *EC*RIT* COMPETITION. CONTE*TANT* ARE PRE*ENTE* *ITH A *ET OF CHA**EN*E* *HICH TE*T THEIR CREATI*IT*, TECHNICA* (AN* *OO**IN*) **I***, AN* PRO**EM-*O**IN* A*I*IT*. CHA**EN*E* ***A*** CO*ER A N*M*ER OF CATE*ORIE*, AN* *HEN *O**E*, EACH *IE*** A *TRIN* (CA**E* A F*A*) *HICH I* ***MITTE* TO AN ON*INE *CORIN* *ER*ICE. CTF* ARE A *REAT *A* TO *EARN A *I*E ARRA* OF COMP*TER *EC*RIT* **I*** IN A *AFE, *E*A* EN*IRONMENT, AN* ARE HO*TE* AN* P*A*E* ** MAN* *EC*RIT* *RO*P* ARO*N* THE *OR** FOR F*N AN* PRACTICE. FOR THI* PRO**EM, THE F*A* I*: PICOCTF{FR3**3NC*_4774C*5_4R3_C001_4871E6F*}
```

So many new words begin to stand out, but we'll stick with the first sentence. It's safe to assume that ```(*HORT FOR CAPT*RE THE F*A*) ARE A T*PE OF COMP*TER``` is ```(SHORT FOR CAPTURE THE FLAG) ARE A TYPE OF COMPUTER```.

* ```gejfw --> *HORT``` (Possibly SHORT)
* ```zacwpfx --> CAPT*RE``` (Possibly CAPTURE)
* ```dqar --> F*A*``` (Possibly FLAG)
* ```wscx --> T*PE``` (Possibly TYPE)
* ```zjicpwxf --> COMP*TER``` (Possibly COMPUTER)

The new mappings are "g" is "S", "p" is "U", "q" is "L", "r" is "G", AND "s" is "Y".

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | A        |
| B          | --><-- | I        |
| C          | --><-- | P        |
| D          | --><-- | F        |
| E          | --><-- | H        |
| F          | --><-- | R        |
| G          | --><-- | S        |
| H          | --><-- | ?        |
| I          | --><-- | M        |
| J          | --><-- | O        |
| K          | --><-- | ?        |
| L          | --><-- | ?        |
| M          | --><-- | ?        |
| N          | --><-- | ?        |
| O          | --><-- | ?        |
| P          | --><-- | U        |
| Q          | --><-- | L        |
| R          | --><-- | G        |
| S          | --><-- | Y        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | N        |
| W          | --><-- | T        |
| X          | --><-- | E        |
| Y          | --><-- | ?        |
| Z          | --><-- | C        |

Deciphered text so far:

```
CTFS (SHORT FOR CAPTURE THE FLAG) ARE A TYPE OF COMPUTER SECURITY COMPETITION. CONTESTANTS ARE PRESENTE* *ITH A SET OF CHALLENGES *HICH TEST THEIR CREATI*ITY, TECHNICAL (AN* GOOGLING) S*ILLS, AN* PRO*LEM-SOL*ING A*ILITY. CHALLENGES USUALLY CO*ER A NUM*ER OF CATEGORIES, AN* *HEN SOL*E*, EACH YIEL*S A STRING (CALLE* A FLAG) *HICH IS SU*MITTE* TO AN ONLINE SCORING SER*ICE. CTFS ARE A GREAT *AY TO LEARN A *I*E ARRAY OF COMPUTER SECURITY S*ILLS IN A SAFE, LEGAL EN*IRONMENT, AN* ARE HOSTE* AN* PLAYE* *Y MANY SECURITY GROUPS AROUN* THE *ORL* FOR FUN AN* PRACTICE. FOR THIS PRO*LEM, THE FLAG IS: PICOCTF{FR3*U3NCY_4774C*5_4R3_C001_4871E6F*}
```

Next we'll knock out the words "AND" (```avm --> AN*```) and "WITH" (```hbwe --> *ITH```).

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | A        |
| B          | --><-- | I        |
| C          | --><-- | P        |
| D          | --><-- | F        |
| E          | --><-- | H        |
| F          | --><-- | R        |
| G          | --><-- | S        |
| H          | --><-- | W        |
| I          | --><-- | M        |
| J          | --><-- | O        |
| K          | --><-- | ?        |
| L          | --><-- | ?        |
| M          | --><-- | D        |
| N          | --><-- | ?        |
| O          | --><-- | ?        |
| P          | --><-- | U        |
| Q          | --><-- | L        |
| R          | --><-- | G        |
| S          | --><-- | Y        |
| T          | --><-- | ?        |
| U          | --><-- | ?        |
| V          | --><-- | N        |
| W          | --><-- | T        |
| X          | --><-- | E        |
| Y          | --><-- | ?        |
| Z          | --><-- | C        |

Deciphered text so far:

```
CTFS (SHORT FOR CAPTURE THE FLAG) ARE A TYPE OF COMPUTER SECURITY COMPETITION. CONTESTANTS ARE PRESENTED WITH A SET OF CHALLENGES WHICH TEST THEIR CREATI*ITY, TECHNICAL (AND GOOGLING) S*ILLS, AND PRO*LEM-SOL*ING A*ILITY. CHALLENGES USUALLY CO*ER A NUM*ER OF CATEGORIES, AND WHEN SOL*ED, EACH YIELDS A STRING (CALLED A FLAG) WHICH IS SU*MITTED TO AN ONLINE SCORING SER*ICE. CTFS ARE A GREAT WAY TO LEARN A WIDE ARRAY OF COMPUTER SECURITY S*ILLS IN A SAFE, LEGAL EN*IRONMENT, AND ARE HOSTED AND PLAYED *Y MANY SECURITY GROUPS AROUND THE WORLD FOR FUN AND PRACTICE. FOR THIS PRO*LEM, THE FLAG IS: PICOCTF{FR3*U3NCY_4774C*5_4R3_C001_4871E6F*}
```

We can continue doing this until all words are finally revealed.

* ```gnbqqg --> S*ILLS``` (SKILLS)
* ```cfjtqxi-gjqybvr atbqbws --> PRO*LEM-SOL*ING A*ILITY``` (PROBLEM-SOLVING ABILITY)
* ```DF3LP3VZS --> FR3*U3NCY``` (FR3QU3NCY)

Map so far:

| SUBSTITUTE | --><-- | ORIGINAL |
|:----------:|:------:|:--------:|
| A          | --><-- | A        |
| B          | --><-- | I        |
| C          | --><-- | P        |
| D          | --><-- | F        |
| E          | --><-- | H        |
| F          | --><-- | R        |
| G          | --><-- | S        |
| H          | --><-- | W        |
| I          | --><-- | M        |
| J          | --><-- | O        |
| K          | --><-- | ?        |
| L          | --><-- | Q        |
| M          | --><-- | D        |
| N          | --><-- | K        |
| O          | --><-- | ?        |
| P          | --><-- | U        |
| Q          | --><-- | L        |
| R          | --><-- | G        |
| S          | --><-- | Y        |
| T          | --><-- | B        |
| U          | --><-- | ?        |
| V          | --><-- | N        |
| W          | --><-- | T        |
| X          | --><-- | E        |
| Y          | --><-- | V        |
| Z          | --><-- | C        |

Deciphered text so far:

```
CTFS (SHORT FOR CAPTURE THE FLAG) ARE A TYPE OF COMPUTER SECURITY COMPETITION. CONTESTANTS ARE PRESENTED WITH A SET OF CHALLENGES WHICH TEST THEIR CREATIVITY, TECHNICAL (AND GOOGLING) SKILLS, AND PROBLEM-SOLVING ABILITY. CHALLENGES USUALLY COVER A NUMBER OF CATEGORIES, AND WHEN SOLVED, EACH YIELDS A STRING (CALLED A FLAG) WHICH IS SUBMITTED TO AN ONLINE SCORING SERVICE. CTFS ARE A GREAT WAY TO LEARN A WIDE ARRAY OF COMPUTER SECURITY SKILLS IN A SAFE, LEGAL ENVIRONMENT, AND ARE HOSTED AND PLAYED BY MANY SECURITY GROUPS AROUND THE WORLD FOR FUN AND PRACTICE. FOR THIS PROBLEM, THE FLAG IS: PICOCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}
```

Finally, we fully uncover the hidden message and flag.

```PICOCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}```
